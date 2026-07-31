<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly ist ein Claude Code Plugin für kurze, freundliche und schrittweise Ausgabestile in zehn Sprachen.">
</p>

# Brain Fog Friendly

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | Deutsch | [Português do Brasil](./README.pt-BR.md)

Ein Claude Code marketplace Plugin für Ausgabestile mit niedriger kognitiver Belastung.

Es hilft Claude, mit weniger Druck, weniger Dichte und klareren nächsten Schritten zu antworten.

Es ist für Menschen mit Brain Fog, Aufmerksamkeitsproblemen, Müdigkeit, Überforderung oder für alle, die ruhige Antworten Schritt für Schritt bevorzugen.

## Was du bekommst

Zehn lokalisierte Ausgabestile:

| Sprache | Ausgabestil |
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

## Was der Stil ändert

Er bittet Claude darum:

- Fazit und nächsten Schritt zuerst zu nennen
- kurze Sätze zu verwenden
- kurze Absätze zu verwenden
- kognitive Belastung zu reduzieren
- jeweils nur einen kleinen Schritt weiterzugehen
- Druck, Bewertungen und zu viele Optionen zu vermeiden
- wenn die Person feststeckt, einfache Optionen anzubieten: fortfahren, einfacher erklären oder pausieren

## Installation

Füge dieses Repository als Claude Code marketplace hinzu:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Installiere dann das Plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Nutzung

Öffne die Claude Code Konfiguration:

```text
/config
```

Wähle dann einen der Brain Fog Friendly Ausgabestile.

## Lokale Entwicklung

Füge dieses Repository als lokalen marketplace hinzu:

```bash
claude plugin marketplace add .
```

Installiere aus dem lokalen marketplace:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Validiere das Plugin:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
