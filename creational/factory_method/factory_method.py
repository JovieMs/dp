#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Dog:
    def __init__(self):
        print 'A dog is instantiated'

    def speak(self):
        print 'Dog says wawa'


class Cat:
    def __init__(self):
        print 'A cat is instantiated'

    def speak(self):
        print 'Cat says miaomiao'


def create_pet(name):
    pet_dict = {
        'cat': Cat,
        'dog': Dog
    }
    return pet_dict[name]()


pets = map(create_pet, ['cat', 'dog'])

for pet in pets:
    pet.speak()
