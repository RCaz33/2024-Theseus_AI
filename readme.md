Projet Theseus AI


Objectifs:
- prendre en main de nouvelles librairies rapidement, 
- créer un API avec fastapi (prend en entrée une question et va chercher la réponse dans un texte)

Exigences :
- nommer tes fonctions, variables, et bien documenter l’ensemble
- Prends soin de ton git, je regarderai tes commits et leur organisation
- Organise ton code en programmation object, si tu y arrives. 
- Ton main.py doit être clair, les fonctions doivent être dans tes fichiers à part et facilement lisibles.
- Pense à ajouter ton fichier de ressources pour PIP
- publier sur ton github, en publique, et de m’en fournir le lien.


Méthodologie :
- utiliser un mix de base de données vectorielle, ainsi qu’un LLM pour trouver la réponse à ta question dans le texte**.
- découper le texte en chunks, c’est-à-dire en bouts de textes. Pour ces chunks, j’aimerais que tu les découpes en éléments de 500 tokens maximum, en coupant à la fin d’une phrase. (Tu devras donc chercher le dernier point avant ces 500 tokens)
- Pour tokeniser, tu dois utiliser la librairie tiktoken***.
- Ensuite comme dans la vidéo tutorielle, tu devrais faire une recherche vectorielle, puis passer sur le n = 3 chunks les plus proches avec ton LLM**.
- Utilise l’api de openAI (chatgpt 3.5), si tu n’as pas d’accès, essai d’en créer, et n’hésite pas à me demander des clefs si cela bloque trop.


