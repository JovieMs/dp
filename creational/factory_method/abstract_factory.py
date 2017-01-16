#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CPU:
    def __init__(self, price):
        self.price = price

    def get_price(self):
        return self.price


class Disk:
    def __init__(self, config):
        """ssd or hard_disk"""
        self.config = config

    def get_config(self):
        return self.config


class GoodComputerFactory:
    def create_cpu(self):
        return CPU('1000')
    def create_disk(self):
        return Disk('ssd')

class BadComputerFactory:
    def create_cpu(self):
        return CPU('100')
    def create_disk(self):
        return Disk('harddrive')


class MediumComputerFactory:
    def create_cpu(self):
        return CPU('500')
    def create_disk(self):
        return Disk('harddrive')


def get_factory(config):
    if(config == 'good'):
        return GoodComputerFactory()
    elif(config == 'medium'):
        return MediumComputerFactory()
    else:
        return BadComputerFactory()


class Computer:
    def __init__(self, factory):
        self.cpu = factory.create_cpu()
        self.disk = factory.create_disk()
    
    def assemble(self):
        print self.cpu.get_price()
        print self.disk.get_config()


my_factory = get_factory('medium')
computer = Computer(my_factory)
computer.assemble()