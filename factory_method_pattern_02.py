#!/usr/bin/env python
#-*- coding: utf-8 -*-
'''
@desc: 使用工厂方法模式来生成不同的容量单位
@Author: wood
@date: Sat Sep  1 11:30:30 CST 2018
'''

class Base(object):

    def __init__(self, volume_num=0, volume_unit="B"):
        self._volume_num = volume_num
        self._volume_unit = volume_unit
        self._convert_base_vol()

    def __str__(self):
        return '<%s:%s>' % (self._volume_num, self._volume_unit)

    #转为高一级单位
    def upper_util(self):
        if self._base_vol_num >= 1024 ** 4:
            return '{0}{1}'.format(self._base_vol_num / (1024 ** 4), 'T')
        elif self._base_vol_num >= 1024 ** 3:
            return '{0}{1}'.format(self._base_vol_num / (1024 ** 3), 'G')
        elif self._base_vol_num >= 1024 ** 2:
            return '{0}{1}'.format(self._base_vol_num / (1024 ** 2), 'M')
        elif self._base_vol_num >= 1024 ** 1:
            return '{0}{1}'.format(self._base_vol_num / (1024), 'K')
        else:
            return "{0}{1}".format(self._base_vol_num, "B")

    #转为基本单位
    def lower_util(self):
        return "{0}{1}".format(self._base_vol_num, "B")

    def _convert_base_vol(self):
        pass

class Bvolume(Base):
    def __init__(self, volume_num):
        super(Bvolume, self).__init__(volume_num, 'B')

    def _convert_base_vol(self):
        self._base_vol_num = self._volume_num * 1

class Kvolume(Base):
    def __init__(self, volume_num):
        super(Kvolume, self).__init__(volume_num, 'K')

    def _convert_base_vol(self):
        self._base_vol_num = self._volume_num * 1024

class Mvolume(Base):
    def __init__(self, volume_num):
        super(Mvolume, self).__init__(volume_num, 'M')

    def _convert_base_vol(self):
        self._base_vol_num = self._volume_num * (1024 ** 2)

class Gvolume(Base):
    def __init__(self, volume_num):
        super(Gvolume, self).__init__(volume_num, 'G')

    def _convert_base_vol(self):
        self._base_vol_num = self._volume_num * (1024 ** 3)

class Tvolume(Base):
    def __init__(self, volume_num):
        super(Tolume, self).__init__(volume_num, 'T')

    def _convert_base_vol(self):
        self._base_vol_num = self._volume_num * (1024 ** 4)

class VolFactory(object):

    VOL_UNIT = {"B": Bvolume, "K": Kvolume, "M": Mvolume, "G": Gvolume, "T": Tvolume}

    def create_vol(self, volume_str):
        if isinstance(volume_str, str):
            #字符串转为大写
            volume_str = volume_str.upper()
            # 字符串倒数第一个字符
            volume_str_last_1 = volume_str[-1]
            # 字符串倒数第二个字符
            volume_str_last_2 = volume_str[-2]
            if volume_str_last_1 in self.VOL_UNIT and volume_str[0:-1].isdigit():
                return self.VOL_UNIT[volume_str_last_1](int(volume_str[0:-1]))
            elif volume_str_last_1 == 'B' and volume_str_last_2 in self.VOL_UNIT and volume_str[0:-2].isdigit():
                return self.VOL_UNIT[volume_str_last_2](int(volume_str[0:-2]))
            else:
                return None
        return None

if __name__ == '__main__':

    vol_factory = VolFactory()
    vol1 = vol_factory.create_vol("1020K")
    if vol1: print vol1.upper_util()

    vol2 = vol_factory.create_vol("2052b")
    if vol2: print vol2.upper_util()

    vol3 = vol_factory.create_vol("20500000Gb")
    if vol3: print vol3.upper_util()