[![License BSD-3](https://img.shields.io/pypi/l/napari-seedseg.svg?color=green)](https://github.com/rezaakb/napari-seedseg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-seedseg.svg?color=green)](https://pypi.org/project/napari-seedseg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-seedseg.svg?color=green)](https://python.org)
[![tests](https://github.com/rezaakb/napari-seedseg/workflows/tests/badge.svg)](https://github.com/rezaakb/napari-seedseg/actions)
[![codecov](https://codecov.io/gh/rezaakb/napari-seedseg/branch/main/graph/badge.svg)](https://codecov.io/gh/rezaakb/napari-seedseg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-seedseg)](https://napari-hub.org/plugins/napari-seedseg)

# napari-seedseg

A simple plugin for 2D medical image segmentation. In this project, we are trying to use Flood method for segmentation. 
Flood segmentation, also known as flood fill or region growing, is an image segmentation technique that starts from a seed point and expands to neighboring pixels with similar properties (e.g., intensity, color). In our project, you only can segment one label at the time. Also, please open **2D greyscale** image. Below is a description of the repository's structure and the purpose of each file:

    .
    ├── setup.cfg              # package metadata
    ├── pyproject.toml         # use setuptools
    ├── src/napari_seedseg     
    │   ├── napari.yaml        # Load and stress tests
    │   ├── __init.py__        # Python package metadata files
    |   ├── _widget.py         # Widget contributions
    │   ├── _layers.py         # Layers contributions
    │   ├── _method.py         # Method contributions
    │   └── _test              # Test cases
    └── ...

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Demo

![Demo](https://drive.google.com/uc?export=view&id=1nJypKACvoIUdtM5nlton5NlmCVDFupu7)

## Installation

First, install `napari`:

    pip install "napari[all]"
    

You can install `napari-seedseg` via [pip]:

    pip install napari-seedseg
    

Alternatively, to install latest development version:

    pip install git+https://github.com/rezaakb/napari-seedseg.git

## Quick Start

1. Launch napari and open the image you want to segment. Please note that the plugin only supports 2D Greyscale images. You can select sample images in this path `File -> Open Sample -> napari -> Cell`.
2. Go to the `Plugins` menu and select the `napari-seedseg: SeedSeg`.
3. In the segmentation plugin window, after selecting image layer, please select the desired tolerance level and click `Confirm` to initialize contour and segmentation layers, and the method with given tolerance. **Note:** If the `Confirm` buttom is disabled, it means the dimention of image is not eqaul to 2.
4. Now, you can move your mouse over the image to visualize the segments. **Note:** You should be in the `Segmentation Layer`.
5. Double click on each segment to add it to the `Segmentation Layer`. 
6. To refine the segmentation, repeat step 3 and adjust the tolerance level as needed.

## Packages
In this project, we have used these packages:

    numpy
    magicgui
    qtpy
    opencv-python-headless
    scikit-image>=0.19.3



## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-seedseg" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/rezaakb/napari-seedseg/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
