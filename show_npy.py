import numpy as np
import matplotlib.pyplot as plt
import mne

# 替换为.npy文件的路径
npy_file_path = "your_eeg_data.npy"

# 加载.npy文件
data = np.load(npy_file_path)

# 创建一个虚拟的raw对象，以获取'sfreq'信息
sfreq = 1000  # 替换为实际的采样频率
num_channels = 32  # 替换为实际的通道数
ch_names = [f'Channel {i + 1}' for i in range(num_channels)]
info = mne.create_info(ch_names, sfreq, ch_types='eeg')
raw = mne.io.RawArray(data, info)

# 获取数据的形状
num_channels, num_samples = data.shape

# 创建时间轴
time_axis = np.arange(0, num_samples) / raw.info['sfreq']

# 创建包含所有通道的子图
fig, axs = plt.subplots(num_channels, 1, sharex=True, figsize=(10, 2*num_channels))

# 绘制每个通道的数据
for channel in range(num_channels):
    axs[channel].plot(time_axis, data[channel, :])
    

# 添加标签和设置共享的x轴标签
axs[num_channels - 1].set_xlabel('Time (seconds)')

# 调整布局
plt.tight_layout()

# 显示绘图
plt.show()
