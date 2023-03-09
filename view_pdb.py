import urllib.request
import gzip
import py3Dmol
def view_pdb(pdb_id): 
    # By @biomedical_informatics Edris Sharif Rahmani, March 9, 2023
    pdb_id = str(pdb_id).lower()
    url = f'ftp://ftp.rcsb.org/pub/pdb/data/structures/all/pdb/pdb{pdb_id}.ent.gz'
    urllib.request.urlretrieve(url, f'{pdb_id}.pdb.gz')
    with gzip.open(f'{pdb_id}.pdb.gz', 'rb') as f_in:
        with open(f'{pdb_id}.pdb', 'wb') as f_out:
            f_out.write(f_in.read())
    with open(f'{pdb_id}.pdb', 'r') as f:
        pdb_data = f.read()
    view = py3Dmol.view(width=600, height=400)
    view.addModel(pdb_data, 'pdb')
    view.setStyle({'cartoon': {'color': 'spectrum'}})
    view.zoomTo()
    view.show()
    
#Crystal structure of p53 Y220C covalently bound to carbazole KG3
view_pdb("8DC4")
# Structure of Ygr203w, a yeast protein tyrosine phosphatase of the Rhodanese family
view_pdb("3FS5")
