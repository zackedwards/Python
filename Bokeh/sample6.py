from bokeh.plotting import figure, output_file, show

output_file('polli.html')

x = [1,2,3]
y = [1,2,3]

p = figure(width=400, height=400)
p.oval(x, y, width=0.2, height=0.4, angle=-0.7, color="#1D91C0")

show(p)
