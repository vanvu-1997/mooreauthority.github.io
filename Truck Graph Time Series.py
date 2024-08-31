import plotly.graph_objects as go
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

# Create the Plotly line plot
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=data['Date'],
    y=data['Insurance Quantity'],
    mode='lines+markers',
    line=dict(color='cyan', width=2),
    marker=dict(size=8),
    name='Insurance Quantity'
))

# Customize the plot
fig.update_layout(
    title='Trucking Insurance Quantity Over Time',
    title_font=dict(color='white', size=16, family='Arial Black'),
    xaxis_title='Date',
    yaxis_title='Insurance Quantity',
    xaxis_title_font=dict(color='white', size=14, family='Arial Black'),
    yaxis_title_font=dict(color='white', size=14, family='Arial Black'),
    xaxis=dict(
        tickangle=45,
        tickfont=dict(color='white', size=12),
        gridcolor='rgba(0,0,0,0)',  # Remove x-axis grid lines
        showgrid=False,             # Hide x-axis grid lines
        showline=True,              # Show x-axis line
        linecolor='white',          # Color of x-axis line
        linewidth=2                 # Width of x-axis line
    ),
    yaxis=dict(
        tickfont=dict(color='white', size=12),
        gridcolor='rgba(0,0,0,0)',  # Remove y-axis grid lines
        showgrid=False,             # Hide y-axis grid lines
        showline=True,              # Show y-axis line
        linecolor='white',          # Color of y-axis line
        linewidth=2                 # Width of y-axis line
    ),
    plot_bgcolor='#2b3d47',
    paper_bgcolor='#2b3d47'
)

# Save the plot as an HTML file
fig.write_html('insurance_quantity_plot.html')

# Optionally, you can also show the plot in the browser
fig.show()
