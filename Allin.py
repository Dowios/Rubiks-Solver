import Camera
import solve
import cube
import optimize
import ConnectArduino
from string import maketrans
# colormap = "WYGRBO"
# posmap = "UDLFRB"
# trans = maketrans(colormap, posmap)
typ = input("1: camera, 2: key \n")
if (typ == 1):
	color = Camera.open()
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