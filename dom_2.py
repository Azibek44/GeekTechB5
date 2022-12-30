# Задача1
# Написать программу, которая будет проверять пароль. Пусть программа в начале
# запросит пароль у пользователя. В самой программе сохраните определенный пароль
# и сравните его с тем, который был введен пользователем. В случае, если пароли
# совпадают, то выведете на экран следующее сообщение: ‘Password is correct. You are
# welcome’ Если нет: ‘Password is incorrect. Please, try again’
# Программу решить 2 способами, 4 строчной if else конструкцией и 1 строчной версией
# if else

# password = "dom2022"
# login = "dom"   
# user_password = input("password:")
# user_login = input("login:") 
# if user_login == login and user_password == password:
#     print("Password is correct. You are welcome")    
# else:
#     print("Password is incorrect. Please, try again")         

# Задача2
# Написать программу, которая будет спрашивать у пользователя температуру за окном.
# Используя условные конструкции if elif else, напишите программу, которая выводит на
# экран следующее:
# 1) При условии меньше -30 градусов: “Там так холодно, лучше дома сиди!”
# 2) При условии от -30 до 0: “Холодновато. Оденься потеплее!”
# 3) При условии от 0 до 15: “Прохладно. Куртку накинь!”
# 4) При условии от 15 до 30: “Тепло. Иди погуляй в парке!”
# 5) При условии от 30 до 50 включительно: “Ого, как жарко!”
# 6) При условии выше 50: “Там такая жара, лучше сиди дома!”
# 7) В других случаях: “Ошибка!”
    
# name = int(input("-30, 0, 15, 30, 50: "))
# if name >= -30 and name < 0:
#     print("Холодновато. ОДенься потеплее!")
# elif name >= 0 and name <15:
#     print("Прохладно.куртку накинь")
# elif name >= 15 and name <30:
#     print("Тепло иди погуляй в парке ")
# elif name >= 30 and name <50:
#     print("там такая жара. лучше дома сиди")
# elif name >= 50:
#     print("Ого ка жарко!")
# else:
#     print("err")     



# Задача3
# Вам дается текст:
# name = """Advertising companies say advertising is necessary and important. It informs people about
# new products. Advertising hoardings in the street make our environment colourful. And
# adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
# programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
# healthy products. And adverts in magazines give us ideas for how to look prettier, be
# fashionable and be successful. Without advertising, life is boring and colourless.
# But some consumers argue that advertising is a bad thing. They say that advertising is bad
# for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
# know we love our children and want to give them everything. So they use children’s ‘pester
# power’ to sell their products. Finally, consumers say, if there is advertising there must be
# rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
# money."""
# print(name.count("s"))
# print(name.count("t"))
# Посчитайте количество букв s и t .

# name = "aidana"
# name_2 = "adilet"
# print((name[0] + name_2[0]) + (name[1] + name_2[1]) + (name[2] + name_2[2]) + (name[3] + name_2[3]) + (name[4] + name_2[4]) + (name[5] + name_2[5]))