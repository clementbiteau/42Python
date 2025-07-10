import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from load_csv import load

def preprocess_country_data(data, country):
    country_data = data[data['country'] == country]
    if country_data.empty:
        raise AssertionError(f"No data found for {country}")
    
    country_data = country_data.drop(columns='country').T
    country_data.columns = ['Population']
    country_data['Population'] = country_data['Population'].str.replace('M', '').astype(float)
    country_data.index.name = 'year'
    country_data.reset_index(inplace=True)
    country_data['year'] = country_data['year'].astype(int)
    country_data = country_data[(country_data['year'] >= 1800) & (country_data['year'] <= 2050)]
    
    return country_data

def aff_pop(file: str, compare_with: str = None):
    data = load(file)
    
    try:
        france = preprocess_country_data(data, "France")
        country_list = [france]
        labels = ["France"]
        colors = ["green"]
        
        if compare_with:
            other = preprocess_country_data(data, compare_with)
            country_list.append(other)
            labels.append(compare_with)
            colors.append("blue")

        # Determine y-axis ticks from combined data
        yticks = [20, 40, 60]
        ytick_labels = [f"{y}M" for y in yticks]

        # Plot each country
        for df, label, color in zip(country_list, labels, colors):
            plt.plot(df['year'], df['Population'], label=label, color=color)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend(loc="lower right")
        plt.xticks(ticks=range(france['year'].min(), france['year'].max() + 1, 40))
        plt.yticks(yticks, ytick_labels)
        
        plt.tight_layout()
        plt.savefig("Population_Comparison.png")
        plt.close()
        
    except AssertionError as e:
        print(f"AssertionError: {e}")

def main():
    data = '../population_total.csv'
    aff_pop(data, compare_with="Belgium")

if __name__ == "__main__":
    main()