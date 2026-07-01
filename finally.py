try:
    file = open("data.txt", "r")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program Finished.")