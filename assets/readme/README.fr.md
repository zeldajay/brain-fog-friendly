<p align="center">
  <img src="./hero.svg" width="100%" alt="Brain Fog Friendly est un plugin Claude Code pour des styles de réponse courts, doux et étape par étape en dix langues.">
</p>

# Adapté au brouillard cérébral

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | Français | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

Un plugin Claude Code marketplace pour des styles de sortie à faible charge cognitive.

Il aide Claude à répondre avec moins de pression, moins de densité et des prochaines étapes plus claires.

Il est conçu pour les personnes ayant du brouillard cérébral, des difficultés d’attention, de la fatigue, une sensation de surcharge, ou pour toute personne qui préfère des réponses calmes et étape par étape.

## Ce que vous obtenez

Dix styles de sortie localisés :

| Langue | Style de sortie |
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

## Ce que ce style change

Il demande à Claude de :

- placer la conclusion et la prochaine étape en premier
- utiliser des phrases courtes
- utiliser des paragraphes courts
- réduire la charge cognitive
- avancer une petite étape à la fois
- éviter la pression, le jugement et trop d’options
- quand la personne est bloquée, proposer des choix simples : continuer, simplifier ou faire une pause

## Installation

Ajoutez ce dépôt comme marketplace Claude Code :

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Puis installez le plugin :

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

## Utilisation

Ouvrez la configuration de Claude Code :

```text
/config
```

Puis :

1. Trouvez le réglage `Output style` (style de sortie).
2. Appuyez sur Entrée pour ouvrir la liste des styles de sortie.
3. Utilisez les flèches pour aller sur l’un des styles Brain Fog Friendly (par exemple `Brain Fog Friendly` ou `Adapté au brouillard cérébral`).
4. Appuyez sur Entrée pour le sélectionner.
5. Appuyez sur Échap pour quitter la configuration. Le style est maintenant actif.

## Développement local

Ajoutez ce dépôt comme marketplace local :

```bash
claude plugin marketplace add .
```

Installez depuis le marketplace local :

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

Validez le plugin :

```bash
claude plugin validate .
claude plugin validate ./output-styles/brain-fog-friendly
```

## License

MIT
