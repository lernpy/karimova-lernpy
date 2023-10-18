print ("Здравствуйте! Расскажите, пожалуйста, о себе!")
first_name = input ("Введите Ваше имя: ")
last_name = input ("Введите Вашу фамилию: ")
birth_year = int (input ("Введите год Вашего рождения: "))
health = input ("Как Вы оцениваете свое здоровье? ")
wishs = input ("Что бы Вы хотели изменить, касательно здоровья? ")

age = 2023 - birth_year

print ("")
print ("Вот мы и познакомились!")
print ("Вас зовут", first_name + " " + last_name)
print ("Вам", age)
print ("Вы оцениваете свое здоровье как", health)
print ("Вы бы хотели изменить:", wishs)

print ("До скорой встречи!")