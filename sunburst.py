import plotly.express as px

# Load sample data
df_sunburst = px.data.tips()

# Create sunburst chart
fig = px.sunburst(
    df_sunburst, 
    path=['day', 'time', 'sex'], 
    values='total_bill',
    title='Restaurant Tips Analysis',
    color='total_bill',
    color_continuous_scale='RdBu'
)

fig.update_layout(
    template='plotly_white',
    width=800,
    height=800
)

# Show the plot
fig.show()