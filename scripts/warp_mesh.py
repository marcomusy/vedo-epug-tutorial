"""Warp a mesh (non-linear registration).
All points stay fixed while a single point in space
moves as the arrow indicates."""
from vedo import dataurl, Mesh, Arrows, show

# Load a mesh
mesh = Mesh(dataurl + "man.vtk").color("white")

# Create a heavily decimated copy with about 200 points
# (to speed up the computation)
mesh_dec = mesh.clone().triangulate().decimate(n=200)
mesh_dec.color("red5").point_size(5) # show it as points

sources = [[0.9, 0.0, 0.2]]  # this point must move
targets = [[1.2, 0.0, 0.4]]  # ...to this.
for pt in mesh_dec.vertices:
    if pt[0] < 0.3:  # while these pts don't move
        sources.append(pt)  # (e.i. source = target)
        targets.append(pt)

# Create the arrows representing the displacement
arrow = Arrows(sources, targets)

# Make a copy of the mesh and warp it
mesh_warped = mesh.clone().warp(sources, targets)
mesh_warped.color("blue5").wireframe()

# Show the meshes and the arrow
show(mesh, mesh_dec, mesh_warped, arrow, __doc__, axes=1)
