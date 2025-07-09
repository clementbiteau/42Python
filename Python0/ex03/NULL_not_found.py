import inspect
import math

def NULL_not_found(object: any) -> int:
    frame = inspect.currentframe().f_back #check caller's frame as type not in scope
    variables = frame.f_locals
    
    exclude_vars = {"__doc__", "__package__", "__name__", "__file__", "__builtins__", "__spec__", "__cached__"} #avoid false matches by builtins
    
    name = [var_name for var_name, var_value in variables.items() if var_value is object and var_name not in exclude_vars]
    
    if name:
        var_name = name[0]
        if isinstance(object, float) and math.isnan(object):
            print(f"Cheese: nan {type(object)}")
        elif isinstance(object, str) and object == "":
            print(f"{var_name}: {type(object)}")
        else:
            print(f"{var_name}: {object} {type(object)}")    
    else:
        print("Type not Found")
        
    return 1