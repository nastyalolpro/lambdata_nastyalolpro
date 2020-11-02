import pandas as pd
import numpy as np
import random

#report confusion matrix with labels

def confusion_matrix(predicted, true):
    
    if len(predicted) != len(true):
        print("Error: lengths of labels do not match")

    else:
        d = {'predicted':predicted, 'true':true}
        df = pd.DataFrame(data=d)
        
        tp = []
        tn = []
        fp = []
        fn = []
   
        for row in range(len(df)):
            if df['predicted'].iloc[row] == df['true'].iloc[row]:
                if df['predicted'].iloc[row] == 1:
                    tp += 1
                else:
                    tn += 1
            else:
                if df['predicted'].iloc[row] == 1:
                    fp += 1
                else:
                    fn += 1
          
        d = {' ':['Predicted Positive (1)', 'Predicted Negetive (0)'], 'Actually                   Positive (1)': [tp, fn], 'Acyually Negative (0)': [fp, tn]}

        df = pd.DataFrame(data=d)
        return df


#"Generate more data" function, takes dataframes and makes more rows

def more_data(df, num_rows):
   
    d = {}

    for col in df:
        
        column = list(df[col])
        for i in range(num_rows):

            num = random.randint(0, len(df))
            new_val = df[col].iloc[num]
            column.append(new_val)
        
        d[col] = column  
    
    df = pd.DataFrame(data = d)
    
    return df
