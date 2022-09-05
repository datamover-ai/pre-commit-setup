# pre-commit-setup
----------------------------------------------------------------
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

load conda environment


```shell
conda create --name my-env python=3.9 --file=environment.yml
```

Install the git hook scripts
```shell
pre-commit install
```

Run pre-commit against all the files
```shell
pre-commit run -–all-files
```

For more information about pre-commit check the [documentation](https://pre-commit.com).
