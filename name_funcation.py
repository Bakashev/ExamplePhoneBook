def get_formated_name(first,middle,second_name = ''):

    #full_name=first + ' '+ last + '' + middle
    #return full_name.title()

    if second_name:
        full_name = first + ' ' + middle + ' ' + second_name
        return full_name.title()
    else:
        full_name=first + ' ' +middle
        return full_name.title()

