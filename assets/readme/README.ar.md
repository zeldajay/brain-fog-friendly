<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly هو إضافة Claude Code لأساليب إخراج قصيرة ولطيفة وخطوة بخطوة بعشر لغات.">
</p>

# صديق لضباب الدماغ

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | العربية | [한국어](./README.ko.md) | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

إضافة في Claude Code marketplace لأساليب إخراج منخفضة العبء المعرفي.

تساعد Claude على الإجابة بضغط أقل، وكثافة أقل، وخطوات تالية أوضح.

مناسبة للأشخاص الذين يعانون من ضباب الدماغ، أو صعوبة الانتباه، أو التعب، أو الإرهاق، أو لأي شخص يفضّل ردودًا هادئة وخطوة بخطوة.

## ما الذي تحصل عليه

عشرة أساليب إخراج مترجمة:

| اللغة | أسلوب الإخراج |
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

## ما الذي يغيّره هذا الأسلوب

يطلب من Claude أن:

- يضع الخلاصة والخطوة التالية أولًا
- يستخدم جملًا قصيرة
- يستخدم فقرات قصيرة
- يقلل العبء المعرفي
- يتحرك خطوة صغيرة واحدة في كل مرة
- يتجنب الضغط، والحكم، وكثرة الخيارات
- يقدم خيارات بسيطة عندما يعلق المستخدم: المتابعة، تبسيط الشرح، أو التوقف مؤقتًا

## التثبيت

أضف هذا المستودع كـ Claude Code marketplace:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

ثم ثبّت الإضافة:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## الاستخدام

افتح إعدادات Claude Code:

```text
/config
```

ثم اختر أحد أساليب Brain Fog Friendly.

## التطوير المحلي

أضف هذا المستودع كـ marketplace محلي:

```bash
claude plugin marketplace add .
```

ثبّت من marketplace المحلي:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

تحقق من الإضافة:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
