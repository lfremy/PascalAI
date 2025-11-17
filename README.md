# PascalAI

Agent conversationnel incarnant le philosophe Blaise Pascal (1623-1662).

##  Prérequis

- Python 3.8 ou plus
- Une clé API Anthropic ([obtenir une clé](https://console.anthropic.com/settings/keys))

## Installation rapide

### 1. Cloner le projet
```bash
git clone https://github.com/lfremy/PascalAI.git
cd PascalAI
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configurer la clé API

Créez un fichier `.env` à la racine du projet :
```bash
ANTHROPIC_API_KEY=votre_clé_api_ici
```

**Important :** Obtenez votre clé sur [console.anthropic.com](https://console.anthropic.com/settings/keys)

### 5. Lancer l'application
```bash
streamlit run app.py
```

L'application s'ouvre automatiquement dans votre navigateur à `http://localhost:8501`

##  Utilisation

Tapez votre question dans la barre de chat et dialoguez avec Pascal !

##  Documentation

- [Méthodologie complète](Methodology.md)
- [Prompt Pascal](prompts/pascal_prompts.py)

## Contribution

Retours et suggestions bienvenus via les issues GitHub.

## Licence

MIT
