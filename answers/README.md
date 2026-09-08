# Tiny Tasks answer key

Each `part-*` directory is a standalone snapshot of the learner's project at the end of that lesson. Run commands from inside the chosen part directory.

These files show one valid solution, not the only valid solution. Learner-chosen text and colours may differ while still satisfying the checkpoints.

## Part 1 — static HTML

```text
cd part-1
python -m http.server 8000
```

Open <http://localhost:8000>. The page shows one named list, one example checkbox, and an add-item form. The form is intentionally not connected to a Python app yet.

## Part 2 — raw Python server

```text
cd part-2
python server.py
```

Open <http://localhost:8000>. Add, toggle, and delete tasks in the single list. Changes live only in memory and reset when the server restarts.

## Part 3 — Flask with temporary memory

Install Flask in a virtual environment as described by the course, then:

```text
cd part-3
python app.py
```

Open <http://localhost:5000>. You can create and delete named lists and add, toggle, and delete their tasks. All changes reset when Flask restarts.

## Part 4 — Flask with SQLite

Install Flask in a virtual environment as described by the course, then:

```text
cd part-4
python app.py
```

Open <http://localhost:5000>. The same list and task actions now use `todo.db`, so changes survive server restarts. The included database contains the persistence-check example from the lesson.

Stop any server with `Ctrl+C`.
