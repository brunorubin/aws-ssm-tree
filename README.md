# SSM Tree

SSM Tree is a tool that provides a tree visualization of the parameters hierarchy from AWS System Manager Parameter Store.

## Installation

SSM Tree can be installed using [pip](https://pip.pypa.io/en/stable/):

```bash
$ pip install aws-ssm-tree
```

## Example
![example](https://user-images.githubusercontent.com/2822509/52458942-3178d700-2bc7-11e9-90c9-2b52930b80df.png)

### Usage
```
Usage: ssm-tree [OPTIONS]

  SSM Tree is a tool that provides a tree visualization of the parameters
  hierarchy from AWS System Manager Parameter Store.

Options:
  -p, --path TEXT       The hierarchy for the parameter. Hierarchies start
                        with a forward slash (/) and end with the parameter
                        name. Here is an example of a hierarchy: /Servers/Prod
                        [required]
  -s, --show-encrypted  Show encrypted parameters with a '*' symbol.
  --no-recursion        Prevent recursion into descending levels.
  --region TEXT         Specify which AWS Region to send this request to.
  --version             Shows the version and exit.
  --help                Shows this message and exit.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
