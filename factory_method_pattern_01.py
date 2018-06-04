#!/usr/bin/env python
#!-*- coding: utf-8 -*-
'''
@desc: 使用工厂方法模式
@Author: wood
@date: 2018年6月4日14:50:00
'''

'''
工厂方法用于屏蔽对象创建的细节，客户端调用时无需知道对象的创建细节；
定义一个用于创建对象的接口，让子类决定实例化哪一个类其，使一个类的实例化延迟到其子类；
'''

'''Animal基类
'''
class Animal(object):

    def __init__(self):
        pass

    def eat(self):
        pass

    def drink(self):
        pass

'''Animal子类
'''
class CatAnimal(Animal):

    def __init__(self, name=''):
        self.name = name
        super(Animal, self).__init__()

    def eat(self):
        print "{0} eat fish".format(self.name)

    def drink(self):
        print "{0} drinking".format(self.name)

'''Animal子类
'''
class DogAnimal(Animal):

    def __init__(self, name=''):
        self.name = name
        super(Animal, self).__init__()

    def eat(self):
        print "{0} eat dog food".format(self.name)

    def drink(self):
        print "{0} drinking".format(self.name)

'''工厂基类，以生成产品类
'''
class AnimalFactory(object):

    def __init__(self):
        pass

    def create_animal(self):
        pass

class CatAnimalFactory(AnimalFactory):

    def __init__(self):
        pass

    def create_animal(self, name=''):
        return CatAnimal(name=name)

class DogAnimalFactory(AnimalFactory):

    def __init__(self):
        pass

    def create_animal(self, name=''):
        return DogAnimal(name=name)

catF = CatAnimalFactory()
dogF = DogAnimalFactory()

animalList = list()
cat1 = catF.create_animal(name='cat1')
cat2 = catF.create_animal(name='cat2')

dog1 = dogF.create_animal(name='dog1')
dog2 = dogF.create_animal(name='dog2')

animalList.append(cat1)
animalList.append(cat2)
animalList.append(dog1)
animalList.append(dog2)

for ani in animalList:
     ani.eat()