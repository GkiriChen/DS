# Python Data

## Installation

We are going to install our environment for usage both for executing python modules, and for an easy way to attach your virtual environment as a Jupyter kernel to your Jupyter Notebook instance.
There are a lot of ways to create a virtual environment with a Jupyter Notebook instance. Below, a few ways are presented, and you can select whichever one works for you and your project.

### conda

[Conda usage manual](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-python.html)

#### Benefits
- Allows you to manage environments on instances as a non-root user (if local admin rights are missing)
- Allows you to select the Python version to be installed in your environment during the environment initialization, without the need to install this Python version beforehand
- Supports C++ modules

#### Prerequisites
- `conda` tool has to be installed in your user via a distribution, e.g. [miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)
- The root directory should contain a `requirements.txt` file with the list of dependencies

#### Usage
```
conda create -n python_data_env python=3.11
conda activate python_data_env

pip install -r requirements.txt  # should include `jupyter` or `notebook` as a dependency

jupyter notebook
```

### pipenv
[Pipenv on PyPI](https://pypi.org/project/pipenv/)

#### Benefits
- Automatic update of the dependency list in the `Pipenv` file after installing a new package from the command line
- Easy management of the versions of the virtual environment with the `lock` file

#### Prerequisites
- `pipenv` tool has to be installed in your user, a convenient way is via PyPI: `pip install pipenv`
- The root directory should contain a `requirements.txt` file with the list of dependencies

#### Usage
```
pipenv install -r requirements.txt  # should include `jupyter` or `notebook` as a dependency
pipenv shell

pipenv run jupyter notebook
```

### poetry
[Poetry on PyPI](https://pypi.org/project/poetry/)

#### Benefits
- Easy management of the versions of the virtual environment with the `lock` file
- Multifunctional tool, having additional features relevant especially for production software and deployment, like separation of core, dev, other types dependencies; specifying special commands and entrypoints for the application; etc.

#### Prerequisites
- `poetry` tool installed globally, a convenient way is via PyPI: `pip install poetry`
- The root directory should contain a `pyproject.toml` file with the list of dependencies and other configuration

#### Usage
```
poetry install
poetry shell

poetry run jupyter notebook
```
