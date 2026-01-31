FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir nltk scikit-learn matplotlib wordcloud

RUN python -m nltk.downloader punkt punkt_tab stopwords

COPY . .

CMD ["python", "analyzer.py", "text.txt", "--top", "10"]