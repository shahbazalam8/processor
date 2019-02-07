import os
import warnings

import click
import colorama
import yaml

from processor.cli.parse import parse_group

@click.group()
@click.option("--parse",type=click.Choice(["ig","sg","pg", "symdev"]), default= "")

#@click.version_option(version=__version__, prog_name="processor")
def cli(
        ctx, debug, directory, no_colour, output, var, var_file
):
    """
    processor is a tool to process specif xml files for internal use.
    """
    # logger = setup_logging(debug, no_colour)
    colorama.init()
    # Enable deprecation warnings
    warnings.simplefilter("always", DeprecationWarning)
    ctx.obj = {
        "user_variables": {},
        "output_format": output,
        "no_colour": no_colour,
        "awsscripter_dir": directory if directory else os.getcwd()
    }
    if var_file:
        for fh in var_file:
            parsed = yaml.safe_load(fh.read())
            ctx.obj["user_variables"].update(parsed)

            # the rest of this block is for debug purposes only
            existing_keys = set(ctx.obj["user_variables"].keys())
            new_keys = set(parsed.keys())
            overloaded_keys = existing_keys & new_keys  # intersection
            # if overloaded_keys:
            #     logger.debug(
            #         "Duplicate variables encountered: {0}. "
            #         "Using values from: {1}."
            #         .format(", ".join(overloaded_keys), fh.name)
            #     )

    if var:
        # --var options overwrite --var-file options
        for variable in var:
            variable_key, variable_value = variable.split("=")
            # if variable_key in ctx.obj["user_variables"]:
            #     logger.debug(
            #         "Duplicate variable encountered: {0}. "
            #         "Using value from --var option."
            #         .format(variable_key)
            #     )
            ctx.obj["user_variables"].update({variable_key: variable_value})


cli.add_command(parse_group)
