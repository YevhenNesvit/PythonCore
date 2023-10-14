#Повернемося до попереднього завдання та виконаємо зворотне.
#Напишіть рекурсивну функцію encode для кодування списку або рядка.
#Як аргумент функція приймає список ( наприклад ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]) або рядок (наприклад, "XXXZZXXYYYZZ").
#Функція повинна повернути закодований список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

def encode(data):
    res = list()
    global quantity
    if not data :
        return []
    def iflist(data) :
        quantity = 0
        for i in range(len(data)) :
            if i != len(data) - 1:
                if data[i] == data[i + 1] :
                    quantity += 1
                else :
                    break
            else :
                quantity = len(data) - 1
                break
        return quantity

    if isinstance(data, list) :
        quantity = iflist(data)
    else :
        data = list(data)
        quantity = iflist(data)
    res.append(data[quantity])
    res.append(quantity + 1)
    data = data[quantity + 1:]
    result = res
    result.extend(encode(data))
    
    return result
print(encode("XXXZZXXYYYZZ"))