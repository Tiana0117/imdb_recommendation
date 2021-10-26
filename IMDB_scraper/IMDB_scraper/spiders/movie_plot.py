from plotly import express as px
from matplotlib import pyplot as plt
from plotly.io import write_html


# we want to extract the first 10 lines of the dataframe to prepare for the plot.



df_plot = df_recommend.head(10)


# Then, we create the scatterplot with the dataframe `df_plot`. The `color` depends on the `number of shared actors`.


fig = px.scatter(df_plot,
                 x = "movie_or_TV_name",
                 y = "number of shared actors", 
                 color = "number of shared actors",
                 color_continuous_midpoint = 0,
                 title = "Scatterplot visualizing movies with shared actors")
    
write_html(fig, "movie_scatter.html")

