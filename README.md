<h1 style="text-align: center;">BRAILS++RoofClassification:  Building Regional Asset Inventories at Large Scale</h1>

[![Tests](https://github.com/NHERI-SimCenter/BrailsPlusPlus/actions/workflows/tests.yml/badge.svg)](https://github.com/NHERI-SimCenter/BrailsPlusPlus/actions/workflows/tests.yml/badge.svg)
[![DOI](https://zenodo.org/badge/184673734.svg)](https://zenodo.org/badge/latestdoi/184673734)
[![PyPi version](https://badgen.net/pypi/v/BRAILS/)](https://pypi.org/project/BRAILS/)
[![PyPI download month](https://img.shields.io/pypi/dm/BRAILS.svg)](https://pypi.python.org/pypi/BRAILS/)

## What is it?

```BRAILS++RoofClassification``` is adapted from ```BRAILS++```, an object-oriented framework for building applications that focus on generating asset inventories for large geographic regions, to include roof classifications.

## How is the repo laid out?

+ ```brails```: A directory containing the classes
  - ```brails/types```: directory containing useful datatypes, e.g., ```ImageSet``` and ```AssetInventory```
  - ```brails/processors```: directory containing classes that do ```image_processing``` to make predictions, e.g. RoofShape
  - ```brails/scrapers```: directory containing classes that do internet downloads, e.g., footprint and image scrapers.
  - ```brails/filters```: directory containing image filters, e.g., classes that take images and revise or filter out unnecessary portions of images.
  - ```brails/imputers```: directory containing classes that fill in missing ```AssetInventory``` datasets, i.e., filling in features that are missing in certain Assets of the AssetInventory.
  - ```brails/inferers```: directory containing classes that infer new asset features based on existing features in the Assets of ```AssetInventory```.
  - ```brails/utils```: directory containing misc classes that do useful things, e.g. geometric conversions
+ ```examples```: A directory containing example scripts and Jupyter notebooks
+ ```tests```: A directory containing unit tests. The directory structure follows that of ```brails```

## Quick Links

- [Documentation & Guides](https://nheri-simcenter.github.io/BrailsPlusPlus/)

## Installation instructions

```shell
git clone https://github.com/noellelaw/BrailsPlusPlusRoofClassification
python -m pip install -e . 
```

## Acknowledgments

This work is based on https://github.com/NHERI-SimCenter/BrailsPlusPlus
