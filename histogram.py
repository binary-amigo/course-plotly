import plotly.graph_objects as go
import pandas as pd

# Sample data - replace with your actual data
data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [4200, 3800, 5100, 4700]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create custom colors for each region
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red

# Create the figure
fig = go.Figure()

# Add bars
fig.add_trace(go.Bar(
    x=df['Region'],
    y=df['Sales'],
    marker_color=colors,
    text=df['Sales'],  # Add sales values on top of bars
    textposition='auto',
))

# Update layout
fig.update_layout(
    title={
        'text': 'Regional Sales Distribution',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Region',
    yaxis_title='Sales',
    template='plotly_white',
    width=800,
    height=500,
    showlegend=False,
    yaxis=dict(
        tickformat=',.0f'  # Format y-axis ticks without decimal places
    ),
    # Add hover template
    hovermode='x unified'
)

# Show the plot
fig.show()

# Optional: Save the plot as HTML
# fig.write_html("regional_sales.html")