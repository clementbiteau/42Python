import pandas as pd

def load(path: str) -> pd.DataFrame:
    try:
        #pd.options.display.max_rows = 3 -> should we wish to have a set number of max rows to print out to Terminal
        data = pd.read_csv(path)

        print(f"Loading dataset with dimensions {data.shape}")
        return data
    
    except FileNotFoundError:
        print(f"❌ File not found: '{path}'")
    except pd.errors.EmptyDataError:
        print(f"❌ File is empty: '{path}'")
    except pd.errors.ParserError:
        print(f"❌ File is not a valid CSV or is corrupted: '{path}'")
    except Exception as e:
        print(f"❌ Unexpected error while loading '{path}': {e}")
    return None