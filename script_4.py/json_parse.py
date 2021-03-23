# def json_parse(json_string):
#       # print the keys and values
#     value=0
#     # parse json and calculate 
#     print("Total Marks:", value )


# if __name__ == '__main__':
#     # code for reading json file
#     # Assign json data  to variable json_string
# #     json_parse(json_string)


import json

jsonfile = open("package.json")
jsondata =  jsonfile.read()
py_dict = json.loads(jsondata)
print("Json: ",py_dict)
total = 0
for i in py_dict.values():
    total+=int(i)
print("Total marks: ",total)
