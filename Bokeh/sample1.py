from bokeh.plotting import figure, output_file, show

output_file("demo.html")
p = figure(plot_width=400, plot_height=400, title='Line Example')

x = [1,2,3,4,5]
y = [6,7,8,9,10]

p.line(x,y,line_width=2)

show(p)