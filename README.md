# Tiny Tasks beginner course

This repository contains a single-page tutorial for a complete beginner. The learner builds a small multi-list to-do app in four stages:

1. Static HTML
2. A raw Python HTTP server with in-memory data
3. Flask with templates
4. Flask with an SQLite database

Each lesson follows one learning loop: watch the video, understand its key concepts, put the video starter into the real project, complete one numbered exercise sequence, and compare the result with a visual checkpoint. Only code derived from the videos is shown; the finished app is never provided as a copy-and-paste solution.

There is only one project. The learner puts each video starter directly into the real file for that stage and changes it there. Every lesson uses the same visible sequence: video, concepts, starter, one numbered exercise, and checkpoint.

Every function the learner must create has an explicit contract describing where it belongs, its input data, its returned output, and any side effects.

## Live websites

- Automatically deployed from `main`: <https://naeem-moostofa.github.io/tiny-tasks-course/>
- Public source repository: <https://github.com/naeem-moostofa/tiny-tasks-course>

## Instructor answer key

The independently completed snapshots are in [`answers/`](answers/). Each `part-*` directory is self-contained and represents the end of one lesson. The public tutorial links to the answer index so learners can compare their work when they are ready. See [`answers/README.md`](answers/README.md) for run instructions and expected behavior.

## Run the tutorial locally

Open a terminal in this folder and run:

```powershell
python -m http.server 8000
```

Then visit [http://localhost:8000](http://localhost:8000).

On macOS or Linux, use `python3 -m http.server 8000` if `python` is not available.

The page stores checked lesson progress in the browser's local storage. No account or internet connection is required, except to watch the embedded YouTube videos or load the Google Fonts.

## Deploy the course

The public deployment contains the tutorial and the complete answer key. Follow [`DEPLOY.md`](DEPLOY.md) for the automatic GitHub Pages workflow.
