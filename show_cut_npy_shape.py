import numpy as np
import os

# 替换为包含.npy文件的文件夹路径列表
folder_paths = ["npy_data/cut_patient_npy", "npy_data/cut_normal_npy"]  # 替换为实际的文件夹路径列表
# ["normal_save", "open_normal_save", "open_patient_save",'patient_save']
# 循环遍历每个文件夹
for folder_path in folder_paths:
    # 获取文件夹中的所有.npy文件
    npy_files = [file for file in os.listdir(folder_path) if file.endswith('.npy')]

    # 循环加载每个.npy文件并显示其形状
    for npy_file in npy_files:
        npy_file_path = os.path.join(folder_path, npy_file)
        data = np.load(npy_file_path)
        print(f"Folder: {folder_path}, File: {npy_file}, Shape: {data.shape}")
