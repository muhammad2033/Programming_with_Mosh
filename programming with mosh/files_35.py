import readline


with open('file_35.txt', "r") as f:

    data = f.read()
    print(data)



                                    # writing



with open('file_35.txt', "w") as f:

    data = f.write("whwre r u coder.....")
    print(data)
    f.close()

                                        # readline


    text = f.readline()
    print(text)    

# it is used to read first line 
    