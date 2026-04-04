# wayve-ai-car-safety-audit

Situation: Conducted a diagnostic audit of autonmous driving sensor metadata to identify and trace logic gaps in model decision making.

Action: Engineered a Python based Risk Scoring Engine t perform a rigorous evaluation of sensor logs, identifying 24 systemic safety gaps. The result revealed 13 "Critical Failures" (Risk > 13) where the model remained in low sensitivity mode despite extreme danger levels. 

Result: Identified 13 critical edge cases representing 8.21% of total project risk. 

Root Cause Analysis: 100% of critical failures involve Vulnerable Road Users (VRUs), specifically 7 cases of pedestrians crossing and 6 involving cyclists/motorbikes.

Strategic Priority: recalibrating VRU detection in urban/ residential environments is now the #1 priority for model retraining. 

Programming: Python(Pandas) used for data ingestion, cleaning, and developing logic based risk engine.

Data Engineering: Developed a Cumulative Risk Index evaluating environmental factors (e.g Weather) and dynamic actors (e.g Pedestrians, Cyclists).

Cloud Infrastructure (Azure): Utilized Azure Blob Storage and Account Key Authentication to host and protect diagnostic audit logs and ensure a live data pipeline. 

Visualization: Power BI leveraged for cross filter diagnostics, visualizing risk distribution, and isolating high priority "False Negatives".
