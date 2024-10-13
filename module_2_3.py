my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
resultat = []

while (index_ < len(my_list)):
    if (my_list[index_] != 0):
        if (my_list[index_] > 0):
            resultat.append(my_list[index_])
            index_ += 1
            continue
        else:
            break
    index_ += 1
    continue

print('Результат: ', resultat)
