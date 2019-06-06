FROM ubuntu:18.04
LABEL name="Divyanshu Sahu"
LABEL email="dsahu1997@gmail.com"

RUN apt-get update && \
    apt-get install -y \
    python3.6 \
    gmsh

RUN apt-get install -y ssh

RUN apt-get install -y python3-pip && \
    pip3 install boto3

RUN mkdir /work

ENV AWS_ACCESS_KEY_ID=AKIASKEGXXNEZDPUOVNB
ENV AWS_SECRET_ACCESS_KEY=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
ENV REGION=ap-south-1

COPY backend/run_process.py /python/run_process.py
COPY backend/cloud_connect.py /python/cloud_connect.py
COPY solverMain /solverMain
COPY vtk_to_vtp/vtkunstructured_to_polydataset /solverMain/

RUN chmod +x /solverMain/solverMain /solverMain/vtkunstructured_to_polydataset