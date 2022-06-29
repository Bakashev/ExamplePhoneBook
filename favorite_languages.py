from collections import  OrderedDict
"""use orderly dictionary """
favorite_languges = OrderedDict()
favorite_languges['sergey']= 'python'
favorite_languges['pavel'] = 'Java'
favorite_languges['stas'] = 'C#'
for key,value in favorite_languges.items():
    print ( '{} favorite language is {} ' .format(value.title(),key.title()))

