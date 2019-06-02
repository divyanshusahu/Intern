import os
import sys
from vtk import vtkPolyDataReader, vtkXMLPolyDataWriter

def vtk2vtp(invtkfile, outvtpfile, binary=False):
    reader = vtkPolyDataReader()
    reader.SetFileName(invtkfile)

    writer = vtkXMLPolyDataWriter()
    writer.SetFileName(outvtpfile)
    if binary:
        writer.SetFileTypeToBinary()
    writer.SetInput(reader.GetOutput())
    writer.Update()