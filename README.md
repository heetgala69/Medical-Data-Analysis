# 🧬 Medical Data Analysis – Drug Prediction Using CART
This project uses the CART (Classification and Regression Trees) algorithm to predict the most appropriate drug for a patient based on key medical features. The model is trained on a dataset of 200 patients and visualized through a decision tree.

# ⚙️ How to Run
1. Make sure the following libraries are installed: pandas, scikit-learn, pydotplus, graphviz, IPython
2. Place the drug200.csv file in the same folder as your script or notebook.
3. Update your Graphviz path (os.environ["PATH"]) as needed.
4. Run the code to:
- Preprocess the dataset (label encoding)
- Train a decision tree classifier
- Export the tree using export_graphviz()
- Convert the tree to PNG and display it with IPython’s Image()

# 📊 Dataset Overview

| Feature       | Type        | Description                                         |
|---------------|-------------|-----------------------------------------------------|
| `Age`         | Numerical   | Patient's age                                       |
| `Sex`         | Categorical | `"M"` (Male) or `"F"` (Female)                      |
| `BP`          | Categorical | Blood Pressure – `"LOW"`, `"NORMAL"`, `"HIGH"`      |
| `Cholesterol` | Categorical | Cholesterol – `"NORMAL"`, `"HIGH"`                  |
| `Na_to_K`     | Numerical   | Sodium-to-potassium ratio in the patient's blood    |
| `Drug`        | Categorical | Target variable – `"drugA"`, `"drugB"`, `"drugC"`, `"drugX"`, `"drugY"` |

# 🧠 Model Overview
This project aims to build a predictive model that recommends the most suitable drug for a patient based on their medical attributes. Given the dataset's mix of numerical and categorical features, the CART (Classification and Regression Trees) algorithm was selected for its clarity, efficiency, and interoperability. Below is the decision tree generated from the model, which visually explains how features like sodium-to-potassium ratio, blood pressure, age, and cholesterol influence the final drug prediction:
![image](https://github.com/user-attachments/assets/a8b3cf42-2fc4-43f6-8b8f-4428cd05a1f1)
While CART was the primary algorithm used, the following alternatives were also considered:
- K-Nearest Neighbors (KNN) – Easy to implement but less effective with mixed feature types
- Logistic Regression – Works for classification but struggles with categorical inputs
- Random Forest – Powerful and accurate, but less interpretable and prone to overfitting on small datasets
Overall, CART offered the best balance between performance and explainability for this problem.
