import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'students_adaptability_level_online_education.csv' 
data = pd.read_csv(file_path)

# Define the order for adaptivity levels
adaptivity_order = ['Low', 'Moderate', 'High']
financial_condition_order = ['Poor', 'Mid', 'Rich']
colors = ['#99ff99', '#ffcc99', '#ff6666']  # Green for 'Low', Orange for 'Moderate', Red for 'High'
data['Adaptivity Level (Predicted)'] = pd.Categorical(data['Adaptivity Level (Predicted)'],
                                                      categories=adaptivity_order,
                                                      ordered=True)
data['Financial Condition'] = pd.Categorical(data['Financial Condition'],
                                            categories=financial_condition_order,
                                            ordered=True)

# Function to create stacked bar chart
def stacked_bar_chart(data, category, title):
    counts = data.groupby(category)['Adaptivity Level (Predicted)'].value_counts(normalize=True).unstack()
    counts = counts.reindex(adaptivity_order, axis=1, fill_value=0)
    counts.plot(kind='bar', stacked=True, color=colors, figsize=(10, 6))
    plt.title(title)
    plt.ylabel('Proportion')
    plt.xticks(rotation=0)  # Rotate x-axis labels to horizontal
    plt.legend(title='Adaptivity Level', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()



# Create visualizations
stacked_bar_chart(data, 'Institution Type', 'Adaptability by Institution Type')
stacked_bar_chart(data, 'Financial Condition', 'Adaptability by Financial Condition')
stacked_bar_chart(data, 'Device', 'Adaptability by Device Used')
stacked_bar_chart(data, 'Internet Type', 'Adaptability by Internet Type')
stacked_bar_chart(data, 'Network Type', 'Adaptability by Network Type')



'''
# Visualization for Adaptability by Institution Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Institution Type', hue='Adaptivity Level (Predicted)', data=data, order=['Non Government', 'Government'], hue_order=adaptivity_order)
plt.title('Adaptability by Institution Type')
plt.show()

# Visualization for Adaptability by Financial Condition
plt.figure(figsize=(10, 6))
sns.countplot(x='Financial Condition', hue='Adaptivity Level (Predicted)', data=data, order=['Poor', 'Mid', 'Rich'], hue_order=adaptivity_order)
plt.title('Adaptability by Financial Condition')
plt.show()

# Visualization for Adaptability by Device Used
plt.figure(figsize=(10, 6))
sns.countplot(x='Device', hue='Adaptivity Level (Predicted)', data=data, hue_order=adaptivity_order)
plt.title('Adaptability by Device Used')
plt.show()

# Visualization for Adaptability by Internet Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Internet Type', hue='Adaptivity Level (Predicted)', data=data, hue_order=adaptivity_order)
plt.title('Adaptability by Internet Type')
plt.show()

# Visualization for Adaptability by Load-shedding Experience
plt.figure(figsize=(10, 6))
sns.countplot(x='Load-shedding', hue='Adaptivity Level (Predicted)', data=data, order=['Low', 'High'], hue_order=adaptivity_order)
plt.title('Adaptability by Load-shedding Experience')
plt.show()

# Visualization for Adaptability by Network Type
plt.figure(figsize=(10, 6))
sns.countplot(x='Network Type', hue='Adaptivity Level (Predicted)', data=data, order=['2G', '3G', '4G'], hue_order=adaptivity_order)
plt.title('Adaptability by Network Type')
plt.show()

# Visualization for Adaptability by Location (Geographic Location)
plt.figure(figsize=(10, 6))
sns.countplot(x='Location', hue='Adaptivity Level (Predicted)', data=data, hue_order=adaptivity_order)
plt.title('Adaptability by Geographic Location')
plt.show()

'''