<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly는 열 가지 언어로 짧고 부드러운 단계별 출력 스타일을 제공하는 Claude Code 플러그인입니다.">
</p>

# 브레인 포그 친화적

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | 한국어 | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

낮은 인지 부담의 출력 스타일을 제공하는 Claude Code marketplace 플러그인입니다.

Claude가 부담을 줄이고, 밀도를 낮추고, 다음 단계를 더 명확하게 답하도록 돕습니다.

브레인 포그, 주의력 어려움, 피로, 압도감을 겪는 사람이나 차분한 단계별 답변을 선호하는 사람에게 적합합니다.

## 제공되는 것

열 가지 현지화된 출력 스타일:

| 언어 | 출력 스타일 |
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

## 이 스타일이 바꾸는 것

Claude에게 다음을 요청합니다:

- 결론과 다음 단계를 먼저 제시하기
- 짧은 문장 사용하기
- 짧은 문단 사용하기
- 인지 부담 줄이기
- 한 번에 하나의 작은 단계로 진행하기
- 압박, 판단, 너무 많은 선택지 피하기
- 사용자가 막혔을 때 간단한 선택지만 제시하기: 계속하기, 더 쉽게 설명하기, 잠시 멈추기

## 설치

이 저장소를 Claude Code marketplace로 추가합니다:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

그다음 플러그인을 설치합니다:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## 사용

Claude Code 설정을 엽니다:

```text
/config
```

그런 다음 Brain Fog Friendly 출력 스타일 중 하나를 선택합니다.

## 로컬 개발

이 저장소를 로컬 marketplace로 추가합니다:

```bash
claude plugin marketplace add .
```

로컬 marketplace에서 설치합니다:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

플러그인을 검증합니다:

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
