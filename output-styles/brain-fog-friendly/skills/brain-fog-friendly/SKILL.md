---
name: brain-fog-friendly
description: 仅当用户显式调用 $brain-fog-friendly 时使用；不要自动调用。在聊天中让用户选择一种 Brain Fog Friendly 语言或禁用该全局响应风格，然后运行非交互脚本应用选择。
---

# Configure Brain Fog Friendly

1. 如果用户尚未指定语言或禁用，请在聊天中显示以下单选列表，然后停止并等待用户回复。不要代替用户选择。

```
   1. English (`en`)
   2. 简体中文 (`zh-cn`)
   3. 日本語 (`ja`)
   4. Русский (`ru`)
   5. العربية (`ar`)
   6. 한국어 (`ko`)
   7. Español (`es`)
   8. Français (`fr`)
   9. Deutsch (`de`)
   10. Português do Brasil (`pt-br`)
   11. 禁用
```

2. 将用户回复的序号、语言名称或代码映射为列表中的代码。不能明确映射时，再请用户选择；不要猜测。
3. 定位此 `SKILL.md` 所在的技能目录。
4. 选择语言时运行 `python3 <技能目录>/scripts/configure.py --language <代码>`；选择禁用时运行 `python3 <技能目录>/scripts/configure.py --disable`。不要请求或分配 PTY；如果沙箱限制写入全局配置，请为该命令请求文件写入授权。
5. 向用户转述脚本的成功消息或错误；不要自行编辑全局 `AGENTS.md`。

脚本负责保留全局 `AGENTS.md` 中的其他内容。选择语言时，它只新增或替换带有
`brain-fog-friendly` 标记的区块；选择禁用时，它只删除该区块。
