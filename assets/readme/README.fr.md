<p align="center">
  <img src="./hero.fr.svg" width="100%" alt="Brain Fog Friendly est un plugin Claude Code et Codex pour des réponses courtes, douces et étape par étape en dix langues.">
</p>

# Adapté au brouillard cérébral

[English](../../README.md) | [中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Русский](./README.ru.md) | [العربية](./README.ar.md) | [한국어](./README.ko.md) | [Español](./README.es.md) | Français | [Deutsch](./README.de.md) | [Português do Brasil](./README.pt-BR.md)

Un plugin marketplace pour Claude Code et Codex, conçu pour des réponses à faible charge cognitive.

Il aide Claude et Codex à répondre avec moins de pression, moins de densité et des prochaines étapes plus claires.

Il est conçu pour les personnes ayant du brouillard cérébral, des difficultés d’attention, de la fatigue, une sensation de surcharge, ou pour toute personne qui préfère des réponses calmes et étape par étape.

## Ce que vous obtenez

Dix styles de réponse localisés. Ils sont disponibles comme styles de sortie Claude Code et via un skill de configuration Codex.

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

Il demande à Claude ou Codex de :

- placer la conclusion et la prochaine étape en premier
- utiliser des phrases courtes
- utiliser des paragraphes courts
- réduire la charge cognitive
- avancer une petite étape à la fois
- éviter la pression, le jugement et trop d’options
- quand la personne est bloquée, proposer des choix simples : continuer, simplifier ou faire une pause

## Installation

### Claude Code

Ajoutez ce dépôt comme marketplace Claude Code :

```bash
claude plugin marketplace add zeldajay/brain-fog-friendly
```

Puis installez le plugin :

```bash
claude plugin install brain-fog-friendly@brain-fog-friendly-marketplace
```

### Application de bureau ChatGPT

1. Ouvrez l’application de bureau ChatGPT.
2. Ouvrez **Extensions**.
3. Ouvrez le menu **Créer ▾** en haut à droite et sélectionnez **Ajouter une place de marché d’extensions**. Saisissez `zeldajay/brain-fog-friendly` dans **Origine**, puis sélectionnez **Ajouter la place de marché**.
4. Ouvrez l’onglet **Personnel** de la page Extensions. Ouvrez **Brain Fog Friendly** et sélectionnez le bouton plus pour l’installer.
5. Démarrez un nouveau chat afin de charger le skill inclus.

Consultez le [guide officiel des plugins ChatGPT et Codex](https://learn.chatgpt.com/docs/plugins) pour connaître les surfaces prises en charge et la gestion des plugins.

### Codex CLI

Ajoutez ce dépôt comme marketplace Codex :

```bash
codex plugin marketplace add zeldajay/brain-fog-friendly
```

Puis installez le plugin :

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## Utilisation

### Claude Code

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

### Codex CLI

Appelez explicitement le skill de configuration :

```text
$brain-fog-friendly
```

Codex affiche une liste numérotée contenant dix langues et une option de désactivation. Répondez avec le numéro, le nom de la langue ou son code.

### Application de bureau ChatGPT

Démarrez un nouveau chat, saisissez `@` et choisissez le skill **Brain Fog Friendly**. Répondez ensuite à la liste avec un numéro, un nom de langue ou un code de langue.

Le skill ajoute ou remplace un bloc `brain-fog-friendly` géré dans le fichier global `~/.codex/AGENTS.md`. La désactivation supprime uniquement ce bloc et conserve toutes les autres instructions globales.

Après avoir activé, changé ou désactivé le style, démarrez un nouveau fil Codex afin de recharger les instructions globales.

## Développement local

### Claude Code

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

### Codex

Ajoutez cette copie de travail comme marketplace local :

```bash
codex plugin marketplace add .
```

Installez depuis le marketplace local :

```bash
codex plugin add brain-fog-friendly@brain-fog-friendly-marketplace
```

## License

MIT
