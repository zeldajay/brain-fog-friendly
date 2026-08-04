<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly는 열 가지 언어로 짧고 부드러운 단계별 응답을 제공하는 Claude Code 및 Codex 플러그인입니다.">
</p>

# 브레인 포그 친화적

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | 한국어 | [Español](./README.es.md) | [Français](./README.fr.md) | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

낮은 인지 부담의 응답을 제공하는 Claude Code 및 Codex marketplace 플러그인입니다.

Claude와 Codex가 부담을 줄이고, 밀도를 낮추고, 다음 단계를 더 명확하게 답하도록 돕습니다.

브레인 포그, 주의력 어려움, 피로, 압도감을 겪는 사람이나 차분한 단계별 답변을 선호하는 사람에게 적합합니다.

## 제공되는 것

열 가지 현지화된 응답 스타일입니다. Claude Code 출력 스타일 또는 Codex 설정 스킬로 사용할 수 있습니다.

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

Claude 또는 Codex에 다음을 요청합니다:

- 결론과 다음 단계를 먼저 제시하기
- 짧은 문장 사용하기
- 짧은 문단 사용하기
- 인지 부담 줄이기
- 한 번에 하나의 작은 단계로 진행하기
- 압박, 판단, 너무 많은 선택지 피하기
- 사용자가 막혔을 때 간단한 선택지만 제시하기: 계속하기, 더 쉽게 설명하기, 잠시 멈추기

## 설치

### Claude Code

이 저장소를 Claude Code marketplace로 추가합니다:

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

그다음 플러그인을 설치합니다:

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### ChatGPT 데스크톱 앱

1. ChatGPT 데스크톱 앱을 엽니다.
2. **플러그인**을 엽니다.
3. 오른쪽 위의 **만들기 ▾** 메뉴를 열고 **플러그인 마켓플레이스 추가**를 선택합니다. **소스**에 `zeldajay/brain-fog-friendly`를 입력한 다음 **마켓플레이스 추가**를 선택합니다.
4. 플러그인 페이지에서 **개인** 탭을 엽니다. **Brain Fog Friendly**를 열고 더하기 버튼을 선택해 설치합니다.
5. 새 채팅을 시작해 포함된 스킬을 불러옵니다.

지원되는 화면과 플러그인 관리 방법은 공식 [ChatGPT 및 Codex 플러그인 가이드](https://learn.chatgpt.com/docs/plugins)를 참조하세요.

### Codex CLI

이 저장소를 Codex marketplace로 추가합니다:

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

그다음 플러그인을 설치합니다:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## 사용

### Claude Code

Claude Code 설정을 엽니다:

```text
/config
```

그런 다음:

1. `Output style`(출력 스타일) 설정을 찾습니다.
2. Enter를 눌러 출력 스타일 목록을 엽니다.
3. 화살표 키로 Brain Fog Friendly 스타일 중 하나(예: `Brain Fog Friendly` 또는 `브레인 포그 친화적`)로 이동합니다.
4. Enter를 눌러 선택합니다.
5. Esc를 눌러 설정을 닫습니다. 이제 스타일이 적용되었습니다.

### Codex CLI

설정 스킬을 명시적으로 호출합니다:

```text
$brain-fog-friendly
```

Codex가 열 가지 언어와 비활성화 옵션이 포함된 번호 목록을 표시합니다. 번호, 언어 이름 또는 언어 코드로 답하세요.

### ChatGPT 데스크톱 앱

새 채팅을 시작하고 `@`를 입력한 다음 **Brain Fog Friendly** 스킬을 선택합니다. 이후 번호, 언어 이름 또는 언어 코드로 언어 목록에 답하세요.

이 스킬은 전역 `~/.codex/AGENTS.md`에 관리되는 `brain-fog-friendly` 블록을 추가하거나 교체합니다. 비활성화를 선택하면 이 블록만 삭제하고 다른 전역 지침은 그대로 유지합니다.

활성화, 전환 또는 비활성화 후에는 Codex가 전역 지침을 다시 불러오도록 새 Codex 스레드를 시작하세요.

## 로컬 개발

### Claude Code

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

### Codex

현재 체크아웃을 로컬 marketplace로 추가합니다:

```bash
codex plugin marketplace add .
```

로컬 marketplace에서 설치합니다:

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
