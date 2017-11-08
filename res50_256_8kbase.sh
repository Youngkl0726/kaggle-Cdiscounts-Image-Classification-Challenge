#!/usr/bin/env bash
# Change to the project root directory. Assume this file is at scripts/.
cd $(dirname ${BASH_SOURCE[0]})/../

# export LD_LIBRARY_PATH=/mnt/lustre/share/nccl-7.5/lib:$LD_LIBRARY_PATH
# Some constants
CAFFE_DIR=/home/yangkunlin/storage/caffe_kaggle

exp=/home/yangkunlin/storage/kaggle
 # local pretrained_model=$2
solver=${exp}/Resnet-50_8kbase_solver.prototxt
log=${exp}/log/Resnet-50_256_8kbase.log

  mkdir -p $(dirname ${log})

  MV2_USE_CUDA=1 MV2_ENABLE_AFFINITY=0 MV2_SMP_USE_CMA=0 srun -p Retrieval \
  --gres=gpu:4 -n1 --ntasks-per-node=1 --job-name=res5025601 \
  ${CAFFE_DIR}/build/tools/caffe train --solver=${solver} --gpu=0,1,2,3  2>&1|tee ${log}

