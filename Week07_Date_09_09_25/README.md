# Week 07 — Iris Dataset Analysis 🐦🌸

Author: Steve Omusula  
Date: September 09, 2025

Brief: Exploratory data analysis of the classic Iris dataset. The notebook loads iris.csv, inspects and cleans the data, computes summary statistics, and produces visualizations to highlight feature relationships and class separation.

What I have done ✅

- Imported libraries: pandas, matplotlib, seaborn. 📦
- Set seaborn theme for plots. 🎨
- Loaded iris.csv with try/except and printed confirmation. 📥
- Displayed dataset info, head, and missing-value checks. 🔎
- Cleaned data by dropping missing rows (df.dropna()). 🧹
- Computed descriptive statistics (mean, median, std), feature ranges, and correlations. 📈
- Counted samples per species and computed average feature values by species. 🧮
- Created visualizations:
  - Pairplot (scatter matrix) by species 🔍
  - Boxplot of sepal length by species 🌸
  - Histogram of petal width 📊
  - Correlation heatmap 🔥
- Summarized findings: dataset shape, class balance, distinguishing features, and strong petal length/width correlation. 📝

Files in this folder 📁

- assignment.ipynb — Jupyter notebook with analysis and plots.
- iris.csv — dataset (place in this folder before running notebook).
- README.md — this file.

How to run (Windows, VS Code) ▶️

1. Open this folder in VS Code.
2. Open assignment.ipynb and run cells (recommended: run all).
3. Or use PowerShell:
   - cd "PLP_Python_Assignments\Week07_Date_09_09_25"
   - jupyter nbconvert --to notebook --execute "assignment.ipynb" --inplace
4. Ensure required packages are installed:
   - pip install pandas matplotlib seaborn jupyter
