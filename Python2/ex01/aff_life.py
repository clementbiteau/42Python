import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load

def aff_life(file: str):
    data = load(file)
    
    try:
        french_data = data[data['country'] == 'France']
        if french_data.empty:
            raise AssertionError(f"{french_data} is empty")
        french_data = french_data.drop(columns='country')
        french_data = french_data.T
        french_data.columns = ['life_expectancy']
        french_data.index.name = 'year'
        #french_data.to_csv('./french_data')
        french_data.reset_index(inplace=True)
        french_data['year'] = french_data['year'].astype(int)
        
        plt.plot(french_data['year'], french_data['life_expectancy'])
        plt.title("France Life expectancy Projections")
        plt.xlabel("Year", )
        plt.ylabel("Life expectancy")
        #plt.grid(True)
        plt.xticks(
        ticks=range(french_data['year'].min(), french_data['year'].max() + 1, 40))
        plt.savefig("Life_Expectancy_France.png")
        plt.close()
        
    except AssertionError as e:
        print(f"AssertionError: {e}")
        
    

def main():
    path = "../life_expectancy_years.csv"
    aff_life(path)
    
if __name__ == "__main__":
    main()