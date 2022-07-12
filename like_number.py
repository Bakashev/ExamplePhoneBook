import json
fielname='like_number.json'
def check_number():
    """Number check with format"""
    number = input("Enter your favotite number")
    while number.format() != int:
        try:
            number = int(number)
        except ValueError:
            print("You enter not number.")
            number = input('Try again: ')
        else:
            return number
def get_new_number():
    """Requeest favorite user number and write file"""
    number = check_number()
    with open(fielname,'w') as f_obj:
        json.dump(number,f_obj)
def print_number():
    """Open file a"""
def like_number():