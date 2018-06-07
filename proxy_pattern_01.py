#!/usr/bin/env python
#!-*- coding: utf-8 -*-
'''
@desc: 代理模式，为其他对象提供一种代理以控制对特定对象的访问
@Author: wood
@date: 2018年6月7日17:20:00
'''

'''远程代理：为远程的对象提供代理
虚代理：根据需要创建很大的对象,即懒加载
保护代理：控制对原始对象的访问,用于具有不同访问权限的对象
'''

#代理其实本质上就是属性的委托
class Proxy(object):
    def __init__(self, subject):
        self.__subject = subject

    #python特性之一，用在查找实例属性的值时
    def __getattr__(self, name):
        return getattr(self.__subject, name)

class RGB(object):
    def __init__(self, red, green, blue):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def Red(self):
        return self.__red
    def Green(self):
        return self.__green
    def Blue(self):
        return self.__blue

#保护代理，拦截Blue属性的访问
# 子代理类拦截了Blue函数的访问，这样就不会返回被代理的类的Blue属性
class NoBlueProxy(Proxy):
    def Blue(self):
        return 0

# 保护代理，拦截Red属性的访问
# 子代理类拦截了Red函数的访问，这样就不会返回被代理的类的Red属性
class NoRedProxy(Proxy):
    def Red(self):
        return 0

# 保护代理，拦截Green属性的访问
# 子代理类拦截了Green函数的访问，这样就不会返回被代理的类的Green属性
class NoGreenProxy(Proxy):
    def Green(self):
        return 0

if __name__ == '__main__':
    rgb = RGB(100, 192, 240)
    print rgb.Red()
    print rgb.Blue()
    print rgb.Green()
    print "_________"
    noblue = NoBlueProxy(rgb)
    nored = NoRedProxy(rgb)
    nogreen = NoGreenProxy(rgb)
    print "Blue in NoBlueProxy: {0}".format(noblue.Blue())
    print "Green in NoGreenProxy: {0}".format(nogreen.Green())
    print "Red in NoBlueProxy: {0}".format(nored.Red())