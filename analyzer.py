import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
import csv
import os 
import sys

# Descarcă resursele necesare pentru procesarea limbajului natural (NLP)
# punkt_tab este necesar pentru noile versiuni de NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def analyze_text(text):
    """
    Realizează procesarea textului: tokenizare, normalizare și filtrare.
    Calculează statistici de bază, N-grame și diversitatea vocabularului.
    """
    # Tokenizare și transformare în minuscule (Normalizare)
    words = word_tokenize(text.lower())
    
    # Filtrare Stopwords (RO/EN) - Cerință: Ignorare cuvinte comune
    stop_words = set(stopwords.words('romanian')).union(set(stopwords.words('english')))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calcul frecvență cuvinte
    freq_dist = FreqDist(filtered_words)
    
    # Analiză N-grams (Bigrame și Trigrame)
    bi = list(ngrams(filtered_words, 2))
    tri = list(ngrams(filtered_words, 3))
    
    # Calcul diversitate vocabular (Type-Token Ratio)
    unique_words = set(filtered_words)
    ttr = len(unique_words) / len(filtered_words) if filtered_words else 0
    
    # Lungime medie cuvinte
    avg_len = sum(len(w) for w in filtered_words) / len(filtered_words) if filtered_words else 0
    
    return {
        "filtered_words": filtered_words,
        "freq_dist": freq_dist,
        "bigrams": bi,
        "trigrams": tri,
        "avg_length": avg_len,
        "ttr": ttr,
        "unique_list": list(unique_words)
    }

def find_concordance(text, target_word, window=5):
    """
    Identifică contextul în care apare un cuvânt specific (Concordanță).
    """
    words = word_tokenize(text.lower())
    contexts = []
    for i, word in enumerate(words):
        if word == target_word.lower():
            start = max(0, i - window)
            end = min(len(words), i + window + 1)
            contexts.append(" ".join(words[start:end]))
    return contexts

def export_data(results, tfidf_results):
    """
    Exportă rezultatele analizei în formate structurate (JSON/CSV).
    """
    # Export Frecvență și Statistici
    with open('results.json', 'w', encoding='utf-8') as f:
        # Salvăm un dicționar serializabil
        json_data = {
            "top_words": results['freq_dist'].most_common(20),
            "ttr": results['ttr'],
            "avg_length": results['avg_length']
        }
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    # Export TF-IDF Scores
    with open('tfidf_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Word', 'TF-IDF Score'])
        writer.writerows(tfidf_results)

def main():
    # Validare argumente linie de comandă
    if len(sys.argv) < 2:
        print("Utilizare: python analyzer.py <nume_fisier.txt> [--top N] [--diversity] [--concordance CUVANT]")
        return

    file_path = sys.argv[1]
    
    # Validare existență fișier
    if not os.path.exists(file_path):
        print(f"Eroare: Fișierul '{file_path}' nu a fost găsit.")
        return 

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    if not text.strip():
        print("Eroare: Fișierul este gol.")
        return

    # Executarea analizei NLP
    results = analyze_text(text)
    
    # Generare Word Cloud (Vizualizare date textuale)
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    wc.to_file('wordcloud.png')

    # Analiză TF-IDF (Opțional conform cerințelor)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    tfidf_results = sorted(zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0]), key=lambda x: x[1], reverse=True)

    # Export date
    export_data(results, tfidf_results)

    # Logica de afișare bazată pe argumente (Input utilizator)
    args = sys.argv[2:]
    total_words = len(text.split())

    # Flag pentru Top N rezultate
    if "--top" in args:
        idx = args.index("--top")
        try:
            n = int(args[idx + 1]) if idx + 1 < len(args) else 10
        except ValueError:
            n = 10
        print(f"\nTop {n} cuvinte frecvente:")
        for i, (word, freq) in enumerate(results['freq_dist'].most_common(n), 1):
            print(f"  {i:>2}. {word:<15} - {freq:>2} apariții")

    # Flag pentru Diversitate vocabular
    if "--diversity" in args:
        print(f"\nStatistici diversitate:")
        print(f"  Total cuvinte: {total_words}")
        print(f"  Cuvinte unice: {len(results['unique_list'])}")
        print(f"  Type-Token Ratio (TTR): {results['ttr']:.3f}")

    # Flag pentru Concordanță
    if "--concordance" in args:
        idx = args.index("--concordance")
        target = args[idx + 1] if idx + 1 < len(args) else "text"
        print(f"\nContext pentru cuvântul '{target}':")
        contexts = find_concordance(text, target)
        for i, ctx in enumerate(contexts[:3], 1):
            print(f"  {i}. ...{ctx}...")

    # Mesaj de finalizare implicit
    if not args:
        print(f"\nAnaliza completă pentru {file_path} a fost realizată cu succes.")
        print("Fișiere generate: wordcloud.png, results.json, tfidf_results.csv")

if __name__ == "__main__":
    main()