<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="Brain Fog Friendly is a Claude Code plugin for short, gentle, step-by-step output styles in ten languages.">
</p>

# Brain Fog Friendly

English | [中文](./assets/readme/README.zh-CN.md) | [日本語](./assets/readme/README.ja.md) | [Русский](./assets/readme/README.ru.md) | [العربية](./assets/readme/README.ar.md) | [한국어](./assets/readme/README.ko.md) | [Español](./assets/readme/README.es.md) | [Français](./assets/readme/README.fr.md) | [Deutsch](./assets/readme/README.de.md) | [Português do Brasil](./assets/readme/README.pt-BR.md)

A Claude Code marketplace plugin for low-cognitive-load output styles.

It helps Claude answer with less pressure, less density, and clearer next steps.

It is for people with brain fog, attention difficulty, fatigue, overwhelm, or anyone who prefers calm, step-by-step replies.

## What you get

Ten localized output styles:

| Language | Output style |
| --- | --- |
| English | `Brain Fog Friendly` |
| 中文 | `脑雾友好` |
| 日本語 | `ブレインフォグにやさしい` |
| Русский | `Дружелюбный к мозговому туману` |
| العربية | `صديق لضباب الدماغ` |
| 한국어 | `브레인 포그 친화적` |
| Español | `Amigable para la niebla mental` |
| Français | `Adapté au brouillard cérébral` |
| Deutsch | `Brain-Fog-freundlich` |
| Português do Brasil | `Amigável para névoa mental` |

## What the style changes

It asks Claude to:

- put the conclusion and next step first
- use short sentences
- use short paragraphs
- reduce cognitive load
- move one small step at a time
- avoid pressure, judgment, and too many options
- offer simple choices when the user is stuck: continue, simplify, or pause

## Install

Add this repository as a Claude Code marketplace:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Then install the plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Use

Open Claude Code config:

```text
/config
```

Then:

1. Find the `Output style` setting.
2. Press Enter to open the list of output styles.
3. Use the arrow keys to move to one of the Brain Fog Friendly styles (for example `Brain Fog Friendly` or `脑雾友好`).
4. Press Enter to select it.
5. Press Esc to leave config. The style is now active.

## Local development

Add this repository as a local marketplace:

```bash
claude plugin marketplace add .
```

Install from the local marketplace:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Validate the plugin:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
