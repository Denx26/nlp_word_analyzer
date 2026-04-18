# NLP Word Analyzer 

A Python-based Natural Language Processing tool designed to process raw text and extract meaningful statistical insights. This application implements fundamental NLP techniques including tokenization, stopword filtering, and vocabulary diversity analysis.

## 🚀 Purpose
The primary goal of this project is to provide a lightweight, containerized tool for text analysis. It is built to handle both English and Romanian text, making it versatile for multilingual datasets.

## 🛠️ Implementation Details
The project is built with **Python**, utilizing industry-standard libraries for linguistic computation and data visualization.

### Project Structure
*   `analyzer.py` – Core logic for text processing and statistical calculations.
*   `text.txt` – Input file containing the source text for analysis.
*   `Dockerfile` – Configuration for containerizing the application.
*   `requirements.txt` – List of dependencies (`nltk`, `scikit-learn`, `matplotlib`, `wordcloud`).

## ✨ Key Features

### 1. Text Analysis & Normalization
The `analyze_text` function handles the heavy lifting:
*   **Tokenization:** Breaks down raw text into individual words.
*   **Normalization:** Converts text to lowercase for consistency.
*   **Stopword Filtering:** Removes common "noise" words in both Romanian and English to focus on meaningful content.

### 2. Statistics & Diversity Metrics
*   **Frequency Analysis:** Identifies and ranks the most used words in the document.
*   **Type-Token Ratio (TTR):** Calculates the ratio of unique words to the total word count to measure vocabulary richness.

### 3. Concordance Identification
The `find_concordance` feature allows users to locate specific words within their immediate context, helping to understand how terms are used throughout the text.

## 📊 Visual Examples

### Top 10 Most Frequent Words
![Top 10 Words](1.png)

### Vocabulary Diversity Stats
![Diversity Statistics](2.png)

## 📦 Installation & Usage

To run this project locally using Docker, follow these steps:

### Build the Docker image:
```bash
docker build -t nlp-analyzer .
docker run nlp-analyzer
