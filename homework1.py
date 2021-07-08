
n = input("число: ")
all = n + n + n + n
print(all)



name = "имя"
years_old = 54
print(name,years_old)
name = input("Введите имя: ")
years_old = int(input("Введите возраст: "))
print(name,years_old)



time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")



n = int(input("Введите число - "))
total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
print("Сумма чисел n + nn + nnn - %d" % total)