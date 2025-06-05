# dict = {
#     'brand':'honda',
#     'electric':'false',
#     'year':'2002',
#     'colors':['red','green','pink']
# }
#
# print(dict)
# print(type(dict))
# print(len(dict))
#
# #get method
# x = dict.get("brand")
# print(x)
#
# #keys() method
#  #y = dict.keys()
# y = dict.values()
# print(y)
#
# #add a new item
# print(dict)
#
# dict['model'] = 'JH0123G'
# print(dict)

thisdict = {
    'brand':"ford",
    "model":"Mustang",
    "year":1964
}
if "model" in thisdict:
    print("yes, It exists in the dictionary")
else:
    print("No, it does not exists.")

thisdict['year'] = 2018
print(thisdict)

thisdict.update({"year":2022})
print(thisdict)