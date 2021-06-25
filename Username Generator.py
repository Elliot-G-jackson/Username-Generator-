#Created by Elliot-G-jackson
#Creation date 25/6/21
#Username Generator 

print('Wellcome to the username generator \nEnter EXIT to exit the program')
print('=====================')

#Main while 
while True:
    firstname = input('Enter your fisrt name')
    if firstname == 'EXIT':
        break

    lastname = input('Enter your last name')
    if lastname == 'EXIT':
        break
    
    else:
        fore = firstname[0:2]
        last = lastname[0:4]
        userName = fore + last
        print(fore + last)
    
    
     


