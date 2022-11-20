#Exercise 4 (Задание 4)
x = 9**22 + 3**66 - 12 # Изначальное число
countTWO = 0
while x > 0: #Перевод в 3-ую сс
    if x % 3 == 2:
        countTWO += 1
    x //= 3
print(countTWO)# Ответ 42


#Exercise 5 (Задание 5)
x = 9**7 - 3**10 + 3**21 - 9 # Изначальное число
countTWO = 0
while x > 0: #Перевод в 3-ую сс
    if x % 3 == 2:
        countTWO += 1
    x //= 3
print(countTWO)# Ответ 11


#Exercise 6 (Задание 6)
x = 12**34 + 7 * 12**26 - 3*12**16 + 2 * 12**5 + 552 # Изначальное число
visitedDigits = [] # Массив в котором храняться цифры которые были в записи
while x > 0: #Перевод в 12-ую сс
    if x % 12 not in visitedDigits: # Если цифра еще не встречалось добавляем в массив
        visitedDigits.append(x%12) # добавление цифры
    x //= 12
print(len(visitedDigits))# Выводим размер массива. Ответ 8

#Exercise 8 (Задание 8)
#Вспомним как переводить число из любой сс в 10
#С помощью полиномиальной формулы: 567_8 = (5*8**2 + 6*8**1 + 7*8**0) = 375_10
#Поймем что у них при подстановке x будет отличаться следующее:
#9759x_17 = (9 * 17**4 + 7 * 17**3 + 5 * 17**2 + 9 * 17**1 + x * 17 ** 1)
generalPart1 = 9 * 17**4 + 7 * 17**3 + 5 * 17**2 + 9 * 17**1 # общая часть для 9759x
generalPart2 = 3 * 17**4 + 1 * 17**2 + 0 + 8 ##общая часть для 3x108
generalResult = generalPart2 + generalPart1
for x in range(17):
    if (generalResult + x + x* 17**3) % 11 == 0: #Проверяем делиться ли число с этим x на 11
        print((generalResult + x + x* 17**3) / 11)
        break
#Ответ: 95306