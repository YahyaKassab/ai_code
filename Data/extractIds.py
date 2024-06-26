import pandas as pd
import json


# Convert the JSON data to a DataFrame
df = pd.read_json('Academy.lectures.json')

# Step 2: Extract and reformat the necessary fields
# Extract the '_id' and 'course' fields, and rename them to 'id' and 'course'
df_extracted = df[['_id', 'course']].copy()
df_extracted['id'] = df_extracted['_id'].apply(lambda x: x['$oid'])
df_extracted['course'] = df_extracted['course'].apply(lambda x: x['$oid'])
df_extracted = df_extracted.drop(columns=['_id'])

# Reformat the DataFrame to match the desired structure
df_extracted = df_extracted.rename(columns={"course": "course"})

# Step 3: Export to a new JSON file
output_data = df_extracted.to_dict(orient='records')
with open('extracted_data.json', 'w') as file:
    json.dump(output_data, file, indent=4)
