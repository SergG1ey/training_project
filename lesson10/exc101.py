f = open("file.txt", "w")
text = 1
while text != "":
    text = input()
    f.write(text + "\n")
f.close()
