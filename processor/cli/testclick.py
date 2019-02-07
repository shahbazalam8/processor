import click

from processor.parsers.minesymdev import SymdevParse

@click.command()
@click.option("--parse",type=click.Choice(["ig","sg","pg", "symdev"]),prompt='parsetype')
@click.option("--filename",type=click.Choice(["ig","sg","pg", "symdev"]),prompt='FileName')
def test(parse,filename):
    ''''simple program for print and test cli'''
    print('testing cli program :'+ parse)
    if parse == 'symdev':
        s = SymdevParse()
        s.new_prog(filex=filename)

if __name__ == '__main__':
    test()
