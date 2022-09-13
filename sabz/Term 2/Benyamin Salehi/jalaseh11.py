from turtle import *
name = textinput("color", "Enter your name: ")
if name == "Benyamin":
    color = 'purple'
elif name =='Koorosh':
    color = 'orange'
elif name == 'Mohammad Mehrshad':
    color = 'red'
elif name == 'Ali':
    color = 'cyan'
elif name == "Mehrad":
    color = 'yellow'
elif name == 'Arad':
    color = 'green'
elif name == 'Parsa':
    color = 'blue'
else:
    color = 'black'
speed(0)
fillcolor(color)
begin_fill()
for i in range(6):
    circle(150)
    lt(60)
end_fill()
done()