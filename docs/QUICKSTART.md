# Quickstart

This repo is the release shell. Runtime code lives in the pinned component repos in `manifest.json`.

## 1. Inspect the release

```bash
git clone https://github.com/BXya/work8.git
cd work8
python scripts/verify_release.py
```

## 2. Open the static product shell

Open:

```text
site/index.html
```

This shows the intended Work8 product surface.

## 3. Run the actual alpha stack

Use the pinned repos:

```bash
git clone https://github.com/BXya/workbuddy-native-ingress.git
git clone https://github.com/BXya/goclaw-stack.git
git clone https://github.com/BXya/openclaw-substrate.git
```

Checkout the alpha tag in each repo:

```bash
git checkout workbuddy-agent-os-v1.0.0-alpha.1
```

Run the WorkBuddy native quickstart from `workbuddy-native-ingress`:

```bash
python scripts/workbuddy_agent_os_quickstart.py
```

The quickstart prints:

- Home URL
- sample task id
- Work Receipt URL
- doctor/reset commands

## 4. Real OpenClaw path

When the OpenClaw plugin hook is installed, a normal OpenClaw user message should create or reuse a WorkBuddy task and return:

- task status
- Home link
- receipt link
- next step

## 5. Operator fallback

The CLI remains for operator/admin recovery and diagnostics. It is not the normal user entry.
