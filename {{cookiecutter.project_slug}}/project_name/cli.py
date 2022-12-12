import click
from ingest import get_data, store_data


@click.group()
def cli():
    pass


@cli.command()
@click.option("--src-path", help="Raw data path")
@click.option("--dst-path", help="output path to store data")
def ingest(src_path, dst_path):
    print("ingest")
    data = get_data(src_path)
    store_data(data, dst_path)
