// ── Theme Toggle ──────────────────────────────────────
const html = document.documentElement;
const toggleBtn = document.getElementById('themeToggle');
const themeIcon = document.getElementById('themeIcon');

const savedTheme = localStorage.getItem('theme') || 'dark';
html.setAttribute('data-theme', savedTheme);
updateIcon(savedTheme);

if (toggleBtn) {
  toggleBtn.addEventListener('click', () => {
    const current = html.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateIcon(next);
  });
}

function updateIcon(theme) {
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
  }
}

// ── Sliders ───────────────────────────────────────────
document.querySelectorAll('.slider').forEach(slider => {
  const valEl = document.getElementById(slider.id + 'Val');
  if (valEl) {
    slider.addEventListener('input', () => {
      valEl.textContent = slider.value;
      updateSliderColor(slider);
    });
    updateSliderColor(slider);
  }
});

function updateSliderColor(slider) {
  const pct = ((slider.value - slider.min) / (slider.max - slider.min)) * 100;
  slider.style.background = `linear-gradient(90deg, var(--accent) ${pct}%, var(--surface2) ${pct}%)`;
}

// ── Progress Bar ──────────────────────────────────────
const form = document.getElementById('assessmentForm');
const progressFill = document.getElementById('progressFill');

if (form && progressFill) {
  const fields = form.querySelectorAll('input[required], select[required]');
  const total = fields.length;

  function updateProgress() {
    const filled = [...fields].filter(f => f.value.trim() !== '').length;
    progressFill.style.width = `${(filled / total) * 100}%`;
  }

  fields.forEach(f => f.addEventListener('input', updateProgress));
  fields.forEach(f => f.addEventListener('change', updateProgress));
}

// ── Form Submit Loader ────────────────────────────────
if (form) {
  form.addEventListener('submit', () => {
    const btn = document.getElementById('submitBtn');
    const loader = document.getElementById('btnLoader');
    if (btn && loader) {
      btn.querySelector('span').textContent = 'Analyzing...';
      loader.classList.remove('hidden');
      btn.disabled = true;
    }
  });
}

// ── Result Ring Animation ─────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const ring = document.querySelector('.ring-fill');
  if (ring) {
    const offset = ring.style.strokeDashoffset;
    ring.style.strokeDashoffset = '327';
    setTimeout(() => { ring.style.strokeDashoffset = offset; }, 200);
  }
});
