temp=[68.7,65.7,7.8]
grade={
    "sat" : 76.6,
    "sam" : 67.5,
    "marry" : 76.9,
}



for i,j in temp,grade:
    print(round(i,j))
    
for marks in grade.keys():
    print(marks)

for marks in grade.values():
    print(round(marks))

for letter in "hello":
    print(letter.title())



while True:
    print(1)
    print("done")

while True:
    a=int(input("Enter your massage"))
    if a>5:
        break
    else:
        print("valid number")
