import click
#import individual parser commands
from processor.cli.igparse import ig_parse
from processor.cli.sgparse import sg_parse

@click.group(name="parse")
def parse_group():
    """ 
    parse as per user request
    :return: 
    """
    pass

parse_group.add_command(ig_parse)
parse_group.add_command(sg_parse)