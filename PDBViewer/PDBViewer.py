import urllib.request
import gzip
import py3Dmol

class PDBViewer:
    def __init__(self):
        pass

    def view(self, pdb_file):
        with open(pdb_file, 'r') as f:
            pdb_data = f.read()
        view = py3Dmol.view(width=600, height=400)
        view.addModel(pdb_data, 'pdb')
        view.setStyle({'cartoon': {'color': 'spectrum'}})
        view.zoomTo()
        view.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py input.pdb")
        sys.exit(1)
    pdb_file = sys.argv[1]
    viewer = PDBViewer()
    viewer.view(pdb_file)

