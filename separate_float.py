exampleList=["Welcome","Jungle","Story",45,18,"Monday","33%",90,3,55.7,20,"Lunch-hour",18.0945,509.2,"16%",99,3,85.21,"Call-of-duty"]

mydic={
  "intergers":"",
  "Strings":"",
   "floats":""
}

def extract_doublenumbers(list):
     return [item for item in list if isinstance(item, float)]


answer = extract_doublenumbers(exampleList)
print(answer)
mydictionary={
 "intergers":[45,18,90,3,20,99,3],
  "Strings":["Welcome","Jungle","Story","Monday","33%","Lunch-hour","16%","Call-of-Duty"],
   "floats":[55.7,18.0945,509.2,85.21]

}
print(mydictionary["floats"])  




print(mydictionary)









