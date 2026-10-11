# party-queue.github.io

The website of [Party Queue](https://github.com/party-queue/party-queue) – <https://party-queue.github.io> – in English and Polish:
what the app does, screenshots, how to download, install and update it (with QR codes).

- `en/index.html`, `pl/index.html` – the two pages, **generated** by `tools/build.py` (all text lives in that one file, so the languages stay in step)
- `index.html` – picks the visitor's language (the choice is remembered), `404.html`, `robots.txt`, `sitemap.xml`
- `assets/` – styles, a little JavaScript (theme switch, copy buttons, the newest version read from GitHub), images
- `assets/img/qr-download.*` – QR code of `https://github.com/party-queue/party-queue/releases/latest/download/party-queue.apk`
  (the release workflow publishes every APK also under that fixed name, so the code never goes stale); `qr-site.*` – the site itself

## Working on it

```bash
python3 tools/build.py          # regenerate en/ and pl/
python3 -m http.server 8123     # look at http://127.0.0.1:8123/
```

Screenshots are `assets/img/screens/app-<name>.jpg` (the host's phone) and `web-<name>.jpg` (the guests' page). A gallery entry appears
when its file exists; the captions are in `tools/build.py`. The same pictures are in the app's repository (`docs/screenshots/`).
QR codes are made with `scripts/make-qr.sh` from the app's repository.

GitHub Pages serves the `main` branch from the root. No framework, no build step on the server.
