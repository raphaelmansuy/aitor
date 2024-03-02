""" 

An AI toolbox for working with Hugging Face Hub.

Tor stands for Torii 🛐, a Japanese gate, suggesting a gateway to AI.	

"""
import click
from huggingface_hub import HfApi, snapshot_download, hf_hub_download


def validate_model(_ctx, _param, value):
    """Validate the model name."""
    if not value:
        raise click.BadParameter(
            "Model name cannot be empty. Please specify a model name."
        )
    return value


@click.group()
def cli():
    """
    An AI toolbox for working with Hugging Face Hub.

    Tor stands for Torii 🛐, a Japanese gate, suggesting a gateway to AI.	
    """
    pass


@cli.command()
@click.option(
    "--model",
    required=True,
    help="The name of the model to download.",
    callback=validate_model,
)
@click.option(
    "--localdir",
    default="models",
    show_default=True,
    help="The local directory to save the model to.",
)
@click.option(
    "--file",
    default=None,
    help="The specific file to download from the model repository. If not specified, the entire model will be downloaded.",
)
def download(model, localdir, file):
    """
    Downloads a specific version of a model from Hugging Face Hub.

    This script downloads a specified version of a model from the Hugging Face Hub and saves it to a local directory.
    If the --file option is specified, only the specified file will be downloaded.
    """
    if file:
        # Download only the specified file
        hf_hub_download(
            repo_id=model, local_dir=localdir, filename=file, use_auth_token=True
        )
    else:
        # Download the entire model
        snapshot_download(
            repo_id=model, local_dir=localdir, use_auth_token=True, filename=file
        )


@cli.command("list")
@click.option(
    "--model",
    required=True,
    help="The name of the model to list files for",
    callback=validate_model,
)
@click.option(
    "--version",
    default=None,
    help="The version of the model to list files for. If not specified, the latest version will be used.",
)
def list_files(model, version):
    """
    Lists all the files for a specific version of a model from Hugging Face Hub.

    This script lists all the files for a specified version of a model from the Hugging Face Hub.
    If no version is specified, it lists files for the latest version.
    """
    api = HfApi()
    if version:
        files = api.list_repo_files(repo_id=model, revision=version)
    else:
        files = api.list_repo_files(repo_id=model)
    for file in files:
        click.echo(file)


if __name__ == "__main__":
    cli()
