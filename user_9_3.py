class User ():
    def __init__(self,first_name,last_name,**other_info):
        self.other_info = {}
        self.name = first_name
        self.surname = last_name
        self.login_attempts = 0
        for key, value in other_info.items():
            self.other_info[key] = value

    def describe_user(self):
         print ('User name: {} '. format(self.name.title()))
         print ('User surname: {}'. format(self.surname.title()))
         print ('Other information:')
         for key, i in self.other_info.items():
             print(key + ' - ' + str(i))
         print()

    def great_user (self):
        print ('We are glad to see you {}'.format(self.name.title()))

    def incremen_login_attempts(self):
        """incremen one for login_attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """refuse login_attempts"""
        self.login_attempts=0

class Privileges ():
    def __init__(self):
        self.privileges =['- create new user', '- delete othere user', '- update users']

    def show_access_rights (self):
        #print('user {} {} can :'.format(self.name.title() , self.surname.title()))
        print("user can")
        for i in self.privileges:
            print(i)

class Admin (User):
    def __init__(self,first_name,last_name,**other_info):
        super().__init__(first_name,last_name,**other_info)
        self.privileges = Privileges()

