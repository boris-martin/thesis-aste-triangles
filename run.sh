#!/usr/bin/bash
python generate_mesh

vtk_calculator.py -d linear -f "x+y" -m coarse.vtk

preciceMap -v -p A --mesh coarse --data linear &
preciceMap -v -p B --mesh fine --data linear --output mapped

vtk_calculator.py -m mapped.vtk -f "x+y" -d difference --diffdata "linear" --diff