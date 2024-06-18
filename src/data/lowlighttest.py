import os
from src.data import srdata

import glob

class LowLightTest(srdata.SRData):
    def __init__(self, args, name='LowLightTest', train=True, benchmark=False):
        super(LowLightTest, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _set_filesystem(self, dir_data):

        super(LowLightTest, self)._set_filesystem(dir_data)
        # self.apath = '../LOL/test'
        # print(self.apath)
        # self.dir_hr = os.path.join(self.apath, 'high')
        # self.dir_lr = os.path.join(self.apath, 'low')
        self.apath = '../LOL-v2/Real_captured/Test'
        print(self.apath)
        self.dir_hr = os.path.join(self.apath, 'high')
        self.dir_lr = os.path.join(self.apath, 'low')

    def _scan(self):
        names_hr, names_lr = super(LowLightTest, self)._scan()
        names_hr = names_hr[self.begin - 1:self.end]
        names_lr = names_lr[self.begin - 1:self.end]

        # list_hr, list_lr = super(LowLightTest, self)._scan()
        # print(f"HR files: {list_hr}")
        # print(f"LR files: {list_lr}")
        # list_hr = list_hr[self.begin:self.end]
        # list_lr = list_lr[self.begin:self.end]
        # # return list_hr, list_lr

        return names_hr, names_lr
