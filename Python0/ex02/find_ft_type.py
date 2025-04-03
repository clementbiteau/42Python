def all_thing_is_obj(object: any) -> int:
    result = type(object)
    if result == list:
        print(f"List : {result}")
    elif result == set:
        print(f"Set : {result}")
    elif result == dict:
        print(f"Dict : {result}")
    elif result == tuple:
        print(f"Tuple : {result}")
    elif result == str:
        print(f"{object} is in the kitchen : {result}")
    else:
        print("Type not found")
    return 42
