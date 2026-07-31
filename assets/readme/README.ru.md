<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly — плагин Claude Code для коротких, мягких, пошаговых стилей ответа на десяти языках.">
</p>

# Brain Fog Friendly

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | Русский | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

Плагин Claude Code marketplace для стилей ответа с низкой когнитивной нагрузкой.

Он помогает Claude отвечать спокойнее, короче и с более ясными следующими шагами.

Подходит людям с brain fog, трудностями внимания, усталостью, перегрузкой, а также всем, кто предпочитает спокойные пошаговые ответы.

## Что вы получаете

Десять локализованных стилей ответа:

| Язык | Стиль ответа |
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

## Что меняет этот стиль

Он просит Claude:

- сначала давать вывод и следующий шаг
- использовать короткие предложения
- использовать короткие абзацы
- снижать когнитивную нагрузку
- двигаться по одному маленькому шагу
- избегать давления, оценок и слишком большого числа вариантов
- когда пользователь застрял, предлагать простые варианты: продолжить, объяснить проще или сделать паузу

## Установка

Добавьте этот репозиторий как Claude Code marketplace:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Затем установите плагин:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Использование

Откройте настройки Claude Code:

```text
/config
```

Затем выберите один из стилей Brain Fog Friendly.

## Локальная разработка

Добавьте этот репозиторий как локальный marketplace:

```bash
claude plugin marketplace add .
```

Установите из локального marketplace:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Проверьте плагин:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
