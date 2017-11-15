#!/usr/bin/env bash
# Change to the project root directory. Assume this file is at scripts/.
cd $(dirname ${BASH_SOURCE[0]})/../

# Some constants
CAFFE_DIR=external/caffe
export PYTHONPATH=external/caffe/python:$PYTHONPATH
export LD_LIBRARY_PATH=/mnt/lustre/share/nccl-8.0/lib:$LD_LIBRARY_PATH


extract_features() {
  local trained_model=$1
  local result_dir= res_dir
  rm -rf ${result_dir}
  mkdir -p ${result_dir}
  echo ${result_dir}
  # Extract train, val, test probe, and test gallery features.
  if 1:
    local num_samples=$(wc -l testlist.txt | awk '{print $1}')
    local num_iters=$(((num_samples + 19) / 20))
    local model=deploy_googlev4bl.prototxt
    MV2_USE_CUDA=1 MV2_ENABLE_AFFINITY=0 MV2_SMP_USE_CMA=0 \
      srun -p Test --gres=gpu:1 -n1 --ntasks-per-node=1 --kill-on-bad-exit=1\
      ${CAFFE_DIR}/build/tools/extract_features \
      ${trained_model} ${model} prob \
      ${result_dir}/prob_lmdb \
      ${num_iters} lmdb GPU
    srun -p Test python2 tools/convert_lmdb_to_numpy.py \
      ${result_dir}/prob_lmdb ${result_dir}/prob.npy \
      --truncate ${num_samples}
}


trained_model=external/exp/cvpr/snapshots/googlenet_v4_8kbase_iter_100000.caffemodel


extract_features ${trained_model}

