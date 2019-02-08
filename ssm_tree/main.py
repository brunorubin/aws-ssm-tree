from treelib import Tree, Node
import boto3
import click

@click.command()
@click.option('--path', required=True, help='The hierarchy for the parameter. Hierarchies start with a forward slash (/) and end with the parameter name. Here is an example of a hierarchy: /Servers/Prod')
@click.option("--recursive", "-r", is_flag=True, help="Retrieve all parameters within a hierarchy.")
@click.version_option(message='aws-ssm-tree - version %(version)s')
@click.pass_context
def main(ctx, **kwargs):
    """
    SSM Tree is a tool that provides a tree visualization of the
    parameters hierarchy from AWS System Manager Parameter Store.
    """
    path = kwargs.pop('path')
    recursive = kwargs.pop('recursive')
    
    try: 
        parameters = []
        for parameter in get_parameters(path, recursive):
            parameters.append(parameter['name'])
        build_tree(parameters)
    except Exception as e:
        raise click.ClickException("{}".format(e))
    
def get_parameters(path=None, recursive=False):
    paginator = boto3.client('ssm').get_paginator('get_parameters_by_path')
    pages = paginator.paginate(
        Path = path,
        Recursive = recursive,
        WithDecryption = False
    )
    parameters = []
    for page in pages:
        parameters_page = [{"name": entry['Name'],
                           "value": entry['Value']} for entry in page['Parameters']]
        parameters.extend(parameters_page)
    return parameters

def get_tree(nodes=None, parent=None, node_list=None):
    node_list = []
    for index, node in enumerate(nodes):
        if node:
            node_list.append({'node': node})
    for index,node in enumerate(nodes):
        if index == 1:
            node_list[index-1]['parent'] = None
        else:
            node_list[index-1]['parent'] = node_list[index-2]['node']
    return node_list

def build_tree(path):
    tree = Tree()
    for item in path:
        for node in get_tree(item.split('/')):
            try:
                tree.create_node(node['node'],node['node'],parent=node['parent'])
            except:
                pass
    if not tree:
        print("Nothing to show.")
    else:
        return tree.show()