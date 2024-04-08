import os
import mne
import numpy as np

# 定义函数来处理每个CNT文件
def process_cnt_file(cnt_file, output_folder):
    # 读取CNT文件
    raw = mne.io.read_raw_cnt(cnt_file, preload=True)
    
    # 删除HEOL、HEOR、VEOU和VEOL通道
    channels_to_remove = ['HEOL', 'HEOR', 'VEOU', 'VEOL','REF']
    raw.drop_channels(channels_to_remove)
    
    # 获取处理后的EEG数据
    eeg_data = raw.get_data()
    raw.filter(0.5,45,fir_design='firwin')
    # 获取文件名（不包含扩展名）
    file_name = os.path.splitext(os.path.basename(cnt_file))[0]
    
    # 构建保存路径
    save_path = os.path.join(output_folder, f'{file_name}_processed.npy')
    
    # 保存处理后的EEG数据为npy文件
    np.save(save_path, eeg_data)

# 指定包含CNT文件的文件夹路径
folder_path = 'scan4.5_rest_data/patient'

# 指定保存处理后的npy文件的文件夹路径
output_folder = 'npy_data/patient_npy'

# 遍历文件夹中的每个文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.cnt'):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, file_name)
        
        # 处理CNT文件并保存处理后的npy文件到指定文件夹
        process_cnt_file(file_path, output_folder)
