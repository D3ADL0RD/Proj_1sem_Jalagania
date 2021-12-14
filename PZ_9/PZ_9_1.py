# Вариант 5.
# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах можно приобрести книги Пушкина и Тютчева

def convert(s):
    str1 = ""
    return (str1.join(s))

stores = {'Магистр': {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'},
          'ДомКниги': {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'},
          'БукМаркет': {'Пушкин', 'Достоевский', 'Маяковский'},
          'Галерея': {'Чехов', 'Тютчев', 'Пушкин'}}

storesWithBook = []

authorToSearch = {'Пушкин', 'Тютчев'}

for k, v in stores.items():
    if authorToSearch.issubset(v):
        storesWithBook.append(k)

print('В магазинах {} можно найти книги следующих авторов: {}'.format(storesWithBook, authorToSearch))