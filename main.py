from collections import Counter
import requests

def get_text(url):
    response = requests.get(url)
    return response.text

def count_word_frequencies(text, words_to_count):
    counter = Counter(text.split())
    return {word: counter.get(word, 0) for word in words_to_count}

def main():
    words_file = "words.txt"
    url = "https://eng.mipt.ru/why-mipt/"

    with open(words_file, 'r') as file:
        words_to_count = [line.strip() for line in file if line.strip()]

    text = get_text(url)
    frequencies = count_word_frequencies(text, words_to_count)

    print(frequencies)

if __name__ == "__main__":
    main()