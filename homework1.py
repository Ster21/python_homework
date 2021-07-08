#1:
name = "имя"
years_old = 54
print(name,years_old)
name = input("Введите имя: ")
years_old = int(input("Введите возраст: "))
print(name,years_old)


#2:
time = int(input("Введите время "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"{hours} : {minutes} : {seconds}")


#3:
n = int(input("Введите число "))
all = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print(f"Сумма чисел n + nn + nnn = {all}")


#4:
n = abs(int(input("Введите целое положительное число ")))
max = n % 10

while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    elif n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break


#5:
plus = int(input("Выручка фирмы "))
minus = int(input("Издержки фирмы "))

if plus > minus:
    print(f"Прибыль — выручка больше издержек {plus / minus:.2f}")
    men = int(input("Численность сотрудников фирмы "))
    print(f"Прибыль фирмы в расчете на одного сотрудника {plus / men:.2f}")

elif plus == minus:
    print("Фирма работает в ноль")

else:
    print("Убыток — издержки больше выручки")



#6:
a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
