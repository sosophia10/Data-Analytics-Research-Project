# Data Analytics Research Project: Barriers for students’ adaptability to online educational settings

## Purpose:
The Data Analytics Research Project demonstrates the application of concepts, methods, and tools learned throughout the course. Using a chosen dataset, we perform analyses using R, Python, and SQL to produce statistical summaries, visualizations, and conclusions.

## Contents:
1. **Exploratory Data Analysis**:
   - Data ingestion and exploration using R, Python, and SQL.
   - Univariate and multivariate analyses with statistical summaries.
   - Tables and visualizations.

2. **Tools Used**:
   - **R** for data cleaning, transformation, and statistical analysis.
   - **Python** for further analysis and visualizations.
   - **SQL** for data schema creation and query execution.

3. **Research Paper**:
   - Includes research questions, approach, literature search, analysis, results, and discussion.
   - Citations and references.

## Files:
- **Python Files**: used for exploratory data analysis. Each file focuses on specific research questions, by loading the `students_adaptability_level_online_education.csv` dataset and creating visualizations using matplotlib and seaborn. 
  - `q1a.py` This script generates pie charts to represent the distribution of students' adaptability levels ("Low", "Moderate", and "High") based on their education    level ("School", "College", "University").
  - `q1b.py` This script generates stacked bar charts to visualize the relationship between students' financial conditions ("Poor", "Mid", "Rich") and their adaptivity levels ("Low", "Moderate", "High").
  - `q1c.py` This script generates comparative pie charts that visualize how load-shedding (electricity availability: "Low", "High") and location ("Local", "Distant") conditions correlate with students' adaptivity levels ("Low", "Moderate", "High").
  - `q3a.py` This script calculates the proportion of students with high adaptivity under various conditions (e.g., location, class duration, financial condition) and generates a horizontal bar chart. The chart visualizes which conditions are most strongly associated with higher adaptivity rates, providing insights into factors that contribute to adaptability in online education.
  - `sql-distributions.py` This script connects to the `student_adaptivity.db` database and executes SQL queries from the `distributions.sql` file. It then plots the results of each query as bar charts to display the distribution of various features (e.g., age, financial condition, or location).
- **R Files**:
  - `q2a.r` This script is focused on transforming categorical variables, such as "Institution Type", "Financial Condition", "Internet Type", and others, from the dataset into numeric factors.
  - `q2b.r` This R script focuses on generating heatmaps to analyze relationships between various factors (e.g., "Self LMS", "Class Duration", "IT Student") and adaptivity levels. It uses ggplot2 to create visualizations that show patterns in how different factors affect student adaptability.
- **SQL Files**:
  - `distributions.sql` This file contains queries that calculate the distribution of various categorical variables from the dataset, such as gender, age range, education level, institution type, location, financial condition, and more.
- **Database & Dataset**:
  - `student_adaptivity.db` SQLite database used for querying and analysis.
  - `students_adaptability_level_online_education.csv` Dataset with various features of students related to adaptability in online education in Bangladesh.

## How to Run:
1. Clone the repository:
   ```
   git clone https://github.com/your-username/data-analytics-research-project.git
   ```
   
2. Install the necessary dependencies:

   Python packages can be installed with:
   ```
   pip install -r requirements.txt --user
   ```

   Ensure you have R and SQL properly configured.
   Run each analysis file individually (example for Python):

   ```
   python q1a.py
   ```

   For SQL scripts:

   Load the database `student_adaptivity.db` into your preferred SQL environment.
   Execute queries in `distributions.sql`.

