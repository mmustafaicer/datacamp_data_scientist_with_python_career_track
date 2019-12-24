# Perform necessary imports
from bokeh.plotting import figure
from bokeh.io import curdoc

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line(x=[1,2,3,4,5], y=[2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)