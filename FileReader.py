try:
    f = open("sample.txt","w+")
    f.write("using try catch")
    text = f.read()
    print(text)
finally:
    f.close()