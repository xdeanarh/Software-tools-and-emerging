MapleFreight Logistics: Late-Delivery Prediction
Project Overview
This is an individual capstone project focused on predicting late shipments for MapleFreight Logistics. It uses machine learning to estimate the probability that a shipment will arrive late and demonstrates how high-risk predictions can trigger Slack notifications.
The goal is to help logistics teams identify potentially delayed shipments earlier and prioritize them for review. The model provides risk estimates, not guaranteed delivery outcomes.
Objectives
•	Clean and prepare shipment data for machine learning.
•	Explore factors associated with late deliveries.
•	Train and compare classification models.
•	Address class imbalance and evaluate different classification thresholds.
•	Interpret model predictions using feature importance and SHAP analysis.
•	Integrate model predictions with Slack alerts.
Technologies Used
•	Python — data processing and model development
•	Pandas and NumPy — data manipulation
•	Scikit-learn — preprocessing, model evaluation, and baseline models
•	XGBoost — late-delivery classification
•	Imbalanced-learn — random oversampling and SMOTE
•	Matplotlib — visualizations
•	SHAP — model explainability
•	Google Colab — development environment
•	Slack Incoming Webhooks — alert notifications
Methodology
1.	Data preparation: Removed duplicate records and rows containing negative metrics, addressed missing values, and engineered cyclical month features.
2.	Data leakage prevention: Excluded shipment identifiers, the target variable, actual transit hours, and other unsuitable predictors.
3.	Model development: Compared a baseline classifier, Logistic Regression, Random Forest, and XGBoost.
4.	Class imbalance handling: Compared no class weighting, class weighting, random oversampling, and SMOTE.
5.	Threshold selection: Compared thresholds using validation data to balance late-shipment detection against false-positive alerts.
6.	Model evaluation: Evaluated the selected model on a held-out test set.
7.	Explainability: Examined feature importance and used SHAP analysis to investigate model behaviour.
8.	Slack integration: Developed a proof-of-concept notification workflow for shipments whose predicted late-delivery risk meets the alert threshold.
Final Model Performance
The selected model was SMOTE XGBoost with a classification threshold of 0.20.
Metric	Test Result
Accuracy	72.44%
Precision	40.91%
Recall	76.52%
F1-score	0.5331
ROC-AUC	0.8073
On the held-out test set, the model correctly identified 189 of 247 late shipments and missed 58. It generated 273 false-positive alerts.
SMOTE XGBoost was selected because it achieved a stronger overall balance across the evaluated metrics than the class-weighted alternative. However, the class-weighted model achieved higher recall, demonstrating the trade-off between detecting more late shipments and reducing unnecessary alerts.
Slack Alert Integration
The project connects predictions to a Slack channel using an incoming webhook.
•	Alert threshold: 20% predicted late-delivery probability.
•	High-risk condition: Predicted probability is at least 20%.
•	Notification: Sends shipment details and predicted risk to Slack.
•	Security: The webhook URL should be stored in a secret rather than hard-coded or printed in notebook output.
Both low-risk and high-risk test cases were prepared to verify the alert logic. The integration demonstrates a notification workflow using test data; it is not a live shipment-monitoring system.
Model Explainability
Feature importance identified weather categories, carrier categories, recent late-delivery history, service level, and number of stops among the features used by the model.
These scores describe how the model uses the available features. They do not prove that any feature or carrier causes delays. SHAP analysis provides additional insight into how feature values influence individual predictions.
Limitations and Future Improvements
•	The dataset contains extreme shipment-weight values that may reflect data-quality issues; their causes were not confirmed.
•	Standard SMOTE was applied after one-hot encoding categorical variables, which can create synthetic records with fractional categorical indicators. Future work should evaluate SMOTENC or other suitable alternatives.
•	False-positive alerts and missed late deliveries have different operational costs, so the threshold should be reviewed against business requirements.
•	Model performance should be validated on additional data before operational deployment.
•	The Slack integration requires a live data feed and further testing before it could support real-time monitoring.
AI Assistance and Critical Evaluation
AI assistance (chat GPT) was used to support code development, debugging, model interpretation, selection and documentation. The tool was used as an aid rather than substitute for checking results against the notebook and project requirements.
Example of an incorrect AI output: During the model-selection and documentation process, the AI assistant continued referring to class-weighted XGBoost at a threshold of 0.30 as the final model after the project had moved to SMOTE. I corrected this by pointing out that SMOTE was the selected approach. The final evaluation and documentation were then aligned with SMOTE XGBoost at a threshold of 0.20.
This demonstrated the importance of verifying AI-generated explanations and documentation against the actual experiments, validation results, and final model-selection decisions.
Conclusion
This project demonstrates an end-to-end machine learning workflow for late-delivery risk prediction, from data preparation and model comparison to explainability and Slack alerting. The selected SMOTE XGBoost model provides a useful starting point for identifying potentially delayed shipments, while further validation and operational testing are needed before deployment. 

