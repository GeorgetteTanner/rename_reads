#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:43:03 2021
@author: medgnt
"""

import argparse


parser = argparse.ArgumentParser(description='Rename reads in fastq file by adding a sequential number starting from 0 to the end of existing read names')
parser.add_argument('-i', '--input', dest='input', help='Input fastq file')
parser.add_argument('-o', '--output', dest='output', help='Output fastq file')
args = parser.parse_args()



with open(args.input,'r') as ifile:
    with open(args.output,'w+') as ofile:
        line=1
        i=1
        line=ifile.readline()
        while line:

            l=line.strip()
            ofile.write(l+'_'+str(i)+'\n')

            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()
            ofile.write(line)
            line=ifile.readline()

            i+=1
