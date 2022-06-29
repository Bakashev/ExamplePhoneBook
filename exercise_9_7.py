import user_9_3 as us, admin as ad
user_admin = ad.Admin('sergey', 'bakashev', age=36, national='belarus', role='admin')
user_admin.describe_user()
#user_admin.show_access_rights()

user_admin.privileges.show_access_rights()


