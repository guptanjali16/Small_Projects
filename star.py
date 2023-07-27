import turtle
bob=turtle.Turtle()
bob.getscreen().bgcolor("red")

bob.color("white")
def star(turtle,size):
    if size<=10:
        return
    else:
     for i in range(5):
      turtle.forward(size)
      star(turtle,size/2)
      turtle.left(216)

star(bob ,300)
 

turtle.done()
