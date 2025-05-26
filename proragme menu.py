import pickle
while True:
    print("""1-Create file
          2-Display The Binary File
          3-Exit""")
    opt=int(input("enter the option"))
    if opt==1:
        f=open("student.dat","wb")
        n=int(input("enter the number student"))
        for i in range(n):
            name=input("enter the name")
            eng=int(input("enter the english marks"))
            lan=int(input("enter the lan marks"))
            phy=int(input("enter the phy marks"))
            math=int(input("enter the math marks"))
            chem=int(input("enter the chem marks"))
            cs=int(input("enter the cs marks"))
            l=[name,eng,lan,phy,math,chem,cs]
            pickle.dump(l,f)
        f.close()
    elif opt==2:
        f=open("student.dat","rb")
        try:
            while True:
                p=pickle.load(f)
                print(p)
        except EOFError:
            f.close()
    else:
        print("exit")
        break
            
