text = input("Введите текст: ")
words_list = text.split()
word_count = {}
for word in words_list:
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1
most_common = max(word_count, key=word_count.get)
longest = max(words_list, key=len)
print("Наиболее встречающееся слово:", most_common)
print("Самое длинное слово:", longest)