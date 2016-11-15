my_string = 'Test string for me. Test one. Test two. One more!'
words = my_string.split(' ')
unique_words = {}
for word in words:
    unique_words[word] = ''
print(unique_words.keys())

my_string = 'Test string for me. go away. Test one. Test two. One more!'
words = my_string.split(' ')
unique_words = {}
for word in words:
    unique_words.setdefault(word, 0)
    unique_words[word] += 1

print(unique_words)

restricted = {'sleep', 'rest'}
str_1 = 'I want to sleep and have a rest'
for restricted_word in restricted:
    str_1 = str_1.replace(restricted_word, '***')
print(str_1)

first_text = 'This is a new text. Hello world'
second_text = 'This is another new text/ Bye!'
first_text = first_text.split(' ')
second_text = second_text.split(' ')
list_of_same_words = []
for word_first_text in first_text:
    for word_second_text in second_text:
        if word_first_text == word_second_text:
            list_of_same_words.append(word_first_text)
print(set(list_of_same_words))

phones = {
    'Oleg': ['0501112233', '011223366'],
    'Max': ['02233336677'],
    'Lena': ['02233336677'],
    'Egor': ['02233336677', '011223366'],
}
sorted_phones = {}

for person in phones:
    for phone in phones[person]:
        sorted_phones.setdefault(phone, [])
        sorted_phones[phone].append(person)

print(sorted_phones)

product_1 = {
    'title': 'Ноутбук Asus',
    'price': 100,
    'photo': '1.jpg',
    'params': {
        'diag': 14,
        'cpu': 'Intel Core i5',
    }
}
product_2 = {
    'title': 'Ноутбук Lenovo',
    'price': 200,
    'photo': '2.jpg',
    'params': {
        'diag': 15,
        'cpu': 'Intel Core i7'
    }
}
products = [product_1, product_2]

srch = input('Введите поисковую строку: ')
for i in range(0, len(products)):
    if products[i]['title'].find(srch) != -1:
        print(products[i])
    for param_val in products[i]['params'].values():
        if str(param_val).find(srch) != -1:
            print(products[i])