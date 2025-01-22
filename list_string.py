demolist =[1,89, 23.4, 100, "23%", 92, "88A"] 
#funtion only returning a list of string values from demolist 
def extract_non_numbers(list):
    result = [item for item in list if not isinstance(item, (int, float))]
    
    if not result:
        return ["No non-integer or non-float numbers found"]
    
    return result


answer_1 = extract_non_numbers(demolist)
print(answer_1)