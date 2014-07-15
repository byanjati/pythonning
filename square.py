from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

def bob_line(bob,length,n):
    fd(bob,length)
    lt(bob,n)

def circle(f,bob,r,n):
    keliling = 2 * 3.14 * r;
    length = keliling / (360/n)
    for i in range(360/n):
        f(bob,length,n)
    wait_for_user()

circle(bob_line,bob,100,1)

#length 115 diameter , diameter lingkaran dengan draw length = 2 , dan putaran 2 derajat
#length 115 diameter , diameter lingkaran dengan draw length = 1 , 360 sisi , 1 derajat    

#circumferences = length * n kali berputar
#circumferences = keliling lingkaran = 2*phi*r
#jadi jika radius dimasukkan 7 , maka panjang circumferences dari lingkaran = 2*22 = 44
#dimana 44 = length * n kali berputar
