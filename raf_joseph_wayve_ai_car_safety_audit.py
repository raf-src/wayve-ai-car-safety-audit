
#Importing the pandas library for data manipulation and analysis
import pandas as pd

#Create file path to scene_metadata file for safety auditing
df = pd.read_csv("/Users/raf/Desktop/data_workbook/scene_metadata.csv")

#Clean column headers and set unique Scene ID as index for precise log tracing
df.columns = df.columns.str.strip()
df.set_index("scene_id", inplace = True)

print(df.head())

# Audit dataset structure and verify unique environmental factors
df.info()
print(df["Weather"].unique())
print(df["Road Type"].unique())

# SAFETY AUDIT LOGIC (The Risk Score Calculation)
def calculate_danger(row):
    score = 0

# Environmental Risks (Rain/Night)
    if row["Weather"] == "Rainy":
        score += 3
    elif row["Weather"] == "Overcast":
        score += 1
    elif row["Weather"] == "Sunny":
        score += 0 

    if row["Time of Day"] == "Night":
        score += 3

    elif row["Time of Day"] == "Dusk": 
        score += 1

    elif row["Time of Day"] == "Day":
        score += 0

# Same Vehicle Traffic Direction Multiplier

    if row["Same direction Vehicle Traffic"] == "No": 
        score += 1

    elif row["Same direction Vehicle Traffic"] == "Yes":
        score += 0

# Infrastructure Risk (High-Speed environments carry higher severity)
    if row["Road Type"] == "Highway": 
        score += 5
    
    elif row["Road Type"] == "Urban": 
        score += 3

    elif row["Road Type"] == "Residential": 
        score += 1

    elif row["Road Type"] == "Rural":
        score += 0

# Oncoming Vehicle Traffic Multiplier

    if row["Oncoming vehicle traffic"] == "No":
        score += 0

    elif row["Oncoming vehicle traffic"] == "Yes": 
        score += 1

# Cross Vehicle Traffic Multiplier

    if row["Cross vehicle traffic"] == "No": 
        score += 0

    elif row["Cross vehicle traffic"] == "Yes":
        score += 2

#Dynamic Actor Risks (presence of vulnerable road users)

    if row["Pedestrian crossing road"] == "No": 
        score += 0

    elif row["Pedestrian crossing road"] == "Yes": 
        score +3

    #Pedestrian on sidewalk Multiplier

    if row["Pedestrian on sidewalk"] == "No": 
        score += 0 

    elif row["Pedestrian on sidewalk"] == "Yes":
        score += 2

    if row["Cyclists / motorbike present"] == "No":
        score += 0

    elif row["Cyclists / motorbike present"] == "Yes":
        score += 2

#High Priority Safety Trigger (Immediate attention required) Triggers sensor re-calibration
    if row["Large Exposure Change"] == "No":
        score += 0

    elif row["Large Exposure Change"] == "Yes":
        score += 3

#Traffic Light Change Multiplier

    if row["Traffic Light Change"] == "No": 
        score += 0

    elif row["Traffic Light Change"] == "Yes": 
        score += 1

#High Priority Safety Trigger (Immediate attention required) Indicates intent change
    if row["Changing brake light / indicator"] == "No": 
        score += 0

    elif row["Changing brake light / indicator"] == "Yes":
        score += 3

    return score

# Transformation & Ranking
df["Danger Score"] = df.apply(calculate_danger, axis = 1)

# Sort by Danger Score to prioritize high-risk scenarios for review
df.sort_values("Danger Score", ascending = False, inplace = True)

# Preview the top 20 high-risk scenes for manual safety audit
print(df[["Weather", "Time of Day","Same direction Vehicle Traffic", "Road Type", "Oncoming vehicle traffic", "Cross vehicle traffic", "Pedestrian crossing road", "Pedestrian on sidewalk", "Cyclists / motorbike present", "Large Exposure Change", "Traffic Light Change", "Changing brake light / indicator", "Danger Score"]].head(20))

# Export sanitized audit results to for Azure Cloud storage and Power BI visualization
df.to_csv("/Users/raf/Desktop/data_workbook/self_driving_car_risk_score_results.csv")
print("Success! The Danger Auditfile has been saved to your workbook folder")