exampleList=["Welcome","Jungle","Story",45,18,"Monday","33%",90,3,55.7,20,"Lunch-hour",18.0945,509.2,"16%",99,3,85.21,"Call-of-duty"]

mydic={
  "intergers":"",
  "Strings":"",
   "floats":""
}
#I separated the strings from the examplelist then added them to the dictionary
def extract_non_numbers(list):
    result = [item for item in list if not isinstance(item, (int, float))]
    
    if not result:
        return ["No non-integer or non-float numbers found"]
    
    return result


answer_1 = extract_non_numbers(exampleList)
print(answer_1)

mydictionary={
 "intergers":"",
  "Strings":["Welcome","Jungle","Story","Monday","33%","Lunch-hour","16%","Call-of-Duty"],
   "floats":""

}
print(mydictionary["Strings"])  














































