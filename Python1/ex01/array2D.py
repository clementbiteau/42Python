import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert (isinstance(start, int)), "Start needs to be an integer"
        assert (isinstance(end, int)), "End needs to be an integer"
        assert (isinstance(family, list)) or len(family), "Family must be a clear list"
        assert all(isinstance(item, list) and (len(item) == len(family[0])) for item in family), "All items must be list and and must be same length as initialy stated in the first item that we take as reference"
        arr = np.array(family)
        subset_arr = arr[start:end]
        
        print(f"My shape is : {arr.shape}")
        print(f"My new shape is : {subset_arr.shape}")
        return subset_arr.tolist()     
       
    except AssertionError as e:
        print(f"Assertion Error: {e}")