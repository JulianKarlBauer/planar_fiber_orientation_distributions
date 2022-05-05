[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/419436511.svg)](https://zenodo.org/badge/latestdoi/419436511)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/JulianKarlBauer/planar_fiber_orientation_distributions/HEAD)

<p align="center">
  <a href="https://github.com/JulianKarlBauer/planar_fiber_orientation_distributions">
  <img alt="PlanarFiberDist" src="logo/logo.png" width="20%">
  </a>
</p>

# PlanarFiberDist

This repository contains a Python package called `planarfiberdist`  
which contains selected contributions of the paper

```bibtex
@article{insertdoihere,
	author = {Julian Karl Bauer and Thomas Böhlke},
	title ={Fiber orientation distributions based on planar fiber orientation tensors of fourth order},
	journal = {Mathematics and Mechanics of Solids},
}
```

Please see [license][url_license],
[acknowledgment](#acknowledgment)
and cite the [paper given above][url_article] and the latest [Zenodo-DOI][url_latest_doi].

## Installation

### Install directly from github
```
python -m pip install git+https://github.com/JulianKarlBauer/planar_fiber_orientation_distributions.git
```

### Install from local clone
- [Clone][url_how_to_clone] this repository to your machine
- Open a terminal and navigate to your local clone
- Install the package from the local clone into the current [env][url_env_python]i[ronment][url_env_conda] in develop mode:
	```shell
	python setup.py develop
	```

Note: [Develop vs. install](https://stackoverflow.com/a/19048754/8935243)

## Examples

Rendered example notebooks and example scripts are given [here](examples/).

## Acknowledgment

The research documented in this repository has been funded by the
[German Research Foundation (DFG, Deutsche Forschungsgemeinschaft)][dfg_website] - project number [255730231][dfg_project].
The support by the German Research Foundation within the International Research Training Group
[“Integrated engineering of continuous-discontinuous long fiber reinforced polymer structures“ (GRK 2078)][grk_website]
is gratefully acknowledged.

[grk_website]: https://www.grk2078.kit.edu/
[dfg_website]: https://www.dfg.de/
[dfg_project]: https://gepris.dfg.de/gepris/projekt/255730231

[url_license]: LICENSE
[url_latest_doi]: ??
[url_article]: ??
[url_how_to_clone]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

[url_env_python]: https://docs.python.org/3/tutorial/venv.html
[url_env_conda]: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
