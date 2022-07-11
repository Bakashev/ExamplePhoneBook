def count_words(*filenames):
    """Подсчет приблизительного количества слов"""
    for filename in filenames:
        try:
            with open(filename,encoding='utf-8') as f_obj:
                content = f_obj.read()
        except FileNotFoundError:
            msg = 'File {} not found'.format(filename)
            print(msg)

        else:
            count=content.split()
            print('Book {} have {} words '. format(filename,len(count)))

#count_words('alice.txt')
def count_word_pass(*fielnames):
    for fielname in fielnames:
        try:
            with open(fielname,encoding='utf-8') as f_obj:
                content = f_obj.read()
        except:
            with open('missing_fiels.txt', 'a') as f_obj_w:
                f_obj_w.write('{} \n'.format(fielname))
        else:
            count_word = content.split()
            print('Book {} have {}'.format(fielname,len(count_word)))