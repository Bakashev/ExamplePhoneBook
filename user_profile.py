
def build_profile(first,last, **info):
    """получение имя фамилии и произвольное количество - ключ=значение"""
    build_info={}
    build_info['name']=first
    build_info['Sername']=last
    for key , value in info.items():
        build_info[key]=value
    print(build_info)

build_profile('sergey','bakashev', location='Minsk', profesion ='BA' )
