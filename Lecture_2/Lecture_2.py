#Функция list() - функция создающая список(массив)

list_1 = [1, 2, 3, 4]
print(list_1)
print(*list_1) # звездочка убирает квадратные скобки в терминале

for i in list_1: # Поочередно выведет все значения из списка
    print(i)

print(len(list_1))

list_1.append(5) # добавляет значение к списку
print(list_1)

list_2 = []
print(list_2)
for i in range(5):
    list_2.append(i)
    print(list_2)







