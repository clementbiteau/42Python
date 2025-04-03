def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """give_bmi will return the calculated BMI (Body Mass Index) given from the list of integers | floats
    BMI is calculated as follows : weight (in kg) / height (in meters power of 2)"""
    # Rules are => entries must be of type int or float only -> else and Assertion Error will be raised
    # The lists can be of different sizes (so we must apply the calculation as long as there are values to compare)
    try:
        assert(weight and height and None not in weight and None not in height), "Height and Weight must have values"
        if len(height) != len(weight):
            raise AssertionError("not the same number of indexes in lists")
        assert all(isinstance(h, (int, float)) for h in height), "Height must be integer or float"
        assert all(isinstance(w, (int, float)) for w in weight), "Weight must be integer or float"
        bmi = [w / (h ** 2) for w, h in zip(weight, height)]
        return bmi
    except AssertionError as e:
        print(f"Assertion Error: {e}")

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply_limit will receive the BMI, previously calculated by give_bmi, and will return True, if the BMI has
    surpassed the index, and False if it has not."""
    try:
        assert (bmi and None not in bmi), "BMI cannot be empty to be studied"
        assert all(isinstance(r, (int, float)) for r in bmi), "BMI must be integer or float value"
        assert (isinstance(limit, int)), "Limit must be expressed as an integer"
        limit_check = [r > limit for r in bmi]
        return limit_check
    except AssertionError as e:
        print(f"Assertion Error: {e}")