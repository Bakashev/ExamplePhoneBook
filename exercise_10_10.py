def count_word_book(*fielnames,word = 'the'):
    for fielname in fielnames:
        try:
            with open(fielname, encoding='utf-8') as f_obj:
                content = f_obj.read()
                #print(content.count(word))
        except FileNotFoundError:
            print('Fiel not found!!!')
        else:
            print('Book {} have {} word - {}'. format(fielname, content.count(word),word))

#fielname = 'magic.txt'
count_word_book('Alice.txt','magic.txt','book.txt', 'book_two.txt','little princesse.txt')
count_word_book('Alice.txt','magic.txt','book.txt', 'book_two.txt','little princesse.txt', word='and')
