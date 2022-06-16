request_topings=['mashrooms','green_pepper']
if request_topings:
    for request_toping in request_topings:
        print ("You request " + request_toping)
    print('Finish you order')
else:
    print("Are you shuer")
print()
available_topings=['mushrooms','olives','green pepers', 'peperoni', 'pineapple'
                   ,'extra cheese']
request_topings=['mushrooms','peperoni','onion']

if request_topings:
    for request_toping in request_topings:
        if request_toping in available_topings:
            print("Your request " + request_toping)
        else:
            print('Sorry your request is fail we do not ' + request_toping)
    print('Finish your order')
else:
    print('Are you shuer')