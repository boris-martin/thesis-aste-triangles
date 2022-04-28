import gmsh
import meshio

def generate_unit_square_vtk(out, resolution):

    gmsh.initialize()

    # Next we add a new model named "t1" (if gmsh.model.add() is not called a new
    # unnamed model will be created on the fly, if necessary):
    gmsh.model.add("t1")

    lc = resolution
    gmsh.model.geo.addPoint(0,0,0, lc, 1)
    gmsh.model.geo.addPoint(1,0,0, lc, 2)
    gmsh.model.geo.addPoint(1,1,0, lc, 3)
    gmsh.model.geo.addPoint(0,1,0, lc, 4)

    gmsh.model.geo.addLine(1, 2)
    gmsh.model.geo.addLine(2, 3)
    gmsh.model.geo.addLine(3, 4)
    gmsh.model.geo.addLine(4, 1)

    gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)

    surface = gmsh.model.geo.addPlaneSurface([1], 1)

    gmsh.model.geo.synchronize()

    # Add groups
    gmsh.model.addPhysicalGroup(2, [surface], name = "Surface")
    gmsh.model.addPhysicalGroup(1, [1,2,3,4], name = "Boundary")

    gmsh.model.mesh.generate(3)
    gmsh.write("tmp.msh")

    gmsh.finalize()

    # Convert 

    mesh = meshio.read("tmp.msh")
    mesh.write(out) 