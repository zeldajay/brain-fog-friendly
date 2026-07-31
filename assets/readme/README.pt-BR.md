<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly é um plugin do Claude Code para estilos de resposta curtos, gentis e passo a passo em dez idiomas.">
</p>

# Amigável para névoa mental

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | Português do Brasil

Um plugin do Claude Code marketplace para estilos de saída com baixa carga cognitiva.

Ele ajuda o Claude a responder com menos pressão, menos densidade e próximos passos mais claros.

É feito para pessoas com névoa mental, dificuldade de atenção, fadiga, sobrecarga, ou qualquer pessoa que prefira respostas calmas e passo a passo.

## O que você recebe

Dez estilos de saída localizados:

| Idioma | Estilo de saída |
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

## O que este estilo muda

Ele pede ao Claude para:

- colocar a conclusão e o próximo passo primeiro
- usar frases curtas
- usar parágrafos curtos
- reduzir a carga cognitiva
- avançar um pequeno passo por vez
- evitar pressão, julgamento e opções demais
- quando a pessoa travar, oferecer escolhas simples: continuar, simplificar ou pausar

## Instalação

Adicione este repositório como marketplace do Claude Code:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Depois instale o plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Uso

Abra a configuração do Claude Code:

```text
/config
```

Depois escolha um dos estilos de saída Brain Fog Friendly.

## Desenvolvimento local

Adicione este repositório como marketplace local:

```bash
claude plugin marketplace add .
```

Instale a partir do marketplace local:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Valide o plugin:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
