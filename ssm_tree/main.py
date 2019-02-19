from treelib import Tree, Node
import boto3
import click

region_name = None
path_separator = '/'
secure_string_identifier = '[*]'

@click.command()
@click.option("--path", "-p", required=True, help="The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. Here is an example of a hierarchy: /Servers/Prod")
@click.option("--show-encrypted", "-s", is_flag=True, help="Show encrypted parameters with a '*' symbol.")
@click.option("--no-recursion", is_flag=True, help="Prevent recursion into descending levels.")
@click.option("--region", help="Specify which AWS Region to send this request to.")
@click.version_option(message="aws-ssm-tree - version %(version)s")
@click.pass_context
def main(ctx, **kwargs):
    """
    SSM Tree is a tool that provides a tree visualization of the
    parameters hierarchy from AWS System Manager Parameter Store.
    """
    global region_name 

    path = kwargs.pop('path')
    show_encrypted = kwargs.pop('show_encrypted')
    recursive =  not kwargs.pop('no_recursion')
    region_name = kwargs.pop('region')

    try:
        build_tree(path, recursive, show_encrypted)
    except Exception as e:
        raise click.ClickException("{}".format(e))
    
def get_parameters(path=None, recursive=True):
    client = boto3.client('ssm', region_name=region_name)
    paginator = client.get_paginator('get_parameters_by_path')
    pages = paginator.paginate(
        Path = path,
        Recursive = recursive,
        WithDecryption = False
    )
    parameters = []
    for page in pages:
        parameters_page = [{"name": entry['Name'],
                           "type": entry['Type'],
                           "version": entry['Version']} for entry in page['Parameters']]
        parameters.extend(parameters_page)
    return parameters

def get_tree_from_path(path=None):
    path = path.split(path_separator)
    node_list = []
    for index, node in enumerate(path):
        if node:
            node_list.append({'node': node})
    for index, node in enumerate(path):
        if index == 1:
            node_list[index-1]['parent'] = None
        else:
            node_list[index-1]['parent'] = node_list[index-2]['node']
    return node_list

def build_tree(path, recursive, show_encrypted=False):
    parameters = []
    for parameter in get_parameters(path, recursive):
        if show_encrypted and parameter['type'] == 'SecureString':
            parameters.append(parameter['name'] + " " + secure_string_identifier)
        else:
            parameters.append(parameter['name'])
    tree = Tree()
    for item in parameters:
        for node in get_tree_from_path(item):
            try:
                tree.create_node(node['node'],node['node'],parent=node['parent'])
            except:
                pass
    if not tree:
        print("Nothing to show.")
    else:
        return tree.show()