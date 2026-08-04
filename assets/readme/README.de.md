<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly ist ein Claude Code und Codex Plugin für kurze, freundliche und schrittweise Antworten in zehn Sprachen.">
</p>

# Brain-Fog-freundlich

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | Deutsch | [Português do Brasil](./README.pt-BR.md)

Ein Claude Code und Codex marketplace Plugin für Antworten mit niedriger kognitiver Belastung.

Es hilft Claude und Codex, mit weniger Druck, weniger Dichte und klareren nächsten Schritten zu antworten.

Es ist für Menschen mit Brain Fog, Aufmerksamkeitsproblemen, Müdigkeit, Überforderung oder für alle, die ruhige Antworten Schritt für Schritt bevorzugen.

## Was du bekommst

Zehn lokalisierte Antwortstile. Sie sind als Claude Code Ausgabestile und über einen Codex-Konfigurations-Skill verfügbar.

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

Er bittet Claude oder Codex darum:

- Fazit und nächsten Schritt zuerst zu nennen
- kurze Sätze zu verwenden
- kurze Absätze zu verwenden
- kognitive Belastung zu reduzieren
- jeweils nur einen kleinen Schritt weiterzugehen
- Druck, Bewertungen und zu viele Optionen zu vermeiden
- wenn die Person feststeckt, einfache Optionen anzubieten: fortfahren, einfacher erklären oder pausieren

## Installation

### Claude Code

Füge dieses Repository als Claude Code marketplace hinzu:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Installiere dann das Plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### ChatGPT Desktop-App

1. Öffne die ChatGPT Desktop-App.
2. Öffne **Plug-ins**.
3. Öffne oben rechts das Menü **Erstellen ▾** und wähle **Plug-in-Marktplatz hinzufügen**. Gib unter **Quelle** `zeldajay/brain-fog-friendly` ein und wähle dann **Marktplatz hinzufügen**.
4. Öffne auf der Plug-in-Seite die Registerkarte **Persönlich**. Öffne **Brain Fog Friendly** und wähle die Plus-Schaltfläche zur Installation.
5. Starte einen neuen Chat, damit der enthaltene Skill geladen wird.

Weitere Informationen zu unterstützten Oberflächen und zur Plugin-Verwaltung findest du im offiziellen [Leitfaden für ChatGPT- und Codex-Plugins](https://learn.chatgpt.com/docs/plugins).

### Codex CLI

Füge dieses Repository als Codex marketplace hinzu:

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

Installiere dann das Plugin:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## Nutzung

### Claude Code

Öffne die Claude Code Konfiguration:

```text
/config
```

Dann:

1. Suche die Einstellung `Output style` (Ausgabestil).
2. Drücke Enter, um die Liste der Ausgabestile zu öffnen.
3. Gehe mit den Pfeiltasten zu einem der Brain Fog Friendly Stile (zum Beispiel `Brain Fog Friendly` oder `Brain-Fog-freundlich`).
4. Drücke Enter, um ihn auszuwählen.
5. Drücke Esc, um die Konfiguration zu verlassen. Der Stil ist jetzt aktiv.

### Codex CLI

Rufe den Konfigurations-Skill ausdrücklich auf:

```text
$brain-fog-friendly
```

Codex zeigt eine nummerierte Liste mit zehn Sprachen und einer Option zum Deaktivieren. Antworte mit der Nummer, dem Sprachnamen oder dem Sprachcode.

### ChatGPT Desktop-App

Starte einen neuen Chat, gib `@` ein und wähle den Skill **Brain Fog Friendly**. Antworte dann mit einer Nummer, einem Sprachnamen oder einem Sprachcode auf die Sprachliste.

Der Skill fügt in der globalen Datei `~/.codex/AGENTS.md` einen verwalteten `brain-fog-friendly`-Block hinzu oder ersetzt ihn. Beim Deaktivieren wird nur dieser Block entfernt; alle anderen globalen Anweisungen bleiben erhalten.

Starte nach dem Aktivieren, Wechseln oder Deaktivieren einen neuen Codex-Thread, damit Codex die globalen Anweisungen neu lädt.

## Lokale Entwicklung

### Claude Code

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

### Codex

Füge diesen Checkout als lokalen marketplace hinzu:

```bash
codex plugin marketplace add .
```

Installiere aus dem lokalen marketplace:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
