# Задача1
# Создайте кортеж it_company = (‘Google’, ‘Amazon’, ‘Microsoft’) вам нужно
# превратить кортеж в список и добавить новое значение ‘Tesla’, затем
# превращаете список обратно в кортеж

# it_company = ("Google", "Amazon","Microsoft")
# print(it_company)
# lst_company = list(it_company)
# print(lst_company)
# lst_company.append("Tesla")
# print(lst_company)
# it_company = tuple(lst_company)
# print(it_company)


# Задача2
# Из 1 задания попробуйте вывести индекс ‘Amazon’
# it_company = ('Google', 'Amazon', 'Microsoft', 'Tesla')
# print(it_company)
# lst_company = list(it_company)
# print(lst_company)
# print(it_company.index('Amazon'))


# Задача3
# Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способам

# it_company = ('google', 'amazon', 'microsoft', 'Tesla')
# tup_company = tuple(it_company)
# print(tup_company)
# lst_company =  list(tup_company)
# print(lst_company)
# lst_company[0] = 'apple'
# tup_company = tuple(lst_company)
# print(tup_company)


# Задача4
# Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’

# it_company = ('apple', 'amazon', 'microsoft', 'Tesla')
# print(it_company[0:3:2])


# Задача5 Есть кортеж
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview') 
# print(text_tuple.Lower.count('python'))
# вам нужно посчитать сколько раз встречается слово python независимо от регистра


# Задача6
# Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd':
# 600}. Объедините их в один при помощи встроенных функций языка Python.
# Подсказка: метод update()
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)



# Задача7
#  Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2,
# ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения
# словаря на 5 и вывести в терминал.
# numbers = numbers = {'1num' : 1, 'num_2': 2, 'num_3' : 3 , 'num_100' :100 }
# numbers['1num'] = 1 * 5
# numbers['num_2'] = 2 * 5
# numbers['num_3'] = 3 * 5 
# numbers['num_100'] = 100 * 5
# print(numbers)


# Задча8 
# Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза
# student = {"name" : "Askhat", "age" : "17"}
# student["age"] = 17 * 2
# print(student)


# Задача9
# Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}.
 # Обновите age в 16
# student = {"name" : "Askhat", "age" : "18"}
# print(student)
# student['age'] = '16'
# print(student)


# Задача10
# Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. 
# Удалите ключ и значение age
# student = {"name" : "Askhat", "age" : "17"}
# student.pop('age')
# print(student)

# Задчача11
#  Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и
# значение(Западный Анар)
# student = {"name" : "Askhat"}
# print(student)
# student.setdefault('address', 'Западный Анар')
# print(student)

# ДОП ЗАДАНИЕ:
# 12) Напишите программу, которая имитирует проверку пароля, придуманного
# пользователем. Пользователь вводит пароль, а потом ещё раз его же, для
# подтверждения. И пароль который вводит пользователь записывается в пустое
# множество после проверок
# Если первый пароль, который ввел пользователь короче 8 символов, программа
# выводит на экран слово "Короткий пароль!"
# Если же первый пароль достаточно длинный, но в нём содержится сочетание
# символов "123", программа выводит на экран слово "Простой пароль!"
# Если же предыдущие проверки пройдены успешно, но введённые слова-пароли не совпадают, то программа выводит на экран слово "Различаются."
# Если же и третья проверка пройдена успешно, программа выводит "OK"
# (латинскими буквами) и выводит “Пароль создан!”

# 13) Сделайте до конца контакты, которую вы делали на уроке. Сделайте 4 команду
# для обновления