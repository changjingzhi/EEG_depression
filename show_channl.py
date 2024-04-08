import mne

# 读取CNT文件
raw = mne.io.read_raw_cnt('scan4.5_rest_data/normal/1_huangkun Data-22.cnt', preload=False)

# 获取电极名称列表
electrode_names = raw.ch_names

# 打印电极名称
print("Electrode Names:")
for name in electrode_names:
    print(name,end=' ')


# 读取CNT文件
raw = mne.io.read_raw_cnt('scan4.5_rest_data/patient/s1.cnt', preload=False)

# 获取电极名称列表
electrode_names = raw.ch_names

# 打印电极名称
print("Electrode Names:")
for name in electrode_names:
    print(name,end=' ')
