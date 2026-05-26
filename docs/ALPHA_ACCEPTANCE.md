# Alpha Acceptance

Release: `workbuddy-agent-os-v1.0.0-alpha.1`

## Fresh Clone Rehearsal

Clean clone root:

```text
C:\Users\26781\AppData\Local\Temp\workbuddy-fresh-clone-20260526T014215Z
```

Passed:

- Plugin doctor: `ok=true`
- Clean install gate: `ok=true`
- Global runtime mutation: `false`
- Quickstart sample task: `ok=true`
- Home URL returned
- Receipt URL returned and opened with HTTP 200

Fresh Home URL:

```text
http://127.0.0.1:8795/index.html?data=/runs/latest/dashboard-projection.json
```

Fresh receipt URL:

```text
http://127.0.0.1:8795/runs/latest/artifacts/work-deliverable-report-20260526t014238z-4adb7086.html
```

## Real OpenClaw Dogfood

Runtime:

```text
Windows-local OpenClaw 2026.5.18
```

Message:

```text
帮我创建一个 WorkBuddy 测试任务，并生成回执。
```

Result:

- WorkBuddy hook: `ok=true`
- Task status: `Done`
- Task id: recorded in Linear beta acceptance evidence; omitted here to keep public secret scans unambiguous
- Dashboard API included the latest task
- Receipt opened with HTTP 200

Home:

```text
http://127.0.0.1:8790/index.html?data=/api/dashboard
```

Receipt:

```text
http://127.0.0.1:8790/runs/latest/artifacts/work-deliverable-report-20260526t011440z-03a9fa72.html
```

Activity log:

```text
http://127.0.0.1:8790/runs/latest/artifacts/tracebundle-trace-20260526t011440z-a2c8e1bf.html
```

## Local Gates

Passed:

- `workbuddy-native-ingress`: 16 tests OK
- `goclaw-doctor.py --mode local --json`: ok
- `goclaw-smoke.py --profile local --json`: ok
- `openclaw-substrate` via stack smoke: 40 tests OK
- Browser product check: normal UI shows Current Work / Needs You / Delivered / Runtime State
- Normal UI hides internal substrate object names

## Side-Effect Gate

`openclaw health` and `openclaw gateway status --token local` did not mutate WorkBuddy latest artifacts.

## Known Limitation

The WorkBuddy hook payload is correct. The visible OpenClaw assistant text still needs product hardening so that the WorkBuddy reply contract is the primary user-facing response.
