<p align="center">
  <img src="./hero.pt-BR.svg" width="100%" alt="Brain Fog Friendly é um plugin do Claude Code e Codex para respostas curtas, gentis e passo a passo em dez idiomas.">
</p>

# Amigável para névoa mental

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | Português do Brasil

Um plugin de marketplace para Claude Code e Codex com respostas de baixa carga cognitiva.

Ele ajuda o Claude e o Codex a responder com menos pressão, menos densidade e próximos passos mais claros.

É feito para pessoas com névoa mental, dificuldade de atenção, fadiga, sobrecarga, ou qualquer pessoa que prefira respostas calmas e passo a passo.

## O que você recebe

Dez estilos de resposta localizados. Eles estão disponíveis como estilos de saída do Claude Code e por meio de uma skill de configuração do Codex.

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

Ele pede ao Claude ou Codex para:

- colocar a conclusão e o próximo passo primeiro
- usar frases curtas
- usar parágrafos curtos
- reduzir a carga cognitiva
- avançar um pequeno passo por vez
- evitar pressão, julgamento e opções demais
- quando a pessoa travar, oferecer escolhas simples: continuar, simplificar ou pausar

## Instalação

### Claude Code

Adicione este repositório como marketplace do Claude Code:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Depois instale o plugin:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### Aplicativo para desktop do ChatGPT

1. Abra o aplicativo para desktop do ChatGPT.
2. Abra **Extensões**.
3. Abra o menu **Criar ▾** no canto superior direito e selecione **Adicionar mercado de extensões**. Digite `zeldajay/brain-fog-friendly` em **Origem** e selecione **Adicionar mercado**.
4. Abra a aba **Pessoal** na página Extensões. Abra **Brain Fog Friendly** e selecione o botão de mais para instalar.
5. Inicie um novo chat para carregar a skill incluída.

Consulte o [guia oficial de plugins do ChatGPT e Codex](https://learn.chatgpt.com/docs/plugins) para conhecer as superfícies compatíveis e o gerenciamento de plugins.

### Codex CLI

Adicione este repositório como marketplace do Codex:

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

Depois instale o plugin:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## Uso

### Claude Code

Abra a configuração do Claude Code:

```text
/config
```

Depois:

1. Encontre a configuração `Output style` (estilo de saída).
2. Pressione Enter para abrir a lista de estilos de saída.
3. Use as setas para ir até um dos estilos Brain Fog Friendly (por exemplo `Brain Fog Friendly` ou `Amigável para névoa mental`).
4. Pressione Enter para selecioná-lo.
5. Pressione Esc para sair da configuração. O estilo agora está ativo.

### Codex CLI

Invoque explicitamente a skill de configuração:

```text
$brain-fog-friendly
```

O Codex exibe uma lista numerada com dez idiomas e uma opção para desativar. Responda com o número, o nome do idioma ou o código do idioma.

### Aplicativo para desktop do ChatGPT

Inicie um novo chat, digite `@` e escolha a skill **Brain Fog Friendly**. Depois responda à lista com um número, nome de idioma ou código de idioma.

A skill adiciona ou substitui um bloco gerenciado `brain-fog-friendly` no arquivo global `~/.codex/AGENTS.md`. A opção de desativar remove apenas esse bloco e preserva todas as outras instruções globais.

Depois de ativar, trocar ou desativar o estilo, inicie uma nova conversa do Codex para recarregar as instruções globais.

## Desenvolvimento local

### Claude Code

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

### Codex

Adicione este checkout como marketplace local:

```bash
codex plugin marketplace add .
```

Instale a partir do marketplace local:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
