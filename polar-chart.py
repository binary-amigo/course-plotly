import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Generate sample wind data
directions = np.arange(0, 360, 30)
frequencies = np.random.randint(10, 50, size=len(directions))

# Create polar chart
fig = go.Figure(data=go.Scatterpolar(
    r=frequencies,
    theta=directions,
    mode='lines+markers',
    name='Wind Pattern',
    fill='toself',
    line=dict(color='darkblue', width=2),
    marker=dict(color='royalblue', size=8)
))

fig.update_layout(
    title='Wind Direction Distribution',
    template='plotly_white',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, max(frequencies)]
        ),
        angularaxis=dict(
            direction="clockwise",
            period=360
        )
    ),
    showlegend=False,
    width=700,
    height=700
)

# Show the plot
fig.show()