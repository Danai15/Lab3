# TODO Напишите функцию count_letters
from collections import Counter

def count_letters(text):
# Убираем все символы, кроме букв, и приводим к нижнему регистру
filtered_text = ''.join(filter(str.isalpha, text)).lower()
# Подсчитываем количество каждой буквы
letter_count = Counter(filtered_text)
return letter_count

def calculate_frequency(letter_count, total_letters):

frequency = {letter: count / total_letters for letter, count in letter_count.items()}
return frequency




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
letter_count = count_letters(main_str)

total_letters = sum(letter_count.values())

frequency = calculate_frequency(letter_count, total_letters)

for letter, freq in sorted(frequency.items()):
print(f"{letter}: {freq:.2f}")






