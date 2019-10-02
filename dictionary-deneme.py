
dictionary={'fatma':'23','beste':'16',"leyla":"21","erdem":"11"}
print("----------------------------Real dictionary----------------------------------------")
print(dictionary.keys())
print(dictionary.values())

#update
dictionary["fatma"]="24"
print("----------------------------Update value dictionary----------------------------------------")
print(dictionary.keys())
print(dictionary.values())

#delete
del dictionary["beste"]
print("----------------------------Delete key dictionary----------------------------------------")
print(dictionary.keys())
print(dictionary.values())

print("----------------------------check include key----------------------------------------")
print("fatma" in dictionary)
print("emircan" in dictionary)