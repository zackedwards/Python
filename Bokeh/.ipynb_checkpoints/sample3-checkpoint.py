from bokeh.plotting import figure, output_file, show

output_file("demo.html")

x = [1,2,3,4,5]
y = [5,6,7,8,9]

p = figure(plot_width=400, plot_height=400, title='DottedLine Chart Example')

p.line(x,y,line_width=2)

p.circle(x,y, fill_color='orange', size=6)

show(p)