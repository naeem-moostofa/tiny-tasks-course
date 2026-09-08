# Deploy Tiny Tasks automatically

The public website contains the tutorial and the complete `answers/` directory. Visitors can read or download the Python source files, although a static website cannot run the Flask servers.

## Automatic deployment from GitHub

The repository includes `.github/workflows/deploy.yml`. Whenever a commit is pushed to the `main` branch, GitHub automatically:

1. checks out the current code;
2. runs `python build_site.py`;
3. uploads the generated `dist` directory; and
4. publishes it with GitHub Pages.

The repository owner does not need to run a separate deploy command. Make a change, commit it, and push it:

```powershell
git add .
git commit -m "Describe the change"
git push
```

The deployment status appears on the repository's **Actions** tab. The stable website address is:

<https://naeem-moostofa.github.io/tiny-tasks-course/>

The workflow follows GitHub's recommended Pages artifact process and grants only read access to the repository plus the two permissions required to publish Pages.

## Preview the exact public build locally

Run:

```powershell
python build_site.py
python -m http.server 8000 --directory dist
```

Visit <http://localhost:8000>. The generated `dist` directory contains the tutorial assets and all answer-key files. Press **Ctrl+C** in the terminal to stop the preview server.
