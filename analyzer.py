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

nltk.download('punkt')
nltk.download('stopwords')

def analyze_text(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('romanian')).union(set(stopwords.words('english')))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    freq_dist = FreqDist(filtered_words)
    top_words = freq_dist.most_common(10) 
    
    bi = list(ngrams(filtered_words, 2))
    tri = list(ngrams(filtered_words, 3))
    
    avg_len = sum(len(w) for w in filtered_words) / len(filtered_words) if filtered_words else 0
    unique_words = set(filtered_words)
    ttr = len(unique_words) / len(filtered_words) if filtered_words else 0
    
    return {
        "top_words": top_words,
        "bigrams": bi,
        "trigrams": tri,
        "avg_length": avg_len,
        "ttr": ttr,
        "unique_list": list(unique_words)
    }

def generate_wordcloud(text):
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('wordcloud.png')  

def export_results(results):
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'frequency'])
        for word, freq in results['top_words']:
            writer.writerow([word, freq])


def tdfidf_analysis(text):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]
    tfidf_dict = {feature_names[i]: tfidf_scores[i] for i in range(len(feature_names))}
    sorted_tfidf = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_tfidf

def find_concordance(text, target_word, window=5):
    words = word_tokenize(text.lower())
    contexts = []
    for i, word in enumerate(words):
        if word == target_word.lower():
            start = max(0, i - window)
            end = min(len(words), i + window + 1)
            contexts.append(" ".join(words[start:end]))
    return contexts
def main():

    if not os.path.exists('text.txt'):
        print("Fisierul text.txt nu a fost gasit.")
        return 
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    if (not text.strip()):
        print("The input text file is empty.")
        return
    else:
        print("The input text file is not empty.")

    results = analyze_text(text)
    generate_wordcloud(text)    
    export_results(results)
    tfidf_results = tdfidf_analysis(text)
    print(tfidf_results)

    with open('tfidf_results.json', 'w', encoding='utf-8') as f:
        json.dump(tfidf_results, f, ensure_ascii=False, indent=4)
    with open('tfidf_results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['word', 'tfidf_score'])
        for word, score in tfidf_results:
            writer.writerow([word, score])
    print (f"\nAnaliza text: text.txt ({len(text.split())} cuvinte) a fost finalizata. Rezultatele au fost salvate in results.json, results.csv, tfidf_results.json, tfidf_results.csv si wordcloud.png.")
    print("-" * 30)
    print("Top 10 cuvinte frecvente (fara stopwords):")
    for i, (word, freq) in enumerate(results['top_words'], 1):
        print(f"{i}. {word}: {freq} aparitii")
    print(f"\nDiversitate vocabular: ")
    print(f"Cuvinte unice: {len(results['unique_list'])}")
    print(f"Total cuvinte: {len(results['unique_list'])}")
    print(f"Type-Token Ratio (TTR): {results['ttr']:.3f}")
    print("\nCautare context pentru cuvantul 'exemplu':")
    contexts = find_concordance(text, "exemplu")
    for context in contexts:
        print(f"...{context}...")

if __name__ == "__main__":
    main()
