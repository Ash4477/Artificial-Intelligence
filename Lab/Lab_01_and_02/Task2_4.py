og_dict = {
 "name": "Kelly",
 "age": 25,
 "salary": 8000,
 "city": "New york"} 

# Keys to extract
keys = ["name", "salary"] 

new_dict = {}

for i in range(len(keys)):
    new_dict[keys[i]] = og_dict[keys[i]]

print(new_dict)