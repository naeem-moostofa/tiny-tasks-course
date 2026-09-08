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

## Existing Cloudflare Pages project

The existing `tiny-tasks-course` Cloudflare project was created with Direct Upload. Cloudflare does not allow an existing Direct Upload project to be converted to Git integration. It can still be refreshed manually with:

```powershell
python build_site.py
npx wrangler pages deploy dist --project-name tiny-tasks-course --branch main
```

Use the stable production address <https://tiny-tasks-course.pages.dev/>. Addresses beginning with a deployment hash, such as `https://3fe48045.tiny-tasks-course.pages.dev/`, refer to one fixed historical deployment and do not change after a later upload.

If automatic Cloudflare deployment is preferred over GitHub Pages, create a new Git-integrated Cloudflare Pages project and select this GitHub repository. Use `python build_site.py` as the build command, `dist` as the output directory, and `main` as the production branch.
