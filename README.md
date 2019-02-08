# SSM Tree

SSM Tree is a tool that provides a tree visualization of the parameters hierarchy from AWS System Manager Parameter Store.

## Installation

SSM Tree can be installed using [pip](https://pip.pypa.io/en/stable/):

```bash
$ pip install aws-ssm-tree
```

## Example
![example](https://user-images.githubusercontent.com/2822509/52458912-f676a380-2bc6-11e9-99a3-a66d722850a3.png)

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
