import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(r'[\t\r\n\v\f]', ' ', text)

    text = re.sub(r' +', ' ', text).strip()

    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("   двойные    пробелы   "))

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!")) 
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]

freq = count_freq(["a", "b", "a", "c", "b", "a"])
print(freq)       
print(top_n(freq, n=2))

freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
print(freq2)                              
print(top_n(freq2, n=2))





