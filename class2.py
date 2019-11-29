'''Write a class called Password_manager. The class should have a list called old_passwords
that holds all of the user’s past passwords. The last item of the list is the user’s current password.
There should be a method called get_password that returns the current password
and a method called set_password that sets the user’s password. The set_password
method should only change the password if the attempted password is different from all
the user’s past passwords. Finally, create a method called is_correct that receives a string
and returns a boolean True or False depending on whether the string is equal to the current
password or not.'''

class Password_manager:
    def __init__(self,old_passwords):
        self.old_passwords = old_passwords

    def get_passwords(self):
        return self.old_passwords[-1]

    def set_passwords(self,password):
        self.password = password
        for i in self.old_passwords:
            if i == self.password:
                print('Password already exist')
                break
        else:
            self.old_passwords.append(self.password)
            print('Password changed successfuly!')
            
                
            '''
            if self.password not in self.old_passwords:
                return self.old_passwords.append(self.password)
                print('Okay')
            else:
                return "Password already exist"
            '''    
    

    def is_correct(self,p):
        self.p = p
        if self.p == self.old_passwords[-1]:
            return True
        else:
            return False

a = Password_manager(['samson1234','ola','Hola'])
print(a.get_passwords())
a.set_passwords('Samosky')
print(a.is_correct('Hol'))







    
        
    
