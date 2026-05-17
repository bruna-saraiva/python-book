# validate a string
# receive a string, the min and max of characters as parameters
# return true if the string length is between the values
def validate_string(s:str, min:int, max: int) -> bool:
    if isinstance(s,str):
        if (len(s) > min and len(s) < max):
            return True
        return False
    else: 
        return False
    
min = 2
max = 8

s = "abracadabra"
print(f"response: {validate_string(s,min,max)}") 

