# dictionary={
#     "anuska":"she is my sister",
#     "papa":"father",
#     "mom":"mother",
#     1:2,
#     2:"hello"
#     }
# print(dictionary)#--> method to print dictionary
# print(dictionary["mom"])#-->method to print values using keys
# print(dictionary.values())#-->method to print values of dictionary
# print(dictionary.keys())#-->methods to print keys of dictionary
# print(dictionary.items())#-->methods to print the keys and values in list


#nested dictionary

# nested_dict={
#     "harry":"programeer",
#     "love":"mother",
#     "added_dict":{"anuska":"bunu",
#     "hero":"anurag"}
# }
# print(nested_dict)
# updateddic={
#     "school":"place to study",
#     "love":"family",
#     "bibek":"chor khate randi ko baan"
# }
# nested_dict.update(updateddic)
# print(nested_dict)
# print(nested_dict.get("harry"))

# methods of dictionary
renky={
    "hello":"way of greeting",
    "marks":[40,50,60],
    "fuck":"is said to bhandari",
    "anotherdict":{
        1:2,
        2:"hello",
        "sensational":"what a performance",
        "3rddict":{
            "guys":"just word for appreciation",
            "love":"way of expressing feeling"
        }
    }
}
# print(renky)
# print(renky["hello"])
# print(renky["anotherdict"][2])
# print(renky["anot3herdict"]["3rddict"]["love"])

#--> methods of dictionary
# print(renky.keys())#---> prints the keys of dictionary
# print(list(renky.keys()))#--->conversion of dictionary to list
# print((renky.values()))#--->prints the values of dictionary
# print(renky.items())#-->display key value pair
updateddict={
    "shuvam":"u tuber",
    "lara":"gf of mine",
    3:6,
    "fuck":"shit bibek chor"
}
# print(renky)
# renky.update(updateddict)
# print(renky)
print(renky.get("hello1"))#--> returns none if key is not present
print(renky["hello1"])#-->throws keyerror
