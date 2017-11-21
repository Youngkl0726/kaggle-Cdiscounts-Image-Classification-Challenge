#!/usr/bin/env bash
# Change to the project root directory. Assume this file is at scripts/.
cd $(dirname ${BASH_SOURCE[0]})/../

# Some constants
CAFFE_DIR=/mnt/lustre/yangkunlin/sensenet/example
export PYTHONPATH=/mnt/lustre/yangkunlin/sensenet/core/python:$PYTHONPATH
MODELS_DIR=/mnt/lustre/yangkunlin/kaggle/normal_model


extract_features() {

  local trained_model=$1

  local result_dir=/mnt/lustre/yangkunlin/kaggle/normal_model/n1_result
  rm -rf ${result_dir}
  mkdir -p ${result_dir}
  echo ${result_dir}
  # Extract train, val, test probe, and test gallery features.
  for num in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 \
             23 24 25 26 27 28 29 30 31 32 33 34 35; do
    echo "Extracting No. ${num} set"
    local num_samples=$(wc -l /mnt/lustre/yangkunlin/kaggle/test_list/test${num}.txt | awk '{print $1}')
    local num_iters=$(((num_samples + 19) / 20))
    local model=temp_normal_model_test.prototxt
    local list=test${num}
    sed -e "s/\${list}/${list}/g" \
      ${MODELS_DIR}/normal_model_test.prototxt > ${model}
    echo ${model}
    MV2_USE_CUDA=1 MV2_ENABLE_AFFINITY=0 MV2_SMP_USE_CMA=0 \
      srun -p Test --gres=gpu:1 -n1 --ntasks-per-node=1 --kill-on-bad-exit=1\
      ${CAFFE_DIR}/build/tools/extract_features \
      ${trained_model} ${model} prob \
      ${result_dir}/prob_${num}_lmdb \
      ${num_iters} lmdb GPU
    srun -p Test python2 /mnt/lustre/yangkunlin/kaggle/normal_model/lmdb_to_prob.py \
      ${result_dir}/prob_${num}_lmdb ${result_dir}/prob_${num}.npy \
      --truncate ${num_samples}
  done
}


trained_model=/mnt/lustre/yangkunlin/kaggle/normal_model/normal_kaggel_iter_300000.caffemodel

  

extract_features ${trained_model}


# Market1501 cuhk01 cuhk03 3dpes ilids prid viper Dukemtmc-reid SenseReID
# Market1501-test cuhk01 cuhk03 3dpes ilids prid viper SenseReID
