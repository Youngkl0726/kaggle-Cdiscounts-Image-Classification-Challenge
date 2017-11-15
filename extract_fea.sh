#!/usr/bin/env bash
# Change to the project root directory. Assume this file is at scripts/.
cd $(dirname ${BASH_SOURCE[0]})/../

# Some constants
CAFFE_DIR=/mnt/lustre/yangkunlin/caffe_kaggle
export PYTHONPATH=/mnt/lustre/yangkunlin/caffe_kaggle/python:$PYTHONPATH


extract_features() {
  local trained_model=$1
  local result_dir=/mnt/lustre/yangkunlin/kaggle/result/n1/
  # rm -rf ${result_dir}
  # mkdir -p ${result_dir}
  echo ${result_dir}
  # Extract train, val, test probe, and test gallery features.
  local num_samples=$(wc -l /mnt/lustre/yangkunlin/kaggle/test.txt | awk '{print $1}')
  local num_iters=$(((num_samples + 19) / 20))
  local model=ResNet-50_8kbase_test.prototxt
  MV2_USE_CUDA=1 MV2_ENABLE_AFFINITY=0 MV2_SMP_USE_CMA=0 \
   srun -p Test --gres=gpu:1 -n1 --ntasks-per-node=1 --kill-on-bad-exit=1\
   ${CAFFE_DIR}/build/tools/extract_features \
   ${trained_model} ${model} prob \
   ${result_dir}/prob_lmdb \
   ${num_iters} lmdb GPU
   srun -p Test python2 /mnt/lustre/yangkunlin/kaggle/convert_lmdb_to_numpy.py \
   ${result_dir}/prob_lmdb ${result_dir}/prob.npy \
   --truncate ${num_samples}
}


trained_model=/mnt/lustre/yangkunlin/kaggle/res50_8kbase_iter_200000.caffemodel


extract_features ${trained_model}

