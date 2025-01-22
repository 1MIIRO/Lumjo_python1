demolist =[1,89, 23.4, 100, "23%", 92, "88A"]


#function to return list of  only double/float values from the demolist 
def extract_doublenumbers(list):
     return [item for item in list if isinstance(item, float)]


answer = extract_doublenumbers(demolist)
print(answer)




