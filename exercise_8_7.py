def make_album(name_singer,name_album, acount_treck=''):
    info={'name' : name_singer, 'album':name_album}
    if acount_treck:
        info['acount']=acount_treck
    return info

singer_album = make_album('sting', 'new')
print(singer_album)
singer_album=make_album('sting', 'new', 23)
print(singer_album)


while True:
    n_singer=input('Enter name your favorite singer\n or enter "q" for exit: ')
    if n_singer == 'q': break

    n_album = input('Enter name album \n or enter "q" for exit:')
    if n_album == 'q': break

    print(make_album(n_singer,n_album))

unprinted_design = [1,'fire','Non']
completed_design=[]
import print_models,show_comleted_models
print_models.print_models(unprinted_design,completed_design)
show_comleted_models.show_completed_models(completed_design)