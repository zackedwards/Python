from bokeh.plotting import figure, output_file, show

output_file("demo.html")

p = figure(plot_width=400, plot_height=400, title='Scattered Chart Example')

x = [1,2,3,4,5]
y = [6,7,8,9,2]

p.circle(x,y,size=15, line_color='red', fill_color='orange', fill_alpha=0.5)

show(p)