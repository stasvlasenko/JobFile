tempa = []

with open('tempa.txt', 'r') as document:
    for line in document:
        tempa.append(int(line))

print(tempa)
avg = sum(tempa)/len(tempa)
print("Средняя температура", avg)

with open('average_temp.txt', 'w') as document:
    document.write("%.2f" % avg)
