passwordFile = open('SecretPasswordFile.txt')
SecretPassword = passwordFile.read()
print('Enter your pass ')
typedPassword = input()
if typedPassword == SecretPassword
    print('Access granted')
    #if typedPassword == '12345' :
        #print('The password is the plain one')
else:
    print ('Access denied')    


