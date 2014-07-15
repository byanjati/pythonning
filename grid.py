def print_line():
	print '+',
	print '- '*4,
	print '+',
	print '- '*4,
	print '+'

def print_underline():
	print '|',
	print ' '*8,
	print '|',
	print ' '*8,
	print '|'

def do_twice(f):
	f()
	f()

def do_four(f1,f2):
	f1(f2)
	f1(f2)

def print_grid(f1,f2,f3,f4):
	f1()
	f2(f3,f4)
	f1()
	f2(f3,f4)
	f1()

print_grid(print_line,do_four,do_twice,print_underline)



