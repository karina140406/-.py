import string
text = input("Введите текст: ")
words = [w.strip(string.punctuation) for w in text.split() if w.strip(string.punctuation)]
average = sum(len(w) for w in words) / len(words) if words else 0
print(f"Средняя длина слова в тексте: {average:.0f}.")