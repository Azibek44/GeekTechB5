#Множества set, frozenset
# a = [1,3,4,5]
# b = [4,5,6]
# print(list(set(a+b)))

# numbers = {1,2,3,4,5,6,7,8,9,2}
# print (numbers)
# # print(numbers[0]) #Нельзя в set выводить по индексу
# print(numbers[::-1]) #Set не поддерживает срезы

# names = {"Askhat", "Kurmanbek", "Daniel", "Asylbek"}
# print(names)
# names.add("Nursultan") #Добавляе Nursultan dв set множество
# print(names)
# names.remove("Askhat") #Удаляем Askhat из множества
# print(names)
# names.pop()   # Удаляем случайное значение
# print(names)
# # names.update("Kurmanbek") #Добавляет Kurmanbek и делит по буквам
# # print(names)
# names.clear() #очищяем set
# print(names)

# lst = []
# print(type(lst))
# hello = ""
# print(type (hello))
# st = {}
# print(type(st))

# lst = [10,4.0,False,"Geek",[1,2,3], {1,2,3}]
# print(lst)
# sft = {1,1.0, True, "1"}
# numbers ={10,5,20,100,1,2,3}
# print(sft)
# print(sorted(numbers))
# frzn = frozenset([1,2,3,4,5,6])
# print(frzn)
# frzn.add(10)
# print(frzn)
# frzn.remove(2)
# print(frzn)

#Tuple - кортеж
# numbers = (1,10,11,2,3,4,4,5)
# print(numbers)
# tup = (1,1.0,True,"Hello", [1,2,3,] , {1,2,3}, (10,20))
# print(tup)
# print(tup.count("Hello"))
# print(tup.index(1))
# print(tup[2])
# print(tup[0:3])

# cars = ("BMW", "Mersedes-Benz","Ferrari")
# # print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append("Tesla")
# print(lst_cars)
# cars = tuple(lst_cars)
# print(cars)

# tup = (10,)
# print(type(tup))

# st = {}
# print(type(st))

# student = {"student" : "Askhat", "age" : "18"} #Создаем список student
# print(student)
# print(len(student))  #выводим длину словаря student
# print(student['age'])  #по ключу age выводим значение с словоря student
# student.setdefault('language', 'python')  #Добовляем с словарь новый ключ и значение
# print(student['language'])
# student.pop('age')  #Удаляем по ключ age и его значение
# print(student)
# student['language'] = 'JavaScript' #Обновляем по ключузначение
# print(student)
# student['place_study'] = 'GeekTech' #если нужного ключа нету то он добавит его
# print(student)
# print(type(student.keys())) #
# print(student.values())

# contact = {'Askhat' : "0778909091"}
# while True:
#     command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("Введите имя: ")
#         add_number = input("Введите номер: ")
#         if add_name not in contact:
#             contact.setdefault(add_name, add_number)
#             print("Успешно добавлено")
#         else:
#             print("Такой контакт уже существует")
#     elif command == "3":
#         delete_contact = input("Кого удалить?: ")
#         if delete_contact in contact:
#             contact.pop(delete_contact)
#             print("Успешно удалено")
#         else:
#             print("Такого контакта нету")
#     elif command == "4":
#         update_contact = input("Кого хотите обновить?:")
#         new_contact = input("Новое имя: ")
#         if update_contact in contacts:
#            new_contact = input("Новое имя: ")
#            contacts[contacts.index(update_contact)] = new_contact
#            print("Успешно добавлен")
#     else:
#         print("Не найден")                   