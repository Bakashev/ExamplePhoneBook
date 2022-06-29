class Privileges ():
    def __init__(self):
        self.privileges =['- create new user', '- delete othere user', '- update users']

    def show_access_rights (self):
        #print('user {} {} can :'.format(self.name.title() , self.surname.title()))
        print("user can")
        for i in self.privileges:
            print(i)