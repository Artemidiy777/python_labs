"""ЛР3, задание Б: статистика по тексту из stdin"""

import os
import sys

SRC_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(SRC_DIR)
#os.path.abspath достраивает до полного пути
#os.path.dirname отрезает от пути ласт часть и возвращает то что осталось
#делаем 2 раза, чтобы дойти до src
from lib.text import normalize, tokenize, count_freq, top_n


"""Задание со звездочкой"""
def print_table(items: list[tuple[str, int]]) -> None:
    if not items:
        return
    max_word_len = max(len(word) for word, _ in items)
    header = f"{'слово'.ljust(max_word_len)} | частота"
    print(header)
    print('-' * len(header))
    for word, count in items:
        print(f"{word.ljust(max_word_len)} | {count}")

"""Задание B"""
def main() -> None:
    raw_text = sys.stdin.read()

    normalized = normalize(raw_text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top5 = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    table_mode = os.environ.get("TABLE_MODE") == "1"

    if table_mode:
        print_table(top5)
    else:
        for word, count in top5:
            print(f"{word}:{count}")

if __name__ == "__main__":
    main()

#echo "привет мир привет" | python3 src/lab03/text_stats.py

#echo "привет мир привет по-настоящему 2025" | TABLE_MODE=1 python3 src/lab03/text_stats.py

