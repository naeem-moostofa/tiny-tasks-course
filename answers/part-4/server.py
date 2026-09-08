import html
import socket
from urllib.parse import parse_qs, urlsplit


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000

items = [
    {"id": 1, "text": "Pack lunch", "done": True},
    {"id": 2, "text": "Read chapter 4", "done": False},
    {"id": 3, "text": "I added this in Python", "done": False},
]
next_id = 4


def make_page(items_to_show):
    item_html = ""

    for item in items_to_show:
        mark = "✓" if item["done"] else "○"
        item_text = html.escape(item["text"])
        item_html += f"""
          <li>
            <form action="/toggle?id={item['id']}" method="post">
              <button type="submit" aria-label="Toggle {item_text}">{mark}</button>
            </form>
            <span>{item_text}</span>
            <form action="/delete?id={item['id']}" method="post">
              <button type="submit">Delete</button>
            </form>
          </li>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tiny Tasks</title>
  </head>
  <body>
    <main>
      <h1>Tiny Tasks</h1>
      <p>One small thing at a time.</p>
      <section>
        <h2>My list</h2>
        <ul>{item_html}</ul>
        <form action="/add" method="post">
          <label for="new-item">New item</label>
          <input id="new-item" name="text" type="text" placeholder="New item…" required>
          <input type="submit" value="Add item">
        </form>
      </section>
    </main>
  </body>
</html>"""


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Listening on port {SERVER_PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)

    request_line = request.splitlines()[0]
    method, target, version = request_line.split()
    target_parts = urlsplit(target)
    path = target_parts.path
    query = parse_qs(target_parts.query)

    if method == "GET" and path == "/":
        content = make_page(items)
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + content
    elif method == "POST":
        if path == "/add":
            body = request.partition("\r\n\r\n")[2]
            text = parse_qs(body).get("text", [""])[0].strip()
            items.append({"id": next_id, "text": text, "done": False})
            next_id += 1
        elif path == "/toggle":
            item_id = int(query["id"][0])
            for item in items:
                if item["id"] == item_id:
                    item["done"] = not item["done"]
                    break
        elif path == "/delete":
            item_id = int(query["id"][0])
            items[:] = [item for item in items if item["id"] != item_id]

        response = "HTTP/1.1 303 See Other\r\nLocation: /\r\n\r\n"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\nPage not found"

    client_socket.sendall(response.encode())
    client_socket.close()
