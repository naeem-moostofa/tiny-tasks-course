const checks = [...document.querySelectorAll(".course-check")];
const progressLabel = document.querySelector("#progress-label");
const progressBar = document.querySelector("#progress-bar");
const storageKey = "tiny-tasks-course-progress";

function readProgress() {
  try {
    return JSON.parse(localStorage.getItem(storageKey)) || [];
  } catch {
    return [];
  }
}

function updateProgress() {
  const completed = checks.filter((check) => check.checked).map((check) => check.dataset.step);
  const percent = checks.length ? (completed.length / checks.length) * 100 : 0;
  localStorage.setItem(storageKey, JSON.stringify(completed));
  progressLabel.textContent = `${completed.length} of ${checks.length} steps`;
  progressBar.style.width = `${percent}%`;
  const progressRegion = progressLabel.closest("[role='progressbar']");
  progressRegion.setAttribute("aria-valuemax", checks.length);
  progressRegion.setAttribute("aria-valuenow", completed.length);
}

const completedSteps = readProgress();
checks.forEach((check) => {
  check.checked = completedSteps.includes(check.dataset.step);
  check.addEventListener("change", updateProgress);
});
updateProgress();

document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const code = button.closest(".code-card").querySelector("code").innerText;
    try {
      await navigator.clipboard.writeText(code);
      const oldLabel = button.textContent;
      button.textContent = "Copied!";
      setTimeout(() => { button.textContent = oldLabel; }, 1400);
    } catch {
      button.textContent = "Select + copy";
    }
  });
});

document.querySelector("#reset-progress").addEventListener("click", () => {
  checks.forEach((check) => { check.checked = false; });
  updateProgress();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

const sections = [...document.querySelectorAll("main > section[id]")];
const navLinks = [...document.querySelectorAll(".sidebar nav a")];

if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting);
    if (!visible.length) return;
    const currentId = visible.sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0].target.id;
    navLinks.forEach((link) => link.classList.toggle("active", link.hash === `#${currentId}`));
  }, { rootMargin: "-25% 0px -60%", threshold: [0, 0.1, 0.25] });
  sections.forEach((section) => observer.observe(section));
}
