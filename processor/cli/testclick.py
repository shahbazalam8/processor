import click

from processor.parsers.minesymdev import SymdevParse
from processor.parsers.dbconnect import DbConnect

@click.command()
@click.option("--parse", type=click.Choice(["ig","sg","pg", "symdev"]),prompt='parsetype')
@click.option("--filename",prompt="xml file required to parse(without .xml extension")
# @click.option("--dbtype", type=click.Choice(["postgres","mysql"]), prompt=True)
# @click.option("--server", prompt=True, default='localhost')
# @click.option("--dbuser", prompt=True)
# @click.option("--password", hide_input=True,prompt=True)
def test(parse,filename):
    ''''
        simple program for print and test cli
    '''
    print('testing cli program :'+ parse)
    if parse == 'symdev':
        """" Need to check for file exsistence  """
        s = SymdevParse()
        s.new_prog(filex=filename)
        # dataf = s.new_prog(filex=filename)
        # db = DbConnect()
        # db.dbengine1(dataf,dbtype,dbuser,password,server)

if __name__ == '__main__':
    test()
