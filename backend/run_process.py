import subprocess, sys
from cloud_connect import dwnl_fl, create_presigned_url, upld_fl

def run_solver(path_to_input) :
    saved_path = dwnl_fl(path_to_input)
    run_code = 0
    with open(saved_path) as f :
        data = f.read()
    if "planform_description" in data :
        c1 = "/solverMain/solverMain %s" % (saved_path)
        r1 = subprocess.run(c1, shell=True).returncode
        if r1 != 0 :
            run_code = 2
            return run_code
    else :
        c1 = "/solverMain/roundCanopy %s" % (saved_path)
        r1 = subprocess.run(c1, shell=True).returncode
        if r1 != 0 :
            run_code = 2
            return run_code

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

    output_file_path = path_to_input.split("/")[0] + "/cad_surfacefile.vtp"
    output_dxf_path = path_to_input.split("/")[0] + "/drawing.dxf"
    upld_fl('/work/cad_surfacefile.vtp', output_file_path)
    upld_fl('/work/drawing.dxf', output_dxf_path)
    return 0

if __name__ == "__main__" :
    run_solver(sys.argv[1])