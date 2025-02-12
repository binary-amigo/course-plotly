import plotly.express as px

# Load gapminder dataset
df_bubble = px.data.gapminder()

# Create animated bubble chart
fig = px.scatter(df_bubble, 
                x="gdpPercap", 
                y="lifeExp",
                animation_frame="year", 
                animation_group="country",
                size="pop", 
                color="continent", 
                hover_name="country",
                log_x=True, 
                size_max=55,
                title='GDP vs Life Expectancy Over Time')

fig.update_layout(
    template='plotly_white',
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[dict(label="Play",
                     method="animate",
                     args=[None, {"frame": {"duration": 500, "redraw": True},
                                "fromcurrent": True}]),
                dict(label="Pause",
                     method="animate",
                     args=[[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}])])])

# Show the plot
fig.show()