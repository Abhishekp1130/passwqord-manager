print("*****PASSWORD MANAGER*****")
def encrypt(data,shift):
    encrypted=""
    for i in range (len(data)):
        char=data[i]
        if(char.isupper()):
            encrypted+=chr((ord(char)+shift-65)%26+65)
        elif(char.islower()):
            encrypted+=chr((ord(char)+shift-97)%26+97)
        elif(char.isdigit()):
            number=(int(char)+shift)%10
            encrypted+=str(number)
        else:
            encrypted+=char
    return encrypted
def decrypt(data,shift):
    decrypted=""
    for i in range (len(data)):
        char=data[i]
        if(char.isupper()):
            decrypted+=chr((ord(char)-shift-65)%26+65)
        elif(char.islower()):
            decrypted+=chr((ord(char)-shift-97)%26+97)
        elif(char.isdigit()):
            number=(int(char)-shift)%10
            decrypted+=str(number)
        else:
            decrypted+=char


menu=""
while menu!=1 or menu!=2:
    menu=input("save a new password or view stored passsword?"
    "\n1. Input a new password "
    "\n2. View passwords "
    "\n3. exit ")
    if menu=='1':
        websiteorsoftwarename=input("enter the sitename or software name you want to store password: ")
        username=input("enter the username: ")
        password=input("enter the website or software password: ")
        shift=4
        file = open("securepasworddata.txt","a")
        file.write(encrypt(websiteorsoftwarename,shift)+";|"+ encrypt(username,shift)+";|"+encrypt(password,shift) +"\n")
        file.close()
    if menu=='2':
        print("displaying passwords")
        file=open("securepasworddata.txt","r")
        print("websiteorsoftwarename\tusername\tpassword ")
        for i in file:
            shift=4
            data=i.split(";|")
            print(decrypt(data[0],shift) + "\t\t" + decrypt(data[1],shift) + "\t\t" + decrypt(data[2],shift))
    if menu=='3':
        exit()
        
