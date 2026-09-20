"""ЛР3: нормализация текста, токенизация и частоты слов"""

import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold:
        text = text.casefold()

    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')

    text = re.sub(r'[\t\r\n\v\f]', ' ', text)
    #сырая строка помогает оставить слешы как они есть и не вызывать их назначение

    text = re.sub(r' +', ' ', text).strip()

    return text


def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Посчитать, сколько раз встречается каждый токен.

    count_freq(["a", "b", "a"])
    {'a': 2, 'b': 1}
    """
    freq: dict[str, int] = {}
    for token in tokens:
        # .get() вернёт 0, если ключа ещё нет, вместо KeyError
        freq[token] = freq.get(token, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Вернуть топ-N пар (слово, частота).

    Сортировка по убыванию частоты, при равенстве — по алфавиту"""

    sorted_items = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:n]

#эта проверка чтобы, если я запустил вручную этот файлик, то он выполняется
#а если я обратился сюда к функции, чтобы он не работал (этот код ниже)
if __name__ == "__main__":
    # контрольные тесты из задания
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"bb": 2, "aa": 2, "cc": 1}
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]

    print("Все тесты пройдены")



