import os
import sys
from vtk import vtkPolyDataReader, vtkXMLPolyDataWriter

def vtk2vtp(invtkfile, outvtpfile, binary):
    reader = vtkPolyDataReader()
    reader.SetFileName(invtkfile)
    reader.Update()

    writer = vtkXMLPolyDataWriter()
    writer.SetFileName(outvtpfile)
    if binary:
        writer.SetFileTypeToBinary()
    writer.SetInputData(reader.GetOutput())
    writer.Update()

vtk2vtp("../solverMain/test/cad_surfacefile.vtk", "./tmp/output.vtp", False)