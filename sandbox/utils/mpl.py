import matplotlib.pyplot as plt

from sandbox.utils.fileio import make_parent_dir


def savefig(fname, **kwargs):
    make_parent_dir(fname)
    tight_layout = kwargs.pop('tight_layout', False)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(fname, **kwargs)
    plt.close()
