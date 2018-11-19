from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter
from bokeh.models import LinearAxis, Range1d

# prepare some data
x = [
datetime(2015,4,3),
datetime(2006,6,9),
datetime(2013,5,24),
datetime(2017,4,14),
datetime(2011,4,29),
datetime(2011,6,24),
datetime(2009,4,3),
datetime(2017,6,16),
datetime(2006,8,4),
datetime(2001,6,22),
datetime(2003,6,6),
datetime(2013,7,17),
datetime(1990,6,29),
datetime(1981,6,19),
datetime(2005,6,22),
datetime(2006,6,16),
datetime(2008,5,9),
datetime(2014,3,14),
datetime(2008,8,22),
datetime(2001,4,27)
]

y = [353007020, 244082982, 238679850, 226008385, 209837675, 191452396, 155064265, 152901115, 148213377,
     144533925 ,127154901, 83028128, 82670733, 72179579, 66023816, 62514415, 43945766, 43577636, 36316032, 32720065
]
y_rank = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# output to static HTML file
output_file("filmgross.html")

# create a new plot with a title and axis labels
p = figure( title="Gross of top Movies for Geners Car Racing", plot_width=800, x_axis_label='Time', y_axis_label='Grossing', 
            x_axis_type="datetime")

# Setting the second y axis range name and range
#p.extra_y_ranges = {"rank": Range1d(start=0, end=20)}

# Adding the second axis to the plot.  
#p.add_layout(LinearAxis(y_range_name="rank", axis_label="Rank"), 'right')

# add a line renderer with legend and line thickness
p.circle( x, y, color="red", size=20 )
#p.line(x, y_rank, legend="Rank", line_color="green", line_width=2, y_range_name="rank")
#p.line( x, y_rank, legend="Rank",line_color="blue", line_width=2 )

# use a formatter to display y-axis tick labels in million dollars
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")
#p.yaxis[1].formatter = NumeralTickFormatter(format="(0.0)")

# show the results
show(p)