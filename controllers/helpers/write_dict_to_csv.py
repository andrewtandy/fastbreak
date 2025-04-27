import pandas as pd
import os

def write_dict_to_csv(data, filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_dir = os.path.abspath(os.path.join(current_dir, '..', '..', 'models', 'csv_data'))
    
    csv_file_path = os.path.join(csv_dir, f"{filename}.csv")
        
    dataframe = pd.DataFrame(data)

    return dataframe.to_csv(csv_file_path, index=False)