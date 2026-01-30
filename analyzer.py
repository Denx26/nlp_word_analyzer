import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import json
import csv

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
def main():
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    results = analyze_text(text)
    generate_wordcloud(text)
    export_results(results)

if __name__ == "__main__":
    main()