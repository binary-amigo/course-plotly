import plotly.graph_objects as go

# Create gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=420,
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Performance Score", 'font': {'size': 24}},
    delta={'reference': 400, 'increasing': {'color': "RebeccaPurple"}},
    gauge={
        'axis': {'range': [None, 500], 'tickwidth': 1},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 250], 'color': 'cyan'},
            {'range': [250, 400], 'color': 'royalblue'}
        ],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 490
        }
    }
))

fig.update_layout(
    template='plotly_white',
    width=600,
    height=400
)

# Show the plot
fig.show()