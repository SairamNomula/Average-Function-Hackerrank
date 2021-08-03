import math
import os
import random
import re
import sys



def avg(*num):
  if len(num)==0:
    return None
  sum_num += i
  for i in nums:
    sum_num += i
    ret = float(sum_num)/len(num)
  return(ret)
if __name__ = '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')
  nums = map(int, raw_input().split())
  res = avg(*nums)
  fptr.write('%.2f' % res + '\n')
  fptr.close()
