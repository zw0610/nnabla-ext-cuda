FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl bzip2 libopenmpi-dev openmpi-bin \
    && rm -rf /var/lib/apt/lists/*

# Fix NCCL version
ENV NCCL_VERSION 2.4.8
RUN apt-get remove -y --allow-change-held-packages libnccl2 \
    && apt-get install -y --no-install-recommends \
        libnccl2=$NCCL_VERSION-1+cuda9.0 \
    && rm -rf /var/lib/apt/lists/*

RUN umask 0 \
    && mkdir -p /tmp/deps \
    && cd /tmp/deps \
    && curl -L https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3 \
    && rm -rf Miniconda3-latest-Linux-x86_64.sh \
    && PATH=/opt/miniconda3/bin:$PATH \
    && conda install python=3.6 \
    && conda update -y --all \
    && conda install pip wheel opencv \
    && conda clean -y --all \
    && cd / \
    && rm -rf /tmp/*

ENV PATH /opt/miniconda3/bin:$PATH

RUN pip install nnabla-ext-cuda90-nccl2-ubuntu16
