
# Required libraries
library(ggplot2)
library(reshape2) # For melt function

# Read the data
data <- read.csv("students_adaptability_level_online_education.csv")

# Print the actual column names to help ensure accuracy
print(colnames(data))

# Define the columns to analyze with the exact names from the dataset
columns_to_analyze <- c("Self.Lms", "Class.Duration..Hours.Per.Week.", "IT.Student",
                        "Financial.Condition", "Institution.Type", "Location")

# Convert columns to factors
data[columns_to_analyze] <- lapply(data[columns_to_analyze], factor)
data$`Adaptivity.Level..Predicted.` <- factor(data$`Adaptivity.Level..Predicted.`)

# Function to create and save heatmap for each specified column
create_and_save_heatmap <- function(column_name) {
  # Set the levels for the 'Adaptivity Level' factor in the desired order
  data$`Adaptivity.Level..Predicted.` <- factor(data$`Adaptivity.Level..Predicted.`, levels = c("Low", "Moderate", "High"))
  
  # Create a contingency table for the column and Adaptivity Level
  table_data <- table(data[[column_name]], data$`Adaptivity.Level..Predicted.`)
  
  # Calculate the proportions for the heatmap
  proportions_data <- prop.table(table_data, 1)
  
  # Melt the proportions table for use in ggplot
  melted_data <- melt(proportions_data)
  
  # Define color palette
  colors <- c("#ff6666", "#ffcc99", "#99ff99")
  
  # Plot the heatmap with the proportion values on each cell
  p <- ggplot(melted_data, aes(x = Var2, y = Var1, fill = value)) +
    geom_tile(color = "black", size = 0.1) + # Adjust the size of the boxes with the 'size' argument
    geom_text(aes(label = sprintf("%.2f", value)), vjust = 1.5, color = "black", size = 3) + # Adjust text size
    scale_fill_gradientn(colors = colors) +
    labs(x = "Adaptivity Level", y = column_name, fill = "Proportion") +
    ggtitle(paste("Heatmap of", column_name, "by Adaptivity Level")) +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 10), # Adjust text size
          axis.text.y = element_text(size = 10), # Adjust text size
          axis.title = element_text(size = 12), # Adjust title size
          plot.title = element_text(size = 14, hjust = 0.5), # Adjust plot title size
          plot.margin = margin(5, 5, 5, 5)) # Adjust the plot margins if necessary
  
  # Save the plot to a file
  ggsave(paste0(column_name, "_adaptivity_heatmap.png"), plot = p, width = 8, height = 6, dpi = 300) # Adjust the dimensions as necessary
}

# Apply the function to each column
lapply(columns_to_analyze, create_and_save_heatmap)
