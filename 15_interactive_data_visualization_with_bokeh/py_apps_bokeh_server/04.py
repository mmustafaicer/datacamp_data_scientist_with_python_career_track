# necessary imports
import numpy as np
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider

# create x and y variables that are used in question
x = np.linspace(0,10,300)
y = np.sin(1/x)

# create figure object
plot = figure()

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x': x, 'y': y})

# Add a line to the plot
plot.line('x', 'y', source=source)

# create slider
slider = Slider(title='slider1', start=1, end=10, step=1, value=1)

# Create a column layout: layout
layout = column(widgetbox(slider), plot)

# Add the layout to the current document
curdoc().add_root(layout)