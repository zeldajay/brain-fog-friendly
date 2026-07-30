# Brain Fog Friendly

A Claude Code marketplace plugin with low-cognitive-load output styles.

It is designed for people with brain fog, attention difficulty, fatigue, overwhelm, or anyone who prefers short, gentle, step-by-step responses.

## Included output styles

- `脑雾友好` — Chinese version
- `Brain Fog Friendly` — English version

## Install

From this repository directory:

```bash
claude plugin install .
```

Or install from a cloned copy:

```bash
git clone <this-repository-url>
cd brain-fog-friendly
claude plugin install .
```

## Use

In Claude Code, select the output style:

```text
/output-style
```

Then choose either:

- `脑雾友好`
- `Brain Fog Friendly`

## What this style does

It asks Claude to:

- use short sentences
- use short paragraphs
- reduce cognitive load
- move one small step at a time
- put the conclusion and next step first
- avoid pressure, judgment, and too many options
- offer simple choices when the user is stuck

## Validate

```bash
claude plugin validate .
```

## License

MIT
