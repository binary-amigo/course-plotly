import plotly.express as px
import pandas as pd

# Sample sales data for different countries
data = {
    "Country": ["United States", "Canada", "Brazil", "United Kingdom", "Germany", 
                "France", "India", "China", "Japan", "Australia"],
    "Sales": [5000, 3000, 4200, 3500, 4800, 4700, 6000, 8000, 4500, 3200]
}

df = pd.DataFrame(data)

# Create choropleth heatmap
fig = px.choropleth(df, 
                     locations="Country", 
                     locationmode="country names", 
                     color="Sales", 
                     color_continuous_scale="Viridis",
                     title="Global Sales Distribution")

# Show the figure
fig.show()
