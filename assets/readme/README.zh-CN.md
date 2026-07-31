<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly 是一个 Claude Code 插件，提供十种语言的简短、温和、分步骤输出风格。">
</p>

# 脑雾友好

[English](../../README.md) | 中文 | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

一个 Claude Code marketplace 插件，提供低认知负荷的输出风格。

它帮助 Claude 用更少压力、更低密度、更清晰的下一步来回答。

适合有脑雾、注意力困难、疲劳、信息过载的人，也适合任何偏好平静、分步骤回复的人。

## 你会得到什么

十种本地化输出风格：

| 语言 | 输出风格 |
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

## 这个风格会改变什么

它会要求 Claude：

- 先给结论和下一步
- 使用短句
- 使用短段落
- 降低认知负荷
- 一次只推进一个小步骤
- 避免压力、评判和太多选项
- 当用户卡住时，只给简单选择：继续、简化解释或暂停

## 安装

添加这个仓库作为 Claude Code marketplace：

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

然后安装插件：

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## 使用

打开 Claude Code 配置：

```text
/config
```

然后选择一个 Brain Fog Friendly 输出风格。

## 本地开发

添加这个仓库作为本地 marketplace：

```bash
claude plugin marketplace add .
```

从本地 marketplace 安装：

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

验证插件：

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
