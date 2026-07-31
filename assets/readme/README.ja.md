<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly は、短く、穏やかで、段階的な出力スタイルを十言語で提供する Claude Code プラグインです。">
</p>

# ブレインフォグにやさしい

[English](../../README.md) | [中文](./README.zh-CN.md) | 日本語 | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

低い認知負荷の出力スタイルを提供する Claude Code marketplace プラグインです。

Claude が、圧力を減らし、密度を下げ、次の一歩をより明確にして答えるようにします。

ブレインフォグ、注意の難しさ、疲労、圧倒感がある人、または穏やかで段階的な返答を好む人向けです。

## 得られるもの

十種類のローカライズ済み出力スタイル：

| 言語 | 出力スタイル |
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

## このスタイルが変えること

Claude に次のことを求めます：

- 結論と次の一歩を先に置く
- 短い文を使う
- 短い段落を使う
- 認知負荷を下げる
- 一度に一つの小さなステップで進む
- 圧力、判断、選択肢の多さを避ける
- ユーザーが詰まったときは、続ける、簡単に説明する、一時停止する、のような簡単な選択肢を出す

## インストール

このリポジトリを Claude Code marketplace として追加します：

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

次にプラグインをインストールします：

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## 使い方

Claude Code の設定を開きます：

```text
/config
```

その後、Brain Fog Friendly の出力スタイルを一つ選びます。

## ローカル開発

このリポジトリをローカル marketplace として追加します：

```bash
claude plugin marketplace add .
```

ローカル marketplace からインストールします：

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

プラグインを検証します：

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
