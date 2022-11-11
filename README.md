# zappa-layer
A tool for managing AWS Lambda layers for Zappa
[![Downloads](https://pepy.tech/badge/zappa-layer)](https://pepy.tech/project/zappa-layer)

https://pypi.org/project/zappa-layer/

## Installation
```
pip install zappa-layer
```

## Usage
```
$ layer_manage -h
Usage: layer_manage.py [OPTIONS] COMMAND [ARGS]...

  Manage layers for zappadock

Options:
  --help  Show this message and exit.

Available subcommands:
  
  [package]
     checkpkgs           Check packages in venv
     installpkgs         Install packages in venv (default: in layer)
  
  [layer]
     makelayer           Make layer.zip from zappa-layer-venv
     publishlayer        Publish layer to AWS
     updatezappalayer    Update zappa_settings.json with layer ARN
  
  [allinone]
     allinone            Execute all commands with one command
     no-update-allinone  Execute all commands, except updatelayer
```

## WIP...
