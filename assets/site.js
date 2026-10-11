(() => {
  'use strict';
  const safe = {
    get(k) { try { return localStorage.getItem(k) || ''; } catch { return ''; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch {} },
  };

  // theme: auto → light → dark
  const root = document.documentElement;
  const modes = ['auto', 'light', 'dark'];
  let mode = modes.includes(safe.get('pqTheme')) ? safe.get('pqTheme') : 'auto';
  const mq = matchMedia('(prefers-color-scheme: light)');
  const btn = document.getElementById('themeBtn');
  const labels = { auto: btn?.dataset.auto, light: btn?.dataset.light, dark: btn?.dataset.dark };
  function apply() {
    const light = mode === 'light' || (mode === 'auto' && mq.matches);
    root.dataset.theme = light ? 'light' : 'dark';
    if (btn) btn.innerHTML = '<span aria-hidden="true">' + { auto: '◐', light: '☀', dark: '☾' }[mode] + '</span><span class="lb"> ' + (labels[mode] || mode) + '</span>';
  }
  btn?.addEventListener('click', () => { mode = modes[(modes.indexOf(mode) + 1) % 3]; safe.set('pqTheme', mode); apply(); });
  mq.addEventListener?.('change', apply);
  apply();

  // remember the chosen language
  document.querySelectorAll('a[data-lang]').forEach((a) => a.addEventListener('click', () => safe.set('pqLang', a.dataset.lang)));

  // copy buttons
  document.querySelectorAll('pre').forEach((pre) => {
    const b = document.createElement('button');
    b.className = 'copy'; b.type = 'button'; b.textContent = root.lang === 'pl' ? 'Kopiuj' : 'Copy';
    b.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(pre.querySelector('code').innerText); b.textContent = root.lang === 'pl' ? 'Skopiowano' : 'Copied'; } catch { b.textContent = '!'; }
      setTimeout(() => { b.textContent = root.lang === 'pl' ? 'Kopiuj' : 'Copy'; }, 1800);
    });
    pre.append(b);
  });

  // newest version, straight from GitHub (the page works without it)
  const out = document.querySelectorAll('[data-latest]');
  if (out.length) {
    fetch('https://api.github.com/repos/party-queue/party-queue/releases/latest', { headers: { Accept: 'application/vnd.github+json' } })
      .then((r) => (r.ok ? r.json() : Promise.reject()))
      .then((rel) => {
        const apk = (rel.assets || []).find((a) => a.name === 'party-queue.apk') || (rel.assets || []).find((a) => /\.apk$/.test(a.name));
        const date = new Date(rel.published_at).toLocaleDateString(root.lang === 'pl' ? 'pl-PL' : 'en-GB', { year: 'numeric', month: 'long', day: 'numeric' });
        const mb = apk ? Math.round(apk.size / 1048576) : null;
        out.forEach((el) => {
          el.textContent = el.dataset.latest.replace('{v}', rel.tag_name.replace(/^v/, '')).replace('{date}', date).replace('{mb}', mb ?? '~225');
        });
      })
      .catch(() => {});
  }
})();
