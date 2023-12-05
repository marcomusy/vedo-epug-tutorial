from vedo import *

# Gene expression data
gene_data = np.load('../data/sox9_data/gene_data.npy')

# Read mesh vertices and faces
verts = np.load('../data/sox9_data/mesh_nodes.npy')
faces = np.load('../data/sox9_data/mesh_faces.npy')

############## Create the mesh 
msh = Mesh([verts, faces]).linewidth(1)
show(msh, bg="#282a36", zoom='tight').close()

############## Adding random scalar values
n = faces.shape[0] # number of faces
values = np.random.random(n)
msh.celldata["fake_data"] = values
msh.cmap("viridis")
show(msh, bg="#282a36", zoom='tight').close()

############## Adding real gene expression data
msh.celldata["gene_data"] = gene_data
msh.cmap("viridis")
print(msh)
show(msh, bg="#282a36", zoom='tight').close()
