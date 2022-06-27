#size and text
def make_shirt(shirt_size = 'large',shirt_text = 'I love python'):
    """Print text on size shirt"""
    print("You choose {} shirt \n"
          "text on shirt: {}".format(shirt_size,shirt_text))

make_shirt('small', 'DO IT')
make_shirt(shirt_text='You must', shirt_size='medium')
make_shirt()
