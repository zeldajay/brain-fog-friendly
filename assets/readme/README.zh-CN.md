<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly 是一个 Claude Code 和 Codex 插件，提供十种语言的简短、温和、分步骤回复。">
</p>

# 脑雾友好

[English](../../README.md) | 中文 | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

一个面向 Claude Code 和 Codex 的 marketplace 插件，提供低认知负荷回复。

它帮助 Claude 和 Codex 用更少压力、更低密度、更清晰的下一步来回答。

适合有脑雾、注意力困难、疲劳、信息过载的人，也适合任何偏好平静、分步骤回复的人。

## 你会得到什么

十种本地化回复风格。它们可作为 Claude Code 输出风格使用，也可通过 Codex 配置技能使用。

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

它会要求 Claude 或 Codex：

- 先给结论和下一步
- 使用短句
- 使用短段落
- 降低认知负荷
- 一次只推进一个小步骤
- 避免压力、评判和太多选项
- 当用户卡住时，只给简单选择：继续、简化解释或暂停

## 安装

### Claude Code

添加这个仓库作为 Claude Code marketplace：

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

然后安装插件：

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### ChatGPT 桌面客户端

1. 打开 ChatGPT 桌面客户端。
2. 打开 **插件**。
3. 打开右上角的 **创建 ▾** 菜单，选择 **添加插件市场**。在 **来源** 中输入 `zeldajay/brain-fog-friendly`，然后点击 **添加市场**。
4. 在插件页面打开 **个人** 选项卡。打开 **Brain Fog Friendly**，点击加号安装。
5. 新建聊天，让客户端加载插件中的技能。

有关支持的平台和插件管理方式，请参阅官方 [ChatGPT 和 Codex 插件指南](https://learn.chatgpt.com/docs/plugins)。

### Codex CLI

添加这个仓库作为 Codex marketplace：

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

然后安装插件：

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## 使用

### Claude Code

打开 Claude Code 配置：

```text
/config
```

然后：

1. 找到 `Output style`（输出风格）设置。
2. 按 Enter 打开输出风格列表。
3. 用方向键移动到某个 Brain Fog Friendly 风格（例如 `Brain Fog Friendly` 或 `脑雾友好`）。
4. 按 Enter 选中它。
5. 按 Esc 离开配置。风格现在已生效。

### Codex CLI

显式调用配置技能：

```text
$brain-fog-friendly
```

Codex 会显示包含十种语言和禁用选项的编号列表。回复序号、语言名称或语言代码。

### ChatGPT 桌面客户端

新建聊天，输入 `@`，然后选择 **Brain Fog Friendly** 技能。接着用序号、语言名称或语言代码回复语言列表。

该技能会在全局 `~/.codex/AGENTS.md` 中添加或替换一个受管理的 `brain-fog-friendly` 区块。选择禁用只会删除该区块，并保留其他全局指令。

启用、切换或禁用后，请新建 Codex 会话，让 Codex 重新加载全局指令。

## 本地开发

### Claude Code

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

### Codex

添加当前项目作为本地 marketplace：

```bash
codex plugin marketplace add .
```

从本地 marketplace 安装：

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
