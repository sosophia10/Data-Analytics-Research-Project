# Load necessary libraries
library(ggplot2)
library(reshape2)
library(RColorBrewer)

# Read the data
data <- read.csv("students_adaptability_level_online_education.csv")

# Convert all factor-able columns to factors and then to numeric
data$Institution.Type <- as.numeric(as.factor(data$Institution.Type))
data$Financial.Condition <- as.numeric(as.factor(data$Financial.Condition))
data$Internet.Type <- as.numeric(as.factor(data$Internet.Type))
data$Network.Type <- as.numeric(as.factor(data$Network.Type))
data$Device <- as.numeric(as.factor(data$Device))
data$Load.shedding <- as.numeric(as.factor(data$Load.shedding))
data$Class.Duration..Hours.Per.Week. <- as.numeric(as.factor(data$Class.Duration..Hours.Per.Week.))
data$Location <- as.numeric(as.factor(data$Location))
data$IT.Student <- as.numeric(as.factor(data$IT.Student))
data$Self.Lms <- as.numeric(as.factor(data$Self.Lms))
data$Gender <- as.numeric(as.factor(data$Gender))
data$Education.Level <- as.numeric(as.factor(data$Education.Level))
data$Age.Range <- as.numeric(as.factor(data$Age.Range))
data$Adaptivity.Level..Predicted. <- as.factor(data$Adaptivity.Level..Predicted.)

# Separate the data based on Adaptivity Level
data_low <- subset(data, Adaptivity.Level..Predicted. == "Low")
data_moderate <- subset(data, Adaptivity.Level..Predicted. == "Moderate")
data_high <- subset(data, Adaptivity.Level..Predicted. == "High")

# Function to create and plot correlation matrix heatmap
plot_correlation_heatmap <- function(data, level) {
  # Select only the columns with numeric data
  numeric_data <- data[, sapply(data, is.numeric)]

  # Calculate correlation matrix
  correlations <- cor(numeric_data, use = "complete.obs")

  # Melt the correlation matrix
  melted_correlations <- melt(correlations)

  custom_colors <- c('#ff6666', '#ffcc99', '#99ff99')

  # Create a ggplot heatmap with custom colors
  heatmap <- ggplot(data = melted_correlations, aes(Var1, Var2, fill = value)) +
    geom_tile() +
    scale_fill_gradientn(colors = custom_colors, values = scales::rescale(c(-1, 0, 1)),
                         name="Pearson\nCorrelation") +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, vjust = 1, size = 12, hjust = 1),
          axis.text.y = element_text(size = 12)) +
    labs(x = '', y = '', title = paste("Correlation Heatmap of Adaptivity Factors (", level, ")", sep = "")) +
    coord_fixed()


  print(heatmap)
}


plot_correlation_heatmap(data_low, "Low")
plot_correlation_heatmap(data_moderate, "Moderate")
plot_correlation_heatmap(data_high, "High")



