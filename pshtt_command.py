import click
import pshtt
import subprocess

@click.command()
@click.argument('domain')
def cli(domain):
    """pshtt cli output"""
    result = subprocess.run(["pshtt", domain, "--json"], stdout=subprocess.PIPE)
    click.echo(result.stdout.decode("utf-8"))


