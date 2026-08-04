<p align="center">
  <img src="./hero.ru.svg" width="100%" alt="Brain Fog Friendly — плагин Claude Code и Codex для коротких, мягких, пошаговых ответов на десяти языках.">
</p>

# Дружелюбный к мозговому туману

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | Русский | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

Плагин marketplace для Claude Code и Codex с ответами с низкой когнитивной нагрузкой.

Он помогает Claude и Codex отвечать спокойнее, короче и с более ясными следующими шагами.

Подходит людям с brain fog, трудностями внимания, усталостью, перегрузкой, а также всем, кто предпочитает спокойные пошаговые ответы.

## Что вы получаете

Десять локализованных стилей ответа. Они доступны как стили вывода Claude Code и через навык настройки Codex.

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

Он просит Claude или Codex:

- сначала давать вывод и следующий шаг
- использовать короткие предложения
- использовать короткие абзацы
- снижать когнитивную нагрузку
- двигаться по одному маленькому шагу
- избегать давления, оценок и слишком большого числа вариантов
- когда пользователь застрял, предлагать простые варианты: продолжить, объяснить проще или сделать паузу

## Установка

### Claude Code

Добавьте этот репозиторий как Claude Code marketplace:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Затем установите плагин:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### Приложение ChatGPT для компьютера

1. Откройте приложение ChatGPT для компьютера.
2. Откройте **Плагины**.
3. Откройте меню **Создать ▾** в правом верхнем углу и выберите **Добавить маркетплейс плагинов**. Введите `zeldajay/brain-fog-friendly` в поле **Источник**, затем выберите **Добавить маркетплейс**.
4. Откройте вкладку **Личное** на странице плагинов. Откройте **Brain Fog Friendly** и нажмите кнопку с плюсом для установки.
5. Начните новый чат, чтобы загрузить включённый навык.

Сведения о поддерживаемых интерфейсах и управлении плагинами см. в официальном [руководстве по плагинам ChatGPT и Codex](https://learn.chatgpt.com/docs/plugins).

### Codex CLI

Добавьте этот репозиторий как Codex marketplace:

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

Затем установите плагин:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## Использование

### Claude Code

Откройте настройки Claude Code:

```text
/config
```

Затем:

1. Найдите настройку `Output style` (стиль вывода).
2. Нажмите Enter, чтобы открыть список стилей вывода.
3. Стрелками перейдите к одному из стилей Brain Fog Friendly (например, `Brain Fog Friendly` или `Дружелюбный к мозговому туману`).
4. Нажмите Enter, чтобы выбрать его.
5. Нажмите Esc, чтобы выйти из настроек. Стиль теперь активен.

### Codex CLI

Явно вызовите навык настройки:

```text
$brain-fog-friendly
```

Codex покажет нумерованный список из десяти языков и варианта отключения. Ответьте номером, названием языка или кодом языка.

### Приложение ChatGPT для компьютера

Начните новый чат, введите `@` и выберите навык **Brain Fog Friendly**. Затем ответьте на список номером, названием языка или кодом языка.

Навык добавляет или заменяет управляемый блок `brain-fog-friendly` в глобальном файле `~/.codex/AGENTS.md`. Отключение удаляет только этот блок и сохраняет все остальные глобальные инструкции.

После включения, переключения или отключения стиля начните новый поток Codex, чтобы заново загрузить глобальные инструкции.

## Локальная разработка

### Claude Code

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

### Codex

Добавьте эту рабочую копию как локальный marketplace:

```bash
codex plugin marketplace add .
```

Установите из локального marketplace:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
