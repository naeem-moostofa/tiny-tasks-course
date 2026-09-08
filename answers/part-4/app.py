import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
database_filename = "todo.db"


def get_db(database_path):
    connection = sqlite3.connect(database_path)
    return connection


def init_db(connection):
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS lists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            list_id INTEGER NOT NULL,
            text TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (list_id) REFERENCES lists (id)
        )
        """
    )
    connection.commit()


@app.get("/")
def index():
    connection = get_db(database_filename)
    list_rows = connection.execute("SELECT id, name FROM lists").fetchall()
    lists = []

    for list_id, name in list_rows:
        item_rows = connection.execute(
            "SELECT id, text, done FROM items WHERE list_id = ?", (list_id,)
        ).fetchall()
        lists.append(
            {
                "id": list_id,
                "name": name,
                "items": [
                    {"id": item_id, "text": text, "done": bool(done)}
                    for item_id, text, done in item_rows
                ],
            }
        )

    connection.close()
    return render_template("index.html", lists=lists)


@app.post("/lists")
def add_list():
    connection = get_db(database_filename)
    connection.execute(
        "INSERT INTO lists (name) VALUES (?)", (request.form["name"],)
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.post("/lists/<int:list_id>/delete")
def delete_list(list_id):
    connection = get_db(database_filename)
    connection.execute("DELETE FROM items WHERE list_id = ?", (list_id,))
    connection.execute("DELETE FROM lists WHERE id = ?", (list_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.post("/lists/<int:list_id>/items")
def add_item(list_id):
    connection = get_db(database_filename)
    connection.execute(
        "INSERT INTO items (list_id, text, done) VALUES (?, ?, ?)",
        (list_id, request.form["text"], 0),
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.post("/items/<int:item_id>/toggle")
def toggle_item(item_id):
    connection = get_db(database_filename)
    current_done = connection.execute(
        "SELECT done FROM items WHERE id = ?", (item_id,)
    ).fetchone()[0]
    connection.execute(
        "UPDATE items SET done = ? WHERE id = ?",
        (0 if current_done == 1 else 1, item_id),
    )
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


@app.post("/items/<int:item_id>/delete")
def delete_item(item_id):
    connection = get_db(database_filename)
    connection.execute("DELETE FROM items WHERE id = ?", (item_id,))
    connection.commit()
    connection.close()
    return redirect(url_for("index"))


if __name__ == "__main__":
    connection = get_db(database_filename)
    init_db(connection)
    connection.close()
    app.run(debug=True)
