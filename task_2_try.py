# Считать/скопировать текст из файла

file = open('text.txt', 'r', encoding='utf-8')
text = file.read()
print(text)
file.close()

# Методами строк очистить текст от знаков препинания;
punctuation = [',','.','?','!','—','»','«', '(', ')']
for i in punctuation:
    text = text.replace(i,' ')
print (text)

# сформировать list со словами (split);

text = text.split()
print(text)

# привести все слова к нижнему регистру (map)
new_text = list(map(str.lower, text))
print(new_text)
#или
text = [i.lower() for i in text]
print(text)
# получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

counter_repeat ={}
for i in text:
    counter = counter_repeat.get(i,0)
    counter_repeat[i] = counter + 1
print(counter_repeat)

# вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
counter_repeat = list(counter_repeat.items())
counter_repeat.sort(key=lambda kv: kv[1], reverse=True)
print(counter_repeat[:5])

import pymorphy2
morph = pymorphy2.MorphAnalyzer()
text_lemmatization = []
for i in text:
    text_lemmatization.append(morph.parse(i)[0].normal_form)
print(text_lemmatization)

