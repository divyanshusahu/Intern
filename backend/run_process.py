import subprocess, sys

def run_solver(path_to_input) :
    run_code = 0
    c1 = "/solverMain/solverMain %s" % (path_to_input)
    r1 = subprocess.run(c1, shell=True).returncode
    if r1 != 0 :
        run_code = 2
        return run_code

    #c2 = "cp /solver/test/gmsh_file.geo /work/"
    #subprocess.run(c2, shell=True)
    c3 = "gmsh /work/gmsh_file.geo -algo del2d -2 -bin -o /work/cad_surfacefile.vtk"
    r3 = subprocess.run(c3, shell=True).returncode
    if r3 != 0 :
        run_code = 3
        return run_code
    
    c4 = "/solverMain/vtkunstructured_to_polydataset /work/cad_surfacefile.vtk /work/cad_surfacefile.vtp"
    r4 = subprocess.run(c4, shell=True).returncode
    if r4 != 0 :
        run_code = 4
        return run_code
    
    return run_code

if __name__ == "__main__" :
    run_solver(sys.argv[1])