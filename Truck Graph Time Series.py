import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a DataFrame with fake data
np.random.seed(0)  # For reproducibility
date_range = pd.date_range(start='2024-01-01', end='2024-08-31', freq='W')
qty = np.random.randint(50, 200, size=len(date_range))

data = pd.DataFrame({
    'Date': date_range,
    'Insurance Quantity': qty
})

# Create the Seaborn lineplot
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='Date', y='Insurance Quantity', marker='o', color='cyan', linewidth=2, markersize=8)

# Customize the plot
plt.title('Trucking Insurance Quantity Over Time', color='white', fontsize=16, fontweight='bold')
plt.xlabel('Date', color='white', fontsize=14, fontweight='bold')
plt.ylabel('Insurance Quantity', color='white', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, color='white', fontsize=12)
plt.yticks(color='white', fontsize=12)

# Set the background color
plt.gcf().patch.set_facecolor('#2b3d47')  # Figure background color
plt.gca().set_facecolor('#2b3d47')       # Plot area background color

# Remove grid lines
plt.grid(False)

# Show the plot
plt.tight_layout()
plt.show()
