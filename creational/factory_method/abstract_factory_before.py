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


class Computer:
    def __init__(self, config):
        self.config = config
    
    def assemble(self):
        if self.config == 'good':
            cpu = CPU(1000)
            disk = Disk('ssd')
        else:
            cpu = CPU(100)
            disk = Disk('harddrive')
        print cpu.get_price()
        print disk.get_config()


computer = Computer('good')
computer.assemble()