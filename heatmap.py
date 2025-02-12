import plotly.graph_objects as go
import numpy as np

# Generate sample correlation data
np.random.seed(42)
size = 8
corr_matrix = np.random.rand(size, size)
corr_matrix = (corr_matrix + corr_matrix.T) / 2  # Make it symmetric
np.fill_diagonal(corr_matrix, 1)  # Set diagonal to 1

# Create labels
labels = ['Var ' + str(i+1) for i in range(size)]

# Create heatmap
fig = go.Figure(data=go.Heatmap(
    z=corr_matrix,
    x=labels,
    y=labels,
    colorscale='RdBu_r',
    zmid=0.5,
    text=np.round(corr_matrix, 2),
    texttemplate='%{text}',
    textfont={"size": 10},
    hoverongaps=False
))

fig.update_layout(
    title='Correlation Heatmap',
    template='plotly_white',
    width=700,
    height=700
)

# Show the plot
fig.show()