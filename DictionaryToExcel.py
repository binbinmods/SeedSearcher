import pandas as pd

def dicts_to_excel(dict_sheet_pairs, output_file):
   
    # Create Excel writer object
    with pd.ExcelWriter(output_file) as writer:
        for dictionary, sheet_name in dict_sheet_pairs:
            max_values = max(len(values) for values in dictionary.values())
            
            columns = ['Item'] + [f'Seed {i+1}' for i in range(max_values)]
            df = pd.DataFrame(columns=columns)
            
            for key, values in dictionary.items():
                row = [key] + values + [''] * (max_values - len(values))
                df.loc[len(df)] = row
            
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Example usage
if __name__ == "__main__":
    caravanDict = {}

    shopDict = {}

    guaranteedDict = {}

    mythicDict = {}

    
    # Create list of (dictionary, sheet_name) pairs
    dict_sheet_pairs = [
        (caravanDict, 'Caravan Items'),
        (shopDict, 'Shop Items'),
        (guaranteedDict, 'Boss Drops'),
        (mythicDict, 'Mythics')
    ]
    
    # Convert to Excel file
    dicts_to_excel(dict_sheet_pairs, 'SeedList.xlsx')