from bokeh.plotting import figure, output_file, show

output_file("demo.html")

x = [1,2,3]
y = [1,2,3]

p = figure(width=300, height=300)
p.wedge(x, y, radius=15, start_angle=0.6, end_angle=4.1, radius_units="screen", color="#2b8cbe")

show(p)
