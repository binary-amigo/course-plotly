import plotly.express as px
import pandas as pd
import numpy as np

# Generate sample data
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
values = np.random.normal(100, 15, len(dates))
df = pd.DataFrame({
    'date': dates,
    'value': values
})

# Create line chart
fig = px.line(df, x='date', y='value',
              title='Time Series with Range Selector')

fig.update_layout(
    template='plotly_dark',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(step="all")
            ])
        )
    )
)

# Show the plot
fig.show()