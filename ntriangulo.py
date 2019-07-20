#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("\t--------------------------------------")
print("\t\tNÚMEROS TRIANGULARES\n")
print("\t--------------------------------------")                  
num=int(input("digite um numero\n"))
tri=0
i=0
while tri<num:
    tri=i*(i+1)*(i+2)
    i=i+1
if tri==num:
    print('%d é um número triangular' %num)
else:
    print('o numero não é triangular')
