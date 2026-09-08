from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

lists = [
    {
        "id": 1,
        "name": "School",
        "items": [
            {"id": 1, "text": "Pack lunch", "done": True},
            {"id": 2, "text": "Read chapter 4", "done": False},
        ],
    },
    {
        "id": 2,
        "name": "Home",
        "items": [
            {"id": 3, "text": "Buy groceries", "done": False},
        ],
    },
]
next_list_id = 3
next_item_id = 4


@app.get("/")
def index():
    return render_template("index.html", lists=lists)


@app.post("/lists")
def add_list():
    global next_list_id
    lists.append(
        {"id": next_list_id, "name": request.form["name"], "items": []}
    )
    next_list_id += 1
    return redirect(url_for("index"))


@app.post("/lists/<int:list_id>/delete")
def delete_list(list_id):
    lists[:] = [task_list for task_list in lists if task_list["id"] != list_id]
    return redirect(url_for("index"))


@app.post("/lists/<int:list_id>/items")
def add_item(list_id):
    global next_item_id
    for task_list in lists:
        if task_list["id"] == list_id:
            task_list["items"].append(
                {"id": next_item_id, "text": request.form["text"], "done": False}
            )
            next_item_id += 1
            break
    return redirect(url_for("index"))


@app.post("/items/<int:item_id>/toggle")
def toggle_item(item_id):
    for task_list in lists:
        for item in task_list["items"]:
            if item["id"] == item_id:
                item["done"] = not item["done"]
                return redirect(url_for("index"))
    return redirect(url_for("index"))


@app.post("/items/<int:item_id>/delete")
def delete_item(item_id):
    for task_list in lists:
        task_list["items"] = [
            item for item in task_list["items"] if item["id"] != item_id
        ]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
