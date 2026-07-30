# Brain Fog Friendly

A Claude Code marketplace plugin with low-cognitive-load output styles.

It is designed for people with brain fog, attention difficulty, fatigue, overwhelm, or anyone who prefers short, gentle, step-by-step responses.

## Included output styles

- `Brain Fog Friendly` — English version
- `脑雾友好` — Chinese version
- `ブレインフォグにやさしい` — Japanese version
- `브레인 포그 친화적` — Korean version
- `Amigable para la niebla mental` — Spanish version
- `Adapté au brouillard cérébral` — French version
- `Brain-Fog-freundlich` — German version
- `Amigável para névoa mental` — Brazilian Portuguese version

## Install

Add this repository as a marketplace:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Then install the plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

For local development:

```bash
claude plugin marketplace add .
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Use

In Claude Code, select the output style with `/config`. This replaces the older `/output-style` command.

```text
/config
```

Then choose one of:

- `Brain Fog Friendly`
- `脑雾友好`
- `ブレインフォグにやさしい`
- `브레인 포그 친화적`
- `Amigable para la niebla mental`
- `Adapté au brouillard cérébral`
- `Brain-Fog-freundlich`
- `Amigável para névoa mental`

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
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
