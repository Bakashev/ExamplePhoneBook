import user_9_3 as us
user_one = us.User('sergey','bakashev',age=36,children=2,education='higher')
user_two = us.User('alina', 'bakasheva', age=6, national = 'belarus')
user_three = us.User('darya', 'bakasheva', age=4)
user_one.great_user()
user_one.describe_user()
user_two.great_user()
user_two.describe_user()
user_three.great_user()
user_three.describe_user()

# exercise 9-5
print('Crate new user and new attribute')
user_four = us.User('ivan','ivanov')
print(user_four.login_attempts)
for i in range(55):
    user_four.incremen_login_attempts()
print('New value attribute login_attemots : {}'.format(user_four.login_attempts))
user_four.reset_login_attempts()
print(user_four.login_attempts)