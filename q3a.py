import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file_path = 'students_adaptability_level_online_education.csv'
data = pd.read_csv(file_path)

# Melt the data to long format
melted_data = data.melt(id_vars='Adaptivity Level (Predicted)', var_name='Condition Type', value_name='Condition')

# Function to rename conditions based on the column
def rename_conditions(row):
    if row['Condition Type'] == 'Age Range' and not row['Condition'].startswith("Aged "):
        return "Aged " + row['Condition']
    elif row['Condition Type'] == 'Location':
        return "Local" if row['Condition'] == 'Yes' else "Distant"
    elif row['Condition Type'] == 'Class Duration (Hours Per Week)' and not row['Condition'].endswith(" hours"):
        return row['Condition'] + " hours"
    elif row['Condition Type'] == 'Self Lms':
        return "No Self LMS" if row['Condition'] == 'No' else "Self LMS"
    elif row['Condition Type'] == 'IT Student':
        return "Generic Student" if row['Condition'] == 'No' else "IT Student"
    else:
        return row['Condition']

# Apply the function to rename conditions
melted_data['Condition'] = melted_data.apply(rename_conditions, axis=1)

# Recalculate the proportion of high adaptivity
high_adaptivity_rate = melted_data[melted_data['Adaptivity Level (Predicted)'] == 'High'].groupby('Condition').size()
total_rate = melted_data.groupby('Condition').size()
adaptivity_proportion = (high_adaptivity_rate / total_rate).fillna(0).reset_index(name='Proportion of High Adaptivity')

# Sort conditions by their proportion of high adaptivity
sorted_conditions = adaptivity_proportion.sort_values(by='Proportion of High Adaptivity', ascending=False)

# Create the mosaic-like plot using bar chart
fig, ax = plt.subplots(figsize=(15, 10))
colors = plt.cm.Spectral(np.linspace(0, 1, len(sorted_conditions)))
y_positions = range(len(sorted_conditions))
ax.barh(y_positions, sorted_conditions['Proportion of High Adaptivity'], color=colors)
ax.set_yticks(y_positions)
ax.set_yticklabels(sorted_conditions['Condition'])
ax.set_xlabel('Proportion of High Adaptivity')
ax.set_title('Conditions and Their Proportion of High Adaptivity')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest values at the top
plt.show()
