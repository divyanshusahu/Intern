FROM ubuntu:18.04
LABEL name="Divyanshu Sahu"
LABEL email="dsahu1997@gmail.com"

RUN apt-get update && \
    apt-get install -y \
    python3.6 \
    gmsh

RUN apt-get install -y ssh

COPY backend/run_process.py /python/run_process.py
COPY solverMain /solverMain
COPY vtk_to_vtp/vtkunstructured_to_polydataset /solverMain/

RUN chmod +x /solverMain/solverMain /solverMain/vtkunstructured_to_polydataset