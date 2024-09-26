import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'students_adaptability_level_online_education.csv' 
data = pd.read_csv(file_path)

# Define colors and labels for the pie charts
colors = ['#99ff99', '#ffcc99', '#ff6666']  # Colors from Low (Green) to High (Red)
labels = ['Low', 'Moderate', 'High']
education_levels = ['School', 'College', 'University']
hue_order = ['Low', 'Moderate', 'High']

# Adjust font size globally for better readability
plt.rcParams.update({'font.size': 14})

# Create a pie chart for each education level
fig, axs = plt.subplots(1, len(education_levels), figsize=(20, 6))  # Adjust the size as needed

for i, level in enumerate(education_levels):
    level_data = data[data['Education Level'] == level]['Adaptivity Level (Predicted)'].value_counts().reindex(labels, fill_value=0)
    wedges, texts, autotexts = axs[i].pie(level_data, labels=None, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[i].set_title(level)
    axs[i].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # Make the autopct font size larger for better readability
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(14)

# Create a legend and place it on the right side of the figure
plt.legend(wedges, labels, title="Adaptivity Level", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.show()


# Define age_order by sorting the 'Age Range' categories numerically
age_order = sorted(data['Age Range'].unique(), key=lambda x: int(x.split('-')[0]))

# Now create the bar chart with the sorted 'Age Range'
plt.figure(figsize=(10, 8))
sns.countplot(x='Age Range', hue='Adaptivity Level (Predicted)', data=data, order=age_order,
              hue_order=hue_order, palette=colors)
plt.title('Bar Chart of Adaptability of Various Age Levels')
plt.legend(title='Adaptivity Level (Predicted)')
plt.show()
