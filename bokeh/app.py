# demo for bokeh dashboard 
from bokeh.plotting import figure
from bokeh.models import Dropdown
from bokeh.layouts import column
from bokeh.io import curdoc

# Generate our cimple 'stock' trends
T = [t for t in range(0, 100)]
S1 = [t for t in T]
S2 = [-t for t in T]

p = figure(x_range=(min(T), max(T)), y_range=(min(S2), max(S1)), title="Simple Stock Trends")

def select_stock(event):
    if event.item == "S1":
        ds.data["y"] = S1
    elif event.item == "S2":
        ds.data["y"] = S2
    else: 
        raise Exception("Unknown stock")
    ds.trigger('data', ds.data, ds.data)


r = p.line(T, S1, color="blue")
ds = r.data_source
menu = [("Stock 1", "S1"), ("Stock 2", "S2")]
dropdown = Dropdown(label="Select Stock Trend", menu=menu)
dropdown.on_event('menu_item_click', select_stock)

curdoc().add_root(column(p,dropdown))
# run with: bokeh serve app.py


