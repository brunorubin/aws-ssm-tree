from click.testing import CliRunner
from ssm_tree import main

def test_cli_with_version():
    runner = CliRunner()
    result = runner.invoke(main.main, ['--version'])
    assert not result.exception
    assert result.exit_code == 0
    assert 'aws-ssm-tree - version' in result.output