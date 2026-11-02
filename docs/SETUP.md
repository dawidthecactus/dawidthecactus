# Botanical Telemetry: setup and maintenance

## Install

1. Create a **public** repository called `dawidthecactus` under the `dawidthecactus` GitHub account.
2. Copy the contents of this folder into the repository root. Do not upload the ZIP as one file.
3. Review `profile.json`, `README.md` and project descriptions before publishing.
4. `git add . && git commit -m "feat(profile): launch botanical telemetry v2" && git push -u origin main`
5. In GitHub, open **Actions** -> **Refresh public GitHub metrics** -> **Run workflow**. The repo needs GitHub Actions enabled; the workflow uses its built-in `GITHUB_TOKEN` with `contents: write` permission. If repository settings restrict writes, grant the action permission or disable this optional workflow.

## What renders on GitHub

- README is Markdown, with local GIF / PNG / SVG image references. It does not rely on Tailwind, HTML canvas, JavaScript, browser fonts or Googleusercontent assets.
- `hero.gif`: animated running/telemetry signal. `milestones.gif`: animated 11-milestone display. The static `*.png` versions are available as fallbacks.
- `analytics-demo.png`: **synthetic** chart, not actual finisher data.
- `github-pulse.svg`: static SVG, updated using real GitHub API data once the Actions job runs.
- The Office block is an **original text graphic linked to an official reaction GIF**. No television footage is shipped with this kit.

## Update running metrics

- Edit `profile.json`: `half_marathons_completed`, `half_marathon_goal`, etc.
- Run `python -m pip install Pillow` and `python scripts/build_assets.py`.
- The current milestone display is designed around 11 progress markers. When the 12th race is completed, adjust the cap/grid in `milestone_frame` to show 12 or more, or keep the graphic as a lifetime counter and adapt the layout.
- All images are generated locally from code. No photos, personal signatures, private invoices, credentials, or proprietary BI data are included.

## Update project links

The profile intentionally does not link to private repos. Once you publish a sanitized portfolio version of any project, add its public URL in the README.

## Optional real Dwight GIF embedding

A GIPHY link has been verified: https://giphy.com/gifs/theoffice-ZfK4cXKJTTay1Ava29 (official The Office channel).
You can replace the linked original card with an image embed from the official host if embedding is permitted and it reliably renders on GitHub. Avoid uploading copyrighted TV footage into the repo without permission.

## Note on GitHub SVG animations

A regular static SVG is used for GitHub Pulse. Animated artwork is exported as GIF because dynamic SVG animation can be browser/renderer-dependent in README previews.
