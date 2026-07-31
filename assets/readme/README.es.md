<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly es un plugin de Claude Code para estilos de respuesta breves, amables y paso a paso en diez idiomas.">
</p>

# Brain Fog Friendly

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | Español | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

Un plugin de Claude Code marketplace para estilos de salida con baja carga cognitiva.

Ayuda a Claude a responder con menos presión, menos densidad y pasos siguientes más claros.

Está pensado para personas con niebla mental, dificultad de atención, fatiga, saturación, o para cualquiera que prefiera respuestas tranquilas y paso a paso.

## Qué obtienes

Diez estilos de salida localizados:

| Idioma | Estilo de salida |
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

## Qué cambia este estilo

Le pide a Claude que:

- ponga primero la conclusión y el siguiente paso
- use frases cortas
- use párrafos cortos
- reduzca la carga cognitiva
- avance un pequeño paso a la vez
- evite la presión, el juicio y demasiadas opciones
- cuando la persona se bloquee, ofrezca opciones simples: continuar, simplificar o pausar

## Instalación

Añade este repositorio como marketplace de Claude Code:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Luego instala el plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Uso

Abre la configuración de Claude Code:

```text
/config
```

Luego elige uno de los estilos de salida Brain Fog Friendly.

## Desarrollo local

Añade este repositorio como marketplace local:

```bash
claude plugin marketplace add .
```

Instala desde el marketplace local:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Valida el plugin:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
