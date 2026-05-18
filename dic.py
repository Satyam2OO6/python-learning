grade={
    "sat" : 76,
    "sam" : 67,
    "marry" : 76,
}
mean=sum(grade.values())/len(grade)
print(mean)
print(grade.keys())
print(grade.items())
grade.update({"bob" : 99})
print(grade)
print(grade.get("sat"))
