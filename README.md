# vedo tutorial for the EMBL Python User Group

A python module for scientific analysis of 3D objects and point clouds.


## Setup and Run
```sh
pip install -U vedo
pip install scipy
```

Copy this repo locally with:
```
git clone https://github.com/marcomusy/vedo-epug-tutorial.git
cd vedo-epug-tutorial
```

To run the scripts:
```
cd scripts
python 01-vis_serie.py
```

Inside jupyter notebooks you may want to declare the preferred backend to use, e.g.:
```py
from vedo import settings
settings.default_backend = "vtk"
```

## Documentation
- [vedo webpage](https://vedo.embl.es/)
- [vedo API docs](https://vedo.embl.es/docs/)
- [EPUG activities](https://git.embl.de/grp-bio-it/EPUG).
