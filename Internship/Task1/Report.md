# Dataset Analysis Report

**Tools Used:** Python (Pandas, NumPy)
**Environment:** Jupyter Notebook / VS Code

---

## 1. Introduction

This report presents an exploratory analysis of two datasets: the **Titanic Dataset** and the **Students Performance Dataset**. The objective is to understand the data structure, identify feature types, analyze data quality, and evaluate the suitability of these datasets for machine learning applications.

---

## 2. Dataset Loading and Structure

Both datasets were loaded using the Pandas library. The first and last five records were displayed using `head()` and `tail()` to understand the structure of rows and columns.

* The **Titanic dataset** contains passenger details such as age, gender, class, fare, and survival status.
* The **Students Performance dataset** contains demographic details and exam scores of students.

---

## 3. Feature Type Identification

### Titanic Dataset

* **Numerical Features:** Age, Fare, SibSp, Parch
* **Categorical Features:** Sex, Embarked, Ticket, Cabin, Name
* **Ordinal Features:** Pclass (1st, 2nd, 3rd class)
* **Binary Feature:** Survived (0 = No, 1 = Yes)

### Students Performance Dataset

* **Numerical Features:** Math score, Reading score, Writing score
* **Categorical Features:** Gender, Race/Ethnicity, Parental level of education
* **Binary Features:** Lunch, Test preparation course

---

## 4. Data Types and Statistical Summary

The `df.info()` function was used to inspect data types and identify missing values.
The `df.describe()` function provided statistical summaries such as mean, minimum, maximum, and standard deviation for numerical features.

---

## 5. Categorical Data Distribution

Unique values in categorical columns were checked using `unique()` to understand data distribution:

* In the Titanic dataset, survival varies significantly based on gender and passenger class.
* In the Students dataset, performance differs based on lunch type and test preparation status.

---

## 6. Target Variable and Input Features

* **Titanic Dataset:**

  * Target Variable: `Survived`
  * Input Features: All other columns
* **Students Performance Dataset:**

  * Target Variable: `Math score`
  * Input Features: Remaining demographic and academic attributes

---

## 7. Dataset Size and Machine Learning Suitability

* Titanic Dataset: Approximately 891 rows and 12 columns
* Students Performance Dataset: Approximately 1000 rows and 8 columns

Both datasets are sufficiently sized for basic machine learning models.

---

## 8. Data Quality Observations

* The Titanic dataset contains missing values in the Age, Cabin, and Embarked columns and shows slight class imbalance.
* The Students Performance dataset has no missing values and is well-structured.
* Both datasets are suitable for machine learning after appropriate preprocessing.

---

## 9. Conclusion

The analysis demonstrates a clear understanding of data structure, feature types, and data quality. The Titanic dataset requires more preprocessing, while the Students Performance dataset is clean and beginner-friendly for machine learning tasks.

---

**Final Outcome:**
This analysis helps interns understand dataset structure, data quality issues, and machine learning readiness.
