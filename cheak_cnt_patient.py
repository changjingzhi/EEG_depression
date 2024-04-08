import os
import mne

def check_electrode_order(folder_path, expected_order):
    # 获取文件夹中的所有CNT文件
    cnt_files = [file for file in os.listdir(folder_path) if file.endswith('.cnt')]

    # 循环检查每个CNT文件的电极顺序
    for cnt_file in cnt_files:
        cnt_file_path = os.path.join(folder_path, cnt_file)

        # 读取CNT文件
        raw = mne.io.read_raw_cnt(cnt_file_path, preload=True)

        # 获取当前CNT文件的电极顺序
        current_order = raw.ch_names

        # 检查电极顺序是否符合预期
        if current_order == expected_order:
            print(f"{cnt_file}: Electrode order is correct.")
        else:
            print(f"{cnt_file}: Electrode order is incorrect. Expected order: {expected_order}, Current order: {current_order}")

# 替换为实际的文件夹路径和期望的电极顺序
folder_path = "scan4.5_rest_close/patient"

expected_order = [
    'HEOL', 'HEOR', 'Fp1', 'Fp2', 'VEOU', 'VEOL', 'F7', 'F3', 'Fz', 'F4',
    'F8', 'FT7', 'FC3', 'FCz', 'FC4', 'FT8', 'T3', 'C3', 'Cz', 'C4', 'T4',
    'TP7', 'CP3', 'CPz', 'CP4', 'TP8', 'A1', 'T5', 'P3', 'Pz', 'P4', 'T6',
    'A2', 'O1', 'Oz', 'O2', 'REF'
]
#  s33.cnt, s21.cnt
# 执行检查
check_electrode_order(folder_path, expected_order)


