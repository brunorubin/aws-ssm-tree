# SSM Tree

SSM Tree is a tool that provides a tree visualization of the parameters hierarchy from AWS System Manager Parameter Store.

## Installation

SSM Tree can be installed using [pip](https://pip.pypa.io/en/stable/):

```bash
$ pip install aws-ssm-tree
```

## Example

![example](https://user-images.githubusercontent.com/2822509/52456988-751a1380-2bbc-11e9-9865-38761b394b8e.png)

### Usage

```
Usage: ssm-tree [OPTIONS]

  SSM Tree is a tool that provides a tree visualization of the parameters
  hierarchy from AWS System Manager Parameter Store.

Options:
  --path TEXT      The hierarchy for the parameter. Hierarchies start with a
                   forward slash (/) and end with the parameter name. Here is
                   an example of a hierarchy: /Servers/Prod  [required]
  -r, --recursive  Retrieve all parameters within a hierarchy.
  --version        Show the version and exit.
  --help           Show this message and exit.
```