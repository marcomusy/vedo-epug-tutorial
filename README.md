# Summer School on Computational Modelling of Multicellular Systems

A python module for scientific analysis of 3D objects and point clouds


## Setup

```sh
pip install -U vedo
pip install scipy
```

Copy this repo locally:
```
git clone https://github.com//vedo-epug-tutorial.git
cd vedo-epug-tutorial
```

## Documentation
- [vedo webpage](https://vedo.embl.es/)
- [vedo API docs](https://vedo.embl.es/docs/)

## Run
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
