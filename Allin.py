import Cam
import solve
import cube
import optimize
import ConnectArduino
import random
from string import maketrans
# colormap = "WYGRBO"
# posmap = "UDLFRB"
# trans = maketrans(colormap, posmap)
typ = input("1: camera, 2: key \n")
if (typ == 1):
	color = Cam.open()
elif (typ == 3):
	rnd = []
	for i in range(15):
		rnd.append(random.choice(['B', 'U', 'D', 'R', 'L', 'F']))
	res = ' '.join(rnd)
	print res
	ConnectArduino.Encoder().send(res)
else:
	color = raw_input("input \n")
# color = color.translate(trans)
print color
c = cube.Cube(color)
print "Solving:\n", c
orig = cube.Cube(c)
solver = solve.Solver(c)
solver.solve()

print "%s moves: " % len(solver.moves)
print " ".join(solver.moves)
opt = optimize.optimize_moves(solver.moves)
print "optimize"
moves = " ".join(opt)
print moves

print "arduino"
ConnectArduino.Encoder().send(moves)

#RRGRWYOOYWGWBGBRGWOWBBGWGRBYBWOOWYRRYRGWOYOOOGBRYYBBYG