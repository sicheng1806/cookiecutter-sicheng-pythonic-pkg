# cookiecutter-sicheng-pythonic-pkg

一个使用 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 工具生成 Python 工程化项目的模板。

- 文档: https://cookiecutter-sicheng-pythonic-pkg.readthedocs.io/en/latest/
- GitHub: https://github.com/sicheng1806/cookiecutter-sicheng-pythonic-pkg

## 特性

- 使用[uv](https://github.com/astral-sh/uv)作为项目虚拟环境管理工具
- 配置`GitHub Actions`
- 使用[ruff](https://github.com/astral-sh/ruff)作为格式风格审查工具
- 使用[pytest](https://github.com/pytest-dev/pytest)作为测试框架
- 使用[sphinx](https://github.com/sphinx-doc/sphinx)作为文档生成工具
- 使用[pre-commit](https://github.com/pre-commit/pre-commit)配置`git commit`执行前的自动化审查脚本
- 使用[nox](https://github.com/wntrblm/nox)作为自动化工具，并配置代码风格审查、测试、文档构建脚本
- 使用[typos](https://github.com/crate-ci/typos)作为源代码拼写错误检查工具

工具的具体使用方法可以查看模板内的[development.md](docs/development.md) 文档。

## 如何使用

1. 安装[cookiecutter](https://github.com/cookiecutter/cookiecutter)
2. 使用模板:
```bash
cookiecutter https://github.com/sicheng1806/cookiecutter-sicheng-pythonic-pkg
```

## 项目结构

```text
my_project/
├── docs
│   ├── conf.py
│   ├── development.md
│   ├── doc_requirements.txt
│   ├── index.md
│   ├── _static
│   └── _templates
├── LICENSE
├── noxfile.py
├── pyproject.toml
├── README.md
├── src
│   └── my_project
│       └── __init__.py
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── settings.yml
    └── test_version.py
```

## 使用项目

具体查看[development.md](docs/development.md)或者查看项目内`docs/development.md`文档。
