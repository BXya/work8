# Work8

Work8 is the product-facing release shell for the WorkBuddy Agent OS alpha.

It turns the current OpenClaw-native task loop into something reviewable:

```text
OpenClaw conversation
-> Work8 native ingress
-> WorkBuddy task state
-> Work Receipt
-> Work8 Home
```

The product rule is simple:

- OpenClaw is the user entry.
- Work8 Home is the read-only task surface.
- Work Receipts are the shareable deliverables.
- The substrate remains the source of truth.
- CLI commands stay in the operator path.

## Current Release

`workbuddy-agent-os-v1.0.0-alpha.1`

Pinned components:

| Component | Commit | Repository |
| --- | --- | --- |
| `workbuddy-native-ingress` | `95666b7` | <https://github.com/BXya/workbuddy-native-ingress> |
| `goclaw-stack` | `ec9a7d3` | <https://github.com/BXya/goclaw-stack> |
| `openclaw-substrate` | `bcc0bf4` | <https://github.com/BXya/openclaw-substrate> |

## What Works

- Fresh clone rehearsal passed from clean directories.
- Plugin doctor passed.
- Clean install gate passed without mutating the global runtime.
- Quickstart sample task generated a Home URL and Work Receipt.
- Real Windows-local OpenClaw `2026.5.18` dogfood created a WorkBuddy task.
- Work8 Home showed the latest task.
- Work Receipt opened successfully.
- `openclaw health` and `openclaw gateway status` did not trigger WorkBuddy side effects.

See [Alpha Acceptance](docs/ALPHA_ACCEPTANCE.md).

## Product Surface

Open the static product shell:

```text
site/index.html
```

For a live local runtime, the accepted Home URL shape is:

```text
http://127.0.0.1:8790/index.html?data=/api/dashboard
```

For fresh clone dry-runs:

```text
http://127.0.0.1:<port>/index.html?data=/runs/latest/dashboard-projection.json
```

## Architecture

See [Architecture](docs/ARCHITECTURE.md).

## Quickstart

See [Quickstart](docs/QUICKSTART.md).

## Release Manifest

The pinned release manifest is in [manifest.json](manifest.json).

Validate it with:

```bash
python scripts/verify_release.py
```

## Known Limitation

The WorkBuddy hook payload is correct and contains task status, Home link, receipt link, and next step. The visible OpenClaw assistant text can still be generic. The next hardening step is to make the WorkBuddy reply contract the primary user-visible response body.
