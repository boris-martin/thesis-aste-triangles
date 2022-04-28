from generate_square_mesh import generate_unit_square_vtk

generate_unit_square_vtk("coarse.vtk", 1e-1)
generate_unit_square_vtk("fine.vtk", 1e-2)