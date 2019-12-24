# necessary imports
import numpy as np
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.plotting import ColumnDataSource
from bokeh.layouts import row
from bokeh.models import Select

# import the data into Pandas DataFrame
data = pd.read_csv('../data/literacy_birth_rate.csv')

# read necessary columns into variables (Pandas Series)
fertility = data['fertility']
female_literacy = data['female_literacy']
population = data['population'] / 1000000 # this is converted into millions

# Create ColumnDataSource: source
source = ColumnDataSource(data={'x' : fertility,
                                'y' : female_literacy})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy',
    # update 'y' to female_literacy
    if new == 'female_literacy':
        source.data = {
            'x' : fertility,
            'y' : female_literacy
        }
        
     # Else, update 'y' to population
    else:
        source.data = {
            'x' : fertility,
            'y' : population
        }
        
# Create a dropdown Select widget: select    
select = Select(title='distribution', options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)