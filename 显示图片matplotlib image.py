import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as img # mpimg 用于读取图片
import numpy as np

stinkbug = img.imread('/Users/wangzhao/Desktop/stinkbug.png')
# 读取目录下的 stinkbug.png
# 此时 stinkbug.png 就已经是一个 np.array 了，可以对它进行任意处理
stinkbug.shape 
plt.imshow(stinkbug) # 显示图片
plt.show()
