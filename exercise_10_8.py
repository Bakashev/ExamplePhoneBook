def fieles_read(*fieles):
    for fiel in fieles:
        try:
            with open(fiel) as f_obj:
                text = f_obj.read()
                print(text.title())
        except FileNotFoundError:
            print('File not found {}'.format(fiel))

fieles_read('cat.txt','dog.txt')