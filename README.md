Documentație Tehnică - Proiect NLP Analyzer 2026

Motivarea și scopul proiectului

Motivarea

Acest proiect a fost realizat ca parte a cursului de Tehnologii AI la Universitatea Politehnica Timișoara, specializarea Informatică. Analiza lingvistică automatizată reprezintă un pilon fundamental în dezvoltarea sistemelor moderne de Inteligență Artificială, fiind esențială pentru înțelegerea structurii limbajului uman.

Scopul

Scopul principal al proiectului a fost crearea unui instrument de analiză lingvistică eficient, capabil să proceseze texte brute și să extragă informații statistice precum frecvența cuvintelor, diversitatea vocabularului și structuri complexe de tip N-grams.

Detalii de implementare

Proiectul a fost implementat folosind limbajul Python, utilizând biblioteca NLTK (Natural Language Toolkit) pentru procesarea limbajului natural.

Structura codului

analyzer.py - conține logica principală de procesare, filtrare a stopword-urilor și calcularea statisticilor.

text.txt - fișierul de intrare care conține textul ce urmează a fi analizat.

Dockerfile - descrie mediul de rulare izolat, asigurând portabilitatea aplicației prin containerizare.

requirements.txt - listează toate bibliotecile externe necesare (nltk, scikit-learn, matplotlib, wordcloud).

Explicație Funcționalități

Analiza Textului (analyze_text):

Realizează tokenizarea textului și normalizarea acestuia prin transformarea în minuscule.

Filtrează cuvintele comune (stopwords) pentru limbile română și engleză.

Calcul Statistici:

Identifică topul celor mai frecvente cuvinte și calculează Type-Token Ratio (TTR) pentru a măsura diversitatea vocabularului.

Căutare în context (find_concordance):

Permite utilizatorului să identifice contextul (cuvintele vecine) pentru un anumit termen cheie.

Tehnologii Folosite

Limbaj de programare: Python.

Gestionarea mediului de rulare: Docker.

Controlul versiunilor: Git.

Editor/IDE: Visual Studio Code.

Mediul de Dezvoltare
Sistem de operare: Windows 11

Editor/IDE: Visual Studio Code

Containerizare: Docker

Exemple de Rulare
1. Analiza Top 10 Cuvinte

python analyzer.py text.txt --top 10

2. Verificarea Diversității Vocabularului

python analyzer.py text.txt --diversity

3. Căutare Context (Concordanță)

python analyzer.py text.txt --concordance "inteligența"

4. Rularea prin Docker

docker build -t nlp-analyzer .
docker run nlp-analyzer