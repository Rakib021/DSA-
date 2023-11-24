#Dictionary ={key:value}



person ={
    "name":"Rakibul Islam",
    "age":21,
    "grades" : {"math":50,'English':60,"bangla":33}
    
}

# print(person["grades"]["bangla"])

for key,val in person.items():
    print(key,val)