"""Build the public, static course website in dist/."""

from pathlib import Path
import shutil


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIRECTORY = (PROJECT_ROOT / "dist").resolve()
PUBLIC_FILES = ("index.html", "styles.css", "script.js", "favicon.svg")
PUBLIC_DIRECTORIES = ("answers",)


def build_site():
    """Copy only public course files into a clean deployment directory."""
    if OUTPUT_DIRECTORY.parent != PROJECT_ROOT:
        raise RuntimeError("Refusing to clean an output directory outside this project.")

    if OUTPUT_DIRECTORY.exists():
        shutil.rmtree(OUTPUT_DIRECTORY)
    OUTPUT_DIRECTORY.mkdir()

    for filename in PUBLIC_FILES:
        source = PROJECT_ROOT / filename
        if not source.is_file():
            raise FileNotFoundError(f"Missing required public file: {filename}")
        shutil.copy2(source, OUTPUT_DIRECTORY / filename)

    for directory_name in PUBLIC_DIRECTORIES:
        source = PROJECT_ROOT / directory_name
        if not source.is_dir():
            raise FileNotFoundError(f"Missing required public directory: {directory_name}")
        shutil.copytree(source, OUTPUT_DIRECTORY / directory_name)

    print(f"Built the tutorial and answer key in {OUTPUT_DIRECTORY}")


if __name__ == "__main__":
    build_site()
