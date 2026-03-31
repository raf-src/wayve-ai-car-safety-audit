# wayve-ai-car-safety-audit

Situation: Conducted a diagnostic audit of autonomous driving sensor metadata to identify and trace logic gaps in model decision making

Action: Engineered a Python based Risk Scoring Engine to perform rigorous evaluation of sensor logs, isolating 16 specific "Silent Failures" where model behaviour diverged from human "Ground Truth"

Result: Achieved an 84% alignment success rate, ensuring safety prtocols met internal validation benchmarks and providing clear documentation for model retraining

Programming: Python(Pandas) used for data ingestion, cleaning, and developing logic based risk engine

Data Engineering: Developed a weighted scoring system to evaluate environmental factors like Weather, Road Type, Pedestrian presence

Cloud Infrastructure (Azure): Utilized Azure Blob Storage for hosting large scale sensor metadata and diagnostic audit logs

Visualization: Power BI used to visualize risk distribution and identify high priority edge cases
