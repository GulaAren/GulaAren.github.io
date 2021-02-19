---
layout: post
title: Basic Usage of Anaconda Environments
menutitle: Use of Anaconda Environments
kategori:
  - python
  - conda
  - jupiter
label:
  - conda
---


## Usage Introduction

Here is the very basic usages of [__Anaconda__](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) environments.


<!--more-->


#### Create New Conda Environment

Overriding `async def dispatch(request, call_next)` method.

```bash
$ conda env create YOUR_ENVIRONMENT_NAME
```

#### Get List of Anaconda Environments


```bash
$ conda env list
```

Result

```
base                  *  /home/gulaaren/anaconda
YOUR_ENVIRONMENT_NAME    /home/gulaaren/anaconda/envs/venv
```


#### Load Anaconda Environment

```bash
$ conda activate YOUR_ENVIRONMENT_NAME
```

#### Additional Note

Start Jupiter Lab

```bash
$ jupyter-lab

[I 22:34:13.194 LabApp] Jupyter Notebook 6.1.4 is running at:
[I 22:34:13.194 LabApp] http://localhost:8888/?token=YOUR_JUPITER_TOKEN
[I 22:34:13.194 LabApp]  or http://127.0.0.1:8888/?token=YOUR_JUPITER_TOKEN
```

then open the link on your browser.


#### Docs

 - [Conda cheat sheet](https://conda.io/projects/conda/en/latest/user-guide/cheatsheet.html)
