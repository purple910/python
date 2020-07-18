"""
    @Time    : 2020/2/15 09:59
    @Author  : fate
    @Site    : 
    @File    : Dragon绘制实例.py
    @Software: PyCharm
"""
import tarfile
import os
import shutil
from mayavi import mlab

# http://graphics.stanford.edu/data/3Dscanrep/
dragon_tar_file = tarfile.open('E:\\MyDownloads\\dragon_recon.tar.gz')
try:
    os.mkdir("dragon_data")
except Exception as e:
    print(e)

dragon_tar_file.extractall("dragon_data")
dragon_tar_file.close()

dragon_ply_file = os.path.join("dragon_data", "dragon_recon", "dragon_vrip.ply")
mlab.pipeline.surface(mlab.pipeline.open(dragon_ply_file))
mlab.show()

shutil.rmtree("dragon_data")
