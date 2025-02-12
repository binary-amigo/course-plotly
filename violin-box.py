import plotly.express as px
import plotly.graph_objects as go

# Load sample data
df_violin = px.data.tips()

# Create violin plot with box plot
fig = go.Figure()

days = df_violin['day'].unique()
colors = ['rgb(67,67,167)', 'rgb(115,115,192)', 'rgb(49,130,189)', 'rgb(189,189,189)']

for day, color in zip(days, colors):
    fig.add_trace(go.Violin(
        x=df_violin['day'][df_violin['day']==day],
        y=df_violin['total_bill'][df_violin['day']==day],
        name=day,
        box_visible=True,
        meanline_visible=True,
        fillcolor=color,
        opacity=0.6,
        line=dict(color='black'),
        points='all',
        jitter=0.05,
        box=dict(
            visible=True,
            width=0.15,
            fillcolor='white',
            line=dict(color='black')
        ),
        meanline=dict(color='black')
    ))

fig.update_layout(
    title='Distribution of Bills by Day',
    xaxis_title='Day',
    yaxis_title='Total Bill',
    template='plotly_dark',
    width=800,
    height=600,
    showlegend=False
)

# Show the plot
fig.show()