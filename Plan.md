# ASTE accuracy test

- Generate a coarse mesh and a fine mesh
- Configure connectivity ? (=> start with NN)
- Measure accuracy

## Generate mesh

Use Gmsh API as a script!

## Sample data on coarse mesh

`vtk_calculator.py -d linear -f "x+y" -m coarse.vtk`

## Compute mapping
`preciceMap -v -p A --mesh coarse --data linear &
preciceMap -v -p B --mesh fine --data linear --output mapped`


## Compute difference
vtk_calculator.py -m mapped.vtk -f "x+y" -d difference --diffdata "linear" --diff

