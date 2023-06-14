# Medical Data Analysis

This project aims to predict the most appropriate drug for a given patient based on medical data. The dataset used contains information about patients, including age, sex, blood pressure, cholesterol level, sodium-to-potassium ratio, and the drug prescribed. The dataset consists of 200 instances of patient data.

## Dataset Description

The dataset includes the following variables:

1. **Age**: Numerical value representing the age of the patient.
2. **Sex**: Categorical variable indicating the sex of the patient ("M" for male or "F" for female).
3. **BP**: Categorical variable representing the blood pressure of the patient ("HIGH," "NORMAL," or "LOW").
4. **Cholesterol**: Categorical variable indicating the cholesterol level of the patient ("HIGH" or "NORMAL").
5. **Na_to_K**: Numerical value representing the ratio of sodium to potassium in the patient's blood.
6. **Drug**: Categorical variable representing the drug prescribed for the patient ("drugA," "drugB," "drugC," "drugX," or "drugY").

## Running the Code

To visualize the decision tree using the CART algorithm and generate a PNG image, follow the steps below:

1. Ensure that you have the necessary dependencies installed, such as pandas, pydotplus, scikit-learn, and Graphviz.
2. Place the `drug200.csv` file in the same directory as your Python script or notebook.
3. Copy and paste the provided code into your Python script or notebook.
4. Run the code.

The code begins by importing the required libraries, such as `os`, `pandas`, `pydotplus`, `Image` (from IPython.display), `LabelEncoder` (from scikit-learn), and `DecisionTreeClassifier` and `export_graphviz` (from scikit-learn's tree module).

Next, it reads the CSV file `drug200.csv` using `pd.read_csv()`. The non-numeric values are encoded using label encoding (`LabelEncoder`) to convert them into numeric representations.

The features (independent variables) are separated from the target variable, and a CART model is trained using the `DecisionTreeClassifier()`.

The `export_graphviz()` function is used to generate a DOT file (`tree.dot`) that represents the decision tree. The `feature_names` and `class_names` parameters are provided to label the features and target classes correctly. Additionally, the `rounded` and `filled` parameters ensure that the tree nodes are displayed with rounded corners and filled colors.

Before visualizing the decision tree, it's necessary to set the `PATH` variable for Graphviz. Make sure to update the `os.environ["PATH"]` line with the appropriate path to the Graphviz binary on your system.

The code then uses `pydotplus` to read the DOT file and save the decision tree as a PNG image (`tree.png`).

Finally, the generated image is displayed using `Image()` from the `IPython.display` module.

Feel free to modify the code to suit your specific environment and file locations.

For detailed instructions on running the code and additional information, please refer to the project's README file.

## Project Objective

The goal of this project is to develop a predictive model using the CART (Classification and Regression Trees) algorithm to determine the most suitable drug for a patient based on their medical attributes. The CART algorithm is particularly well-suited for this dataset since it is a decision tree algorithm commonly used for classification problems.

As the target variable in this dataset is categorical (drug type), and the independent variables consist of both categorical and continuous variables, the CART algorithm can effectively predict the drug type based on the values of the independent variables.

## Alternative Algorithms

While the CART algorithm is the primary choice for this dataset, three other algorithms could be considered:

1. **K-Nearest Neighbors (KNN)**: KNN is a classification algorithm that can be suitable for this type of problem. However, since the dataset includes a mixture of categorical and continuous variables, the performance of KNN may not be as effective as the CART algorithm.

2. **Logistic Regression**: Logistic regression is another classification algorithm. However, similar to KNN, it might not perform as well as CART due to the mixed variable types in the dataset.

3. **Random Forest**: Random forest is a decision tree-based algorithm that builds multiple trees and averages the results. While it could be an option, it may not outperform the CART algorithm since it can lead to overfitting, especially when dealing with a relatively small dataset.

## Conclusion

In conclusion, the CART algorithm is the most suitable choice for this dataset. By utilizing its decision tree approach, it can effectively predict the appropriate drug for a patient based on their medical attributes. The alternative algorithms, such as KNN, logistic regression, and random forest, may not provide optimal performance given the mixed nature of the independent variables.
