fp = open("words.txt","w")
if fp:
    print("Succesfully opened")
    fp.write("i")
    fp.write("a")
    fp.write(" ")
    fp.close()