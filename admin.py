import user_9_3 as us , privileges as pr
class Admin (us.User):
    def __init__(self,first_name,last_name,**other_info):
        super().__init__(first_name,last_name,**other_info)
        self.privileges = pr.Privileges()