import pandas as pd
import json

# Sample dataframe
data = {'id': [1, 2, 3],
        'json_column': ['{"name": "John", "age": 25, "city": "New York"}',
                        '{"name": "Jane", "age": 28, "city": "Los Angeles"}',
                        '{"name": "Tom", "age": 22, "city": "Chicago"}']}

df = pd.DataFrame(data)

# Function to expand JSON column into multiple columns
def expand_json_column(df, json_column):
    # Parse the JSON column and expand it into a DataFrame
    json_df = df[json_column].apply(json.loads).apply(pd.Series)
    
    # Concatenate the original dataframe with the new columns
    df = pd.concat([df, json_df], axis=1)
    
    return df

# Apply the function
df = expand_json_column(df, 'json_column')

# Drop the original JSON column if needed
df = df.drop(columns=['json_column'])

# Display the dataframe
print(df)
