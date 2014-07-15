from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def bob_line(bob,length,n):
    fd(bob,length)
    lt(bob,n)

def first_try(f,bob,length,n):
    for i in range(45):
        f(bob,length,n)

def second_try(f,bob,length,n):
    lt(bob,135)
    for i in range(45):
        f(bob,length,n)
        
def one_clover():
    first_try(bob_line,bob,4,1)
    second_try(bob_line,bob,4,1)
    lt(bob,180)

for i in range(8):
    one_clover()

wait_for_user()
        
