temp=[450,340,380,480]

for i in temp:
    print(i/10)

#Anoter method of list comprehension

temps=[i/10 for i in temp ]
print(temps)


#list comprehension with if condition
temps=[i/10 for i in temp if i>400]
print(temps)
