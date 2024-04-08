import numpy as np
import os
from tqdm import tqdm

# 指定包含原始npy文件的文件夹路径
input_folder = 'npy_data/patient_npy'

# 确定剪切后的数据长度
cut_length = 5000

# 创建保存剪切数据的文件夹
output_folder = 'npy_data/cut_patient_npy/'
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的每个npy文件
for file_name in os.listdir(input_folder):
    if file_name.endswith('.npy'):
        # 加载原始npy文件
        data = np.load(os.path.join(input_folder, file_name))
        
        # 确定剪切的段数
        num_cuts = data.shape[1] // cut_length

        # 使用tqdm显示进度条
        for i in tqdm(range(num_cuts), desc=f'Processing {file_name}', unit='cut'):
            cut_data = data[:, i*cut_length : (i+1)*cut_length]
            np.save(os.path.join(output_folder, f'{file_name[:-4]}_cut_{i}.npy'), cut_data)

        