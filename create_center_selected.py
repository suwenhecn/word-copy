# -*- coding: utf-8 -*
import fileinput
import string
import math
import argparse
import os
import re
import sys
import unittest
import datetime
import time
import sys
import threading
def read_file(file_name):
    input_file=open(file_name)
    count=0
    gc_current=0
    name=[]#存放DNA的名称
    string=[]#存放DNA序列
    gc_per=[]
    current_string=[]
    line=input_file.readline()
    while 1:
        if not line:
            break
        if line[0]=='>':
            #is a name of DNA
            name.append(line[1:len(line)-1])
            line=input_file.readline()
            if not line:
                break
            while line and line[0]!='>' :
                current_string.append(line[0:len(line)-1])
                line=input_file.readline()
            string.append(current_string)
            current_string=[]
    maxx=0;
    loc=-1
    whole_string=[]
    tmp_string=[]
    for i in range(len(name)):
        whole_string.append(''.join(string[i]))
    input_file.close()
    return name,whole_string
def pair_value(a,b):
    if a==b :
        return 0
    elif a=='-' or b=='-':
        return 2
    elif a!=b:
        return 1
#def main():
def cal_sp(filename):
    name,sequence_set=read_file(filename)
    sp=0#average one
    row=len(sequence_set)
    col=len(sequence_set[0])
    #print row,col
    for i in range(col):
        sp_col=0
        for j in range(row-1):
            for k in range(j+1,row):
                sp_col+=pair_value(sequence_set[j][i],sequence_set[k][i])
        sp_col=sp_col/row
        sp+=sp_col
        #print sp_col
    #print "sp-average-score is ",sp
def create():
    filename="1x.fasta"
def main():
    #f=open("1x.fasta",'r')
    name,sequence_set=read_file("1x.fasta")
    for i in range(672):
        new_sequence_set=sequence_set
        center=new_sequence_set[i]
        new_sequence_set[i]=new_sequence_set[0]
        new_sequence_set[0]=center
        f=open("center_"+str(i),'w')
        for j in new_sequence_set:
            #f.write('>')
            f.write(">random_name\n");
            f.write(j+'\n')
        print("create file center_"+str(i))
        f.close()
def main2():
    pass
if __name__== "__main__":
    main()
