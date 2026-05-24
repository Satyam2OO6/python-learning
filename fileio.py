with open ("okkk/fruit.txt","w+")as file:
    file.write("hello\nhii\nsat\nhow is it going" )
    file.seek(0)
    content=file.read()
   
print(content)

