#username:-admin
#password:-********
print("**********Welcome to BookMyShow************")
print("""
       1=="Login"
       2=="Register new account"
       3 =="Exit """)
try:
    option = int(input("Enter your choice  : "))

except:
    print("Please enter  valid choice")


if option ==1:
    print("***********Welcome to BookMyShow************")
    user  = input("Please enter a username : ").lower()
    pass_wrd = input("please enter your password :")
    if user =="admin" and pass_wrd =="********":
        print("***************welcome Admin**************")
        print("""
               1 =="Add New Movie info"
               2=="Edit Movie info"
               3=="Delete Movie"
               4=="Logout" """)
        try:
            option1 = int(input("Enter your input : "))
        except:
            print("please enter a valid input")
        lis = []
        if option1 == 1:
            print("Add new movie :")
            print("*******Welcome admin************")
            a = input("Enter your title : " )
            lis.append("Title" + ":" + a)
            b = input("Enter your genre : ")
            lis.append("Genre" + ":" + b)
            c = input("Enter your Length : ")
            lis.append("Length" + ":" + c)
            g = input("Enter your cast : ")
            lis.append("Cast" + ":" + g)
            h = input("Director : ")
            lis.append("Director" + ":" + h)
            i = input("Admin Ratings : ")
            lis.append("Admin Ratings" + ":" + i)
            j = input("Timings : ")
            lis.append("Timings" + ":" + j)
            print(lis)
        try:
            option2=int(input("Enter your input : "))
        except:
            print("Please enter a Valid input")
        if option1==2:
            print("Edit Movie")
            print("********Welcome admin********")
            d=input("Enter your title: ")
            lis.append("Title" + ":" + d)
            e = input("Enter your genre : ")
            lis.append("Genre" + ":" + e)
            f = input("Enter your Length : ")
            lis.append("Length" + ":" + f)
            g = input("Enter your cast : ")
            lis.append("Cast" + ":" + g)
            h = input("Director : ")
            lis.append("Director" + ":" + h)
            i = input("Admin Ratings : ")
            lis.append("Admin Ratings" + ":" + i)
            j = input("Timings : ")
            lis.append("Timings" + ":" + j)
            print(lis)
   # if option==2:




