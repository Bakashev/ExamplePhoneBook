import restaurant as r
res=r.Restaurant('BBQ', 'Burger')
print(res.name)
print(res.type)
res.describe_restaurant()
res.open_restuarant()

res_one = r.Restaurant('mac', 'burger')
res_two = r.Restaurant('kfc','chicken')
re_three = r.Restaurant('bulbarBRO', 'national cuisine')
res_one.describe_restaurant()
res_two.describe_restaurant()
re_three.describe_restaurant()

