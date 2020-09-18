def f(x):
    result = ''
    for line in x:
        result += line[0] + ': ' + str(line[1]) + '\n'
    return result

x = [('Pavel', 0), ('Natasha', 100)]

answer = f(x)
print(answer)