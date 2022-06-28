import user_9_3 as us
user_admin = us.Admin('sergey', 'bakashev', age=36, national='belarus', role='admin')
user_admin.describe_user()
#user_admin.show_access_rights()

user_admin.privileges.show_access_rights()


