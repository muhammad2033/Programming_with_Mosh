python = {
        "name" :  "maaz",
        "age"   :  22,
         "average" : 66.4,
        #  "average",66.7,   duplicated key is not allowed
         "is_valued"  : True   
            #key        value
        }
 
print(python.get("name")) #it returns only none,doesnt err
print(python.get("Name","saad")) 
print(python["age"])
print(python["average"])
print(python["is_valued"])

python["maaz"] = "educated" #we change the value here, updated a new value 
print(python["maaz"]) 

python["dear"] = "programmer" #we change the value here, updated a new value 
print(python["dear"])



phone = str(input("enter the phone  :  "))
conversion_numbering = {
            "1" : "asslam_alaikum! \n",
            "2" : "how r u doing?\n",
            "3" : "i'm fine,\n ",
            "4" : "what do u do?\n",
            "5" : "i am teacher of python and english , i have been learning english for several years and python for a year \n",
            "6" : "where have you been ?\n",
            "7" : "i havebeen here, nothing have to visit \n ",
            "8" : "ok good , thats sound good ",
            
            
}
output = " "
for ch in phone:
    output += conversion_numbering.get(ch,"!") +" "
print(output) 