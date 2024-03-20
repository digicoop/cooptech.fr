# cooptech.fr

Le site cooptech.fr est un site statique généré avec [Jekyll](https://jekyllrb.com/).

Le site est un effort commun des membres de la Cooptech. N'hésitez pas à soumettre des pull requests pour améliorer/corriger le site.

## Poster une nouvelle action

Les articles dans la section actions du site sont des ["posts"](https://jekyllrb.com/docs/posts/) localisés dans le dosier *_posts*. Ils sont formattés avec markdown.

Pour ajouter un nouvel article:

1. Créer un nouveau fichier yaml dans le dossier _posts avec le format suivant: `YYYY-MM-DD-slug.md` où *slug* et le titre de l'article ["slugifier](https://wpmarmite.com/glossaire/slug/)
2. Ajouter un frontmatter qui doit au minimum préciser le titre et le layout (qui sera toujours `post`)
3. Ajouter votre contenu

Exemple `2024-01-01-annonce-article-a-venir.md`:

```
---
layout: post
title: Annonce action à venir
---
Le contenu de mon article en markdown
```

Vous pouvez optionnellement définir la clé `thumbnail` dans le frontmatter avec le chemin vers une image.

Pour les meetups, il existe quelques metadata supplémentaires afin de pouvoir les identifier facilement:

```yaml
category: Meetups
thumbnail: /assets/img/post-meetup-thumb.jpg # vignette générique pour les meetups
meetup_date: "2024-01-01"
```

## Créer ou éditer sa fiche de membre

Les fiches de membres sont localisées dans le dossier *_members*. Chaque membre est représenté par un fichier yaml.

Le fichier *_members/TEMPLATE* liste les champs possible dans le frontmatter.

## Faire tourner le site localement

Depuis un terminal, an ayant docker installé sur la machine, il suffit de lancer la commande suivante:

```
$ ./jekyll.sh serve --watch
```

Puis ouvrir <http://localhost:4000>

Alternativement, il faudra [installer jekyll](https://jekyllrb.com/docs/installation/) puis lancer jekyll dans le dossier racine.
