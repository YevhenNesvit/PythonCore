def decode(data):
    res = list()
    if not data :
        return []
    for i in range(data[1]) :
        res.append(data[0])
    data = data[2:]
    result = res
    result.extend(decode(data))
    
    return result
print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))