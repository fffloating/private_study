# encoding=gbk
import math
import sys
import os
import numpy as np
import numpy
import torch

"""
class CPU:
    pass


class Dick:
    pass


class Computer:
    def __init__(self, cpu, dick):
        self.dick = cpu
        self.dick = dick


cpu1 = CPU()
cpu2 = cpu1
print(cpu2)
print(cpu1)


���¶���ӷ�__add__()

ϡ�����㷨����ϣ��
 ��sin_in  ��  sin_out
  P_in   P_out
  offset
  




class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


cpu1 = CPU()
cpu2 = cpu1
print(cpu2)
print(cpu1)

disk = Disk()
computer = Computer(cpu1, disk)

computer2 = copy.copy(computer)

print(computer, computer.disk, computer.cpu)
print(computer2, type(computer2.disk), computer2.cpu)




def add(a, b):
    return a+b


if __name__ == '__main__':
    print('������ְ�')
    print('�ҷǳ���ţ��')
    print('�������{}'.format(122))




file = open('requirements.txt', 'a')
file.write('laoxiezhenniubi')
file.close()

with open('requirements.txt', 'rb') as file:
    
"""


class DataTest:
    def __init__(self, id, address):
        self.id = id
        self.address = address
        self.d = {self.id: 1,
                  self.address: "192.168.1.1"
                  }

    def __getitem__(self, key):
        return "hello"


data = DataTest(1, "192.168.2.11")
print(data['ssda'])