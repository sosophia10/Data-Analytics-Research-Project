import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('students_adaptability_level_online_education.csv')

# Define the order and colors for the adaptivity levels
adaptivity_order = ['Low', 'Moderate', 'High']
colors = ['#99ff99', '#ffcc99', '#ff6666']  # Green for 'Low', Orange for 'Moderate', Red for 'High'

# Function to create comparative pie charts for 'Load-shedding' and 'Location' based on 'Adaptivity Level'
def comparative_pie_charts(data, colors, adaptivity_order):
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # Adjust for four pie charts
    
    # Mapping for 'Yes' and 'No' to 'Local' and 'Distant'
    location_mapping = {'Yes': 'Local', 'No': 'Distant'}
    
    # Create pie charts for load shedding and location conditions
    for i, condition in enumerate(['Low', 'High']):
        for j, loc in enumerate(['Yes', 'No']):
            idx = 2 * i + j
            filtered_data = data[(data['Load-shedding'] == condition) & (data['Location'] == loc)]
            adaptivity_counts = filtered_data['Adaptivity Level (Predicted)'].value_counts(normalize=True).reindex(adaptivity_order, fill_value=0)
            axes[idx].pie(adaptivity_counts, colors=colors, autopct='%1.1f%%', startangle=90)
            location_label = location_mapping[loc]
            axes[idx].set_title(f'{condition} Load-shedding & {location_label} Location', fontsize=14)

    # Add a legend
    plt.figlegend(['Low Adaptivity', 'Moderate Adaptivity', 'High Adaptivity'], loc='lower center', ncol=3, fontsize=14)
    plt.tight_layout(rect=[0, 0.1, 1, 0.95])  # Adjust layout to make space for legend at the bottom
    plt.show()

# Call the function to create comparative pie charts
comparative_pie_charts(data, colors, adaptivity_order)
