#!/usr/bin/env bash
# Change to the project root directory. Assume this file is at scripts/.
cd $(dirname ${BASH_SOURCE[0]})/../

# Some constants
CAFFE_DIR=/mnt/lustre/yangkunlin/sensenet/example
#PATH=my_exp/id149509/googlenet_v4_re224_trible4_ft_259w
train_model() {
  local solver=/mnt/lustre/yangkunlin/kaggle/normal_model/normal_solver.prototxt 
  local log=/mnt/lustre/yangkunlin/kaggle/normal_model/log/normal.log
  export LD_LIBRARY_PATH=/mnt/lustre/share/cuda-7.5/lib64:$LD_LIBRARY_PATH
  export LD_LIBRARY_PATH=/mnt/lustre/share/libboost/lib:$LD_LIBRARY_PATH
  mkdir -p $(dirname ${log})

  MV2_USE_CUDA=1 MV2_ENABLE_AFFINITY=0 MV2_SMP_USE_CMA=0 srun -p Retrieval \
  --mpi=pmi2 --gres=gpu:4 -n12 --ntasks-per-node=4 --job-name=normal_kag \
  ${CAFFE_DIR}/build/tools/caffe train --solver=${solver} 2>&1|tee ${log}
}
train_model
