dictionary = {
    "apple": "яблоко",
    "banana": "банан",
    "cherry": "вишня",
    "dog": "собака",
    # Добавьте больше слов и переводов
}

while True:
    word = input("Введите слово для перевода (или 'выход' для завершения): ")
    if word.lower() == "выход":
        break

    if word in dictionary:
        translation = dictionary[word]
        print(f"Перевод слова '{word}' - {translation}")
    else:
        print("Перевод не найден")