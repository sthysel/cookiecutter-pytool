import click

from . import settings

{{cookiecutter.package_name.replace('-','_')}}_config = click.make_pass_decorator(CookConfig, ensure=True)


@click.group()
@click.version_option(settings.__version__)
@click.option('-v', '--verbose', default=0, count=True, help='Level of verbosity of logs')
@click.option('-c', '--cache-path',
              default=settings.CACHE,
              type=click.Path(),
              help='Cache path, Default: {}'.format(settings.CACHE))
@cook_config
@click.command()
