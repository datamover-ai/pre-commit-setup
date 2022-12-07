# 📕 pre-commit-setup
----------------------------------------------------------------
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

After cloning the repo in your machine, load the conda environment
```shell
conda create --name my-env python=3.9 --file=environment.yml
```

Once the environment is installed, activate it via:
```shell
conda activate my-env
```

Install the git hook scripts
```shell
pre-commit install
```

You can read more about the pre-commit and its usage on this ![article](https://www.datamover.ai/post/boost-your-coding-productivity-with-this-tool)
