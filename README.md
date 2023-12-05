# The EMBL Python User Group Session on vedo

A python module for scientific analysis of 3D objects and point clouds.

Link to the EPUG activities [here](https://git.embl.de/grp-bio-it/EPUG).


## Setup and Run
```sh
pip install -U vedo
pip install scipy
```

Copy this repo locally with:
```
git clone https://github.com//vedo-epug-tutorial.git
cd vedo-epug-tutorial
```

To run the scripts:
```
cd scripts
python 01-vis_serie.py
```

For the notebooks use the software you are more comfortable with. 
In case you have never used any, we commend using `jupyter-lab`.
- [Installation with conda](https://jupyterlab.readthedocs.io/en/latest/getting_started/installation.html#conda)

To start the notebooks: `jupyter lab`

Inside the notebook you may want to declare the preferred backend to use, e.g.:
```py
from vedo import settings
settings.default_backend = "vtk"
```

## Documentation
- [vedo webpage](https://vedo.embl.es/)
- [vedo API docs](https://vedo.embl.es/docs/)
