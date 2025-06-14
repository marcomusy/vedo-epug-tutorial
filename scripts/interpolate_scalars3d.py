import numpy as np
from vedo import dataurl, Mesh, Points, show
from vedo.pyplot import plot

# Load an example mesh of a mouse limb at 12 days of development
msh = Mesh(dataurl + "290.vtk")

# The 100 points where we measured the value of gene expression
ids = np.random.randint(0, msh.npoints, 100)
pts = msh.vertices[ids]        # slice the numpy array
x = pts[:, 0]                  # x coordinates of the points
gene = np.sin((x+150)/500)**2  # we are making this up!

# Create a set of points with those values
points = Points(pts, r=10)
points.cmap("Greens", gene, name="Hoxa11")

# Interpolate the gene data onto the mesh, by averaging the 5 closest points
msh.interpolate_data_from(points, n=5).cmap("Greens").add_scalarbar()
print(msh)

# Create a graph of the gene expression as function of x-position
gene_plot = plot(x, gene, lw=0, title="Gene expression").clone2d(size=0.75)

# Show the mesh, the points and the graph
show(msh, points, gene_plot).close()
