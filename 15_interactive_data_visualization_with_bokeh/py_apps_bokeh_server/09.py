# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.io import curdoc
from bokeh.models import CheckboxGroup, RadioGroup, Toggle
from bokeh.layouts import widgetbox

# Add a Toggle: toggle
toggle = Toggle(button_type='success', label='Toggle button')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(labels=['Option 1', 'Option 2', 'Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
curdoc().add_root(widgetbox(toggle, checkbox, radio))