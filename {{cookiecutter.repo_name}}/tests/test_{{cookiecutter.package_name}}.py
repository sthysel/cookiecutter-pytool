from click.testing import CliRunner

from {{ cookiecutter.package_name }}.cli import main
{%- if cookiecutter.test_matrix_configurator|lower == 'yes' and cookiecutter.test_matrix_configurator|lower == 'no' or
       cookiecutter.command_line_interface == 'no' %}
import {{ cookiecutter.package_name }}
{%- endif %}


def test_main():
{%- if cookiecutter.test_matrix_configurator|lower == 'yes' and cookiecutter.test_matrix_configurator|lower == 'no' %}
    assert 'site-packages' in {{ cookiecutter.package_name }}.__file__
{%- endif %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0
