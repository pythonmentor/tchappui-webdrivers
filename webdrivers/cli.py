"""Console script for install_webdrivers."""
import click

from . import webdrivers


@click.command()
@click.option('--path', '-p', default='.', show_default=True)
@click.option('--chromedriver', is_flag=True)
@click.option('--geckodriver', is_flag=True)
def main(path, chromedriver, geckodriver):
    """Console script for install_webdrivers."""
    if not geckodriver or (geckodriver and chromedriver):
        click.echo("Installing the latest version of chromedriver.")
        webdrivers.install_latest_chromedriver(path)
    if not chromedriver or (chromedriver and geckodriver):
        click.echo("Installing the latest version of geckodriver.")
        webdrivers.install_latest_geckodriver(path)


if __name__ == "__main__":
    main()