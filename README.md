# Wikipedia-Based Question Answering System

This Python script extracts textual content from a Wikipedia page, processes it, and answers user queries using TF-IDF vectorization and cosine similarity.

## Features
- Fetches text content from a specified Wikipedia page.
- Cleans and preprocesses the extracted text.
- Uses Natural Language Processing (NLP) techniques to tokenize text and remove stopwords.
- Answers user queries based on similarity to extracted sentences.

## Requirements
Ensure you have the following Python libraries installed:

```bash
pip install beautifulsoup4 nltk scikit-learn lxml
```

## How It Works
1. The script retrieves the Wikipedia page content of the iPhone 14 or replace it with other link.
2. It extracts paragraph text and cleans it by removing references and extra spaces.
3. Sentences are tokenized for further processing.
4. A user-provided question is tokenized, and stopwords are removed.
5. The question is compared to the extracted sentences using TF-IDF and cosine similarity.
6. The most relevant sentence is returned as the answer.

## Usage
```python
answer("What is the release date of iPhone 14?")
```
If a relevant answer is found, the function returns it. Otherwise, it returns:
```plaintext
"Sorry, don't know that"
```

## Dependencies
- `urllib`: Fetches the Wikipedia page.
- `beautifulsoup4`: Parses HTML content.
- `nltk`: Provides NLP tools for tokenization and stopword removal.
- `scikit-learn`: Enables TF-IDF vectorization and cosine similarity computation.

## Notes
- The script is hardcoded to fetch information from the iPhone 14 Wikipedia page.
- The accuracy of responses depends on the structure of the extracted text.


