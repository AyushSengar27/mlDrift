import os
import pandas as pd
import numpy as np




class Dataset_creation:
    def __init__(self):
        pass
        
        
    def create(self):
       
        raw_data_path = 'data\AirBnB.csv'
        raw_data = pd.read_csv(raw_data_path)
        target_col = "price"
        num_cols = ["accommodates",
            "bedrooms",
            "beds",
            "minimum_nights",
            "number_of_reviews",
            "number_of_reviews_ltm",
            "review_scores_rating"]
        cat_cols = ["host_is_superhost",
            "neighbourhood_cleansed",
            "property_type",
            "room_type"]
        cols_to_keep = [target_col] + num_cols + cat_cols
        raw_data = raw_data[cols_to_keep]
        shuffled = raw_data.sample(frac=1)
        month_0,month_1,month_2= np.array_split(shuffled, 3)  
        month_data_path = os.path.join(os.getcwd(),"data","monthly_data")
        os.makedirs(month_data_path,exist_ok=True)
        month_0.to_csv("month_0.csv")
        # month_1.to_csv(month_data_path+"month_1.csv")
        # month_2.to_csv(month_data_path+"month_2.csv")


if __name__ == "__main__":
    obj = Dataset_creation()
    obj.create()


