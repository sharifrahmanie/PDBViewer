**Automatically retrieve a PDB file for a given RCSB PDB id and visualize its 3D structure.**

# Installation

```r{}
pip install PDBViewer
```
# Running

```{r codes}
from PDBViewer.PDBViewer import PDBViewer
viewer = PDBViewer()
viewer.view('8DC4')
```


![8DC4](8DC4.png)

