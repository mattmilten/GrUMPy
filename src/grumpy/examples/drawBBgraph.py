import fire
import os

try:
    from coinor.grumpy import BBTree
except ImportError:
    from src.grumpy import BBTree


def drawgraph(inputfile, savefile=None, silent=False):
    print('processing: '+inputfile)
    bt = BBTree()
    with open(inputfile, 'r') as f:
        for line in f:
            bt.ProcessLine(line)

    if not silent:
        bt.set_display_mode('xdot')
        try:
            bt.display()
        except:
            print('could not display graph for '+inputfile)

    if not savefile is None:
        bt.set_display_mode('file')
        try:
            bt.display()
            os.rename('graph.png', savefile)
            print('saved graph to '+savefile)
        except:
            print('could not save graph for '+inputfile)


if __name__ == "__main__":
    fire.Fire(drawgraph)
