# Aplicație de analiză a frecvenței cuvintelor
# Veți crea un instrument de analiză lingvistică care procesează texte și extrage informații
# statistice despre utilizarea cuvintelor, ideal pentru NLP de bază.
# Ce veți învăța:
# • Procesarea limbajului natural (NLP basics)
# • Tokenizare și normalizare text
# • Stopwords și filtrare
# 24
# • N-grams (bigrame, trigrame)
# • TF-IDF scoring (opțional)
# • Vizualizare date textuale
# Funcționalități cerute:
# • Numărare frecvență cuvinte cu top N rezultate
# • Ignorare stopwords (ro/en) - cuvinte comune "și", "de", "pentru"
# • Analiză bigrame și trigrame (secvențe de 2-3 cuvinte)
# • Lungime medie cuvinte și diversitate vocabular
# • Identificare cuvinte unice/rare
# • Generare word cloud (text)
# • Export rezultate în JSON/CSV
# • Comparație între multiple documente
# • Căutare context (concordanță pentru un cuvânt)


import nt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import ngrams
from sklearn.linear_model import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import csv


nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('tokenizers/punkt')



def analyze_text(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('romanian'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist  = FreqDist(filtered_words)
    top_words = freq_dist.most_common(10)
    bigrams = list(ngrams(filtered_words, 2))
    trigrams = list(ngrams(filtered_words, 3))
    word_length = sum(len(word) for word in filtered_words) / len(filtered_words)
    unique_words = set(filtered_words)
    return top_words, bigrams, trigrams, word_length, len(unique_words), unique_words   

if __name__ == "__main__":
    sample_text = """Acesta este un text de exemplu pentru a demonstra analiza frecventei cuvintelor.
    Scopul este de a extrage informatii statistice despre utilizarea cuvintelor.
    Acest text contine cuvinte comune si unice."""
    results = analyze_text(sample_text)
    print("Top Words:", results[0])
    print("Bigrams:", results[1])   
    print("Trigrams:", results[2])
    print("Average Word Length:", results[3])
    print("Unique Words:", results[4])
    print("Unique/Rare Words:", results[5])


def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    generate_wordcloud(sample_text)

def export_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])
        for word, freq in data:
            writer.writerow([word, freq])
def export_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    export_to_csv(results[0], 'word_frequency.csv')
    export_to_json(dict(results[0]), 'word_frequency.json')
    export_to_csv(results[1], 'bigrams.csv')
    export_to_csv(results[2], 'trigrams.csv')
    export_to_json(dict(results[1]), 'bigrams.json')
    export_to_json(dict(results[2]), 'trigrams.json')
    export_to_csv(results[4], 'unique_words.csv')
    export_to_json(dict(results[4]), 'unique_words.json')
    export_to_csv(results[5], 'rare_words.csv')
    export_to_json(dict(results[5]), 'rare_words.json')

def search_context(text, target_word, window=5):
    words = word_tokenize(text.lower())
    contexts = []
    for i, word in enumerate(words):
        if word == target_word:
            start = max(i - window, 0)
            end = min(i + window + 1, len(words))
            contexts.append(' '.join(words[start:end]))
    return contexts
    contexts = search_context(sample_text, 'cuvintelor')
    print("Contexts for 'cuvintelor':", contexts)


def compare_documents(texts):
    vectorizer = TfidfVectorizer(stop_words=stopwords.words('romanian'))
    tfidf_matrix = vectorizer.fit_transform(texts)
    return tfidf_matrix.toarray()
    docs = [sample_text, "Acesta este un alt text pentru comparatie."]
    comparison = compare_documents(docs)
    print("TF-IDF Comparison:", comparison)


def main():
    sample_text
    results = analyze_text(sample_text)
    print("Top Words:", results[0])
    print("Bigrams:", results[1])
    print("Trigrams:", results[2])
    print("Average Word Length:", results[3])
    print("Unique Words:", results[4])
    print("Unique/Rare Words:", results[5])
    generate_wordcloud(sample_text)
    export_to_csv(results[0], 'word_frequency.csv')
    export_to_json(dict(results[0]), 'word_frequency.json')
    export_to_csv(results[1], 'bigrams.csv')
    export_to_csv(results[2], 'trigrams.csv')
    export_to_json(dict(results[1]), 'bigrams.json')
    export_to_json(dict(results[2]), 'trigrams.json')
    export_to_csv(results[4], 'unique_words.csv')
    export_to_json(dict(results[4]), 'unique_words.json')
    export_to_csv(results[5], 'rare_words.csv')
    export_to_json(dict(results[5]), 'rare_words.json')
    contexts = search_context(sample_text, 'cuvintelor')
    print("Contexts for 'cuvintelor':", contexts)
    docs = [sample_text, "Acesta este un alt text pentru comparatie."]
    comparison = compare_documents(docs)
    print("TF-IDF Comparison:", comparison)
if __name__ == "__main__":
    main()

