class User ():
    def __init__(self,first_name,last_name,**other_info):
        self.other_info = {}
        self.name = first_name
        self.surname = last_name
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