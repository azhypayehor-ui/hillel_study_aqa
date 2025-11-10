adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

fixed_text_1 = adwentures_of_tom_sawer.replace("\n", " ")
print("Task 1:", fixed_text_1)
# task 02 ==
""" Замініть .... на пробіл
"""
fixed_text_2 = adwentures_of_tom_sawer.replace(" ....", " ")
print("Task 2:", fixed_text_2)
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

adwentures_of_tom_sawer = ' '.join(adwentures_of_tom_sawer.split())
print("Task 3:", adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

find_h = adwentures_of_tom_sawer.count("h")
print('Number of h inn text', find_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

words = adwentures_of_tom_sawer.split()
counted_words = 0
for word in words:
    if word.istitle():
        counted_words += 1
print(f"Total amount of words starts with capital: {counted_words}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
step_1 = adwentures_of_tom_sawer.find("Tom")
step_2 = adwentures_of_tom_sawer.find("Tom", step_1 + 1)
print("Task 06:", step_2)
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")
print("Task 07:", adwentures_of_tom_sawer_sentences)
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

fourth_sentance = fixed_text_2.split(". ")
print("Task 8:", fourth_sentance[3].lower())
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
find_begining = fixed_text_2.find("By the time")
if find_begining != -1:
    print(f"Task 09: Find on index {find_begining}.")
else:
    print("Task 09: beggining is absent")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
split_by_sentance = fixed_text_2.split(". ")
last_sentance_split = split_by_sentance[-1].split(" ")
print("Task 10: Amount of words =", len(last_sentance_split))