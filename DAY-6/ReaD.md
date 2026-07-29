# Employee Performance – Data Cleaning & EDA

Day 6 internship task : clean a messy employee dataset and explore it for real patterns — no ML model, just cleaning, analysis, and visualization.

## Project Structure

```
├── employee_performance_dataset.csv     # raw dataset (155 records, intentionally messy)
├── employee_performance_cleaned.csv     # cleaned dataset after processing
├── analysis.py                          # main script (cleaning + EDA + charts)
├── chart1_dept_performance.png
├── chart2_salary_dist.png
├── chart3_exp_vs_perf.png
├── chart4_salary_boxplot.png
├── chart5_correlation.png
├── chart6_gender_pie.png
├── chart7_promotion.png
├── Employee_Performance_Analysis_Report.docx
└── README.md
```

## Dataset

155 employee records across 6 departments (Sales, IT, HR, Marketing, Finance, Operations) with columns for demographics, salary, attendance, performance score, overtime, projects completed, and training hours.

The raw data was built with real-world messiness baked in on purpose:
- 3 duplicate rows
- Missing values in Salary, Attendance, Performance Score, Training Hours
- Department labels with inconsistent casing/spacing (`"it "`, `"SALES"`, `" Hr"`)
- Salary values stored as text (`"110700.0 PKR"`)
- 2 outlier values in Overtime Hours
- 1 empty/unnecessary column

## What the Script Does

1. **Cleaning** — drops duplicates, fills missing values with column medians, fixes the salary data type, standardizes department names, caps overtime outliers, drops the empty column.
2. **EDA** — summary statistics, department-wise performance comparison, low-attendance filter, correlation analysis.
3. **Performance Index** — custom metric: `(Performance Score × 0.5) + (Projects Completed × 0.3) + (Attendance % × 0.2)`.
4. **Visualizations** — 7 charts (bar, histogram, scatter, box plot, heatmap, pie, promotion breakdown) using Matplotlib and Seaborn.
5. **Promotion Eligibility System** — rule-based classification into `Promoted`, `Needs Improvement`, or `Requires Training` based on Performance Score and Attendance thresholds.

## Key Findings

- Dataset went from 155 → 152 rows after removing duplicates.
- IT has the highest average performance score (57.6), Operations the lowest (49.7).
- Experience correlates strongly with Performance Score (r = 0.69) and Salary (r = 0.72).
- Attendance has almost no relationship with performance (r = 0.20) or projects completed (r = -0.04) — showing up isn't the same as performing well.
- Only 4 of 152 employees meet the bar for immediate promotion under the rule set used.


## How to Run

```bash
pip install pandas numpy matplotlib seaborn
python analysis.py
```

Outputs the cleaned CSV and all chart PNGs in the project folder.

## Tools Used

Python, Pandas, NumPy, Matplotlib, Seaborn

## Author

Atiqa Jabeen — AI/ML Intern