def count_letters(text):

    #Подсчитывает количество каждой буквы в тексте.
    #Буквы верхнего и нижнего регистра считаются одинаковыми.


    letter_count = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1
    return letter_count


def calculate_frequency(letter_dict):

    #Вычисляет частоту каждой буквы.


    total_letters = sum(letter_dict.values())
    frequency_dict = {}
    for letter, count in letter_dict.items():
        frequency_dict[letter] = count / total_letters
    return frequency_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

letter_counts = count_letters(main_str)
frequencies = calculate_frequency(letter_counts)

# Сортируем по частоте (по убыванию), затем по алфавиту для одинаковых частот
sorted_letters = sorted(frequencies.items(), key=lambda x: (-x[1], x[0]))


for letter, frequency in sorted_letters:
    print(f"{letter}: {frequency:.2f}")