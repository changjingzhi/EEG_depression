import os
import mne

folder_paths = ['scan4.5_rest_data/normal', "scan4.5_rest_data/patient"]
# 遍历文件夹中的每个文件
for folder_path in folder_paths:
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.cnt'):
            # 构建完整的文件路径
            file_path = os.path.join(folder_path, file_name)
            
            # 读取CNT文件
            raw = mne.io.read_raw_cnt(file_path, preload=False)
            
            # 获取数据信息
            info = raw.info
            
            # 打印采样率
            print(f"Sampling rate of {file_name}: {info['sfreq']} Hz")
