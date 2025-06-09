from vedo import *

points = np.random.rand(2000, 3)

pts = Points(points)
pln = Plane(pos=(0.5, 0.5, 0.6), normal=(1, 0, 0), s=(1.5, 1.5))
pln.alpha(0.5).lw(1)
show(pts, pln, axes=1).close()

pts = Points(points)
pts.cut_with_plane((0.5, 0.5, 0.6))
pts.pointdata['myscalar'] = pts.coordinates[:,0]**2
pts.cmap("coolwarm").add_scalarbar("My Scalar")
pts.point_size(10)

show(pts, pln, axes=1).close()
