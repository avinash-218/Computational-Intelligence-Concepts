import pandas as pd
import numpy as np

def calc_entropy(pos_cnt, neg_cnt):#to calc entropy value
  if(pos_cnt==0 or neg_cnt==0):#if positive or negative samples are 0 return 0
    return 0
  elif(pos_cnt==neg_cnt):#if possible and negative samples are equal in number return 1
    return 1  

  tot_cnt = pos_cnt + neg_cnt
  pos_val = (-pos_cnt/tot_cnt)*np.log2(pos_cnt/tot_cnt)
  neg_val = (-neg_cnt/tot_cnt)*np.log2(neg_cnt/tot_cnt)
  return round(pos_val+neg_val,3)

def count_total_positive(data):
  tot_val = dict()

  for i in data.columns[1:-1]:
    tot_val[i] = dict()
    tot_cnt = data.groupby([i])['PlayTennis'].count()#count of each category of ith column

    print(tot_cnt.index)

    for j in range(data[i].nunique()):
      tot_val[i][tot_cnt.index[j]] = [tot_cnt[j], 0]#total positive of each category of ith column

    df = data.groupby([i, 'PlayTennis'])[['PlayTennis']].count()#count of target for each category of each column
    print(df.index)

    l = len(df)
    for k in range(l):
      if(df.index[k][1]=='Yes'):
        tot_val[i][df.index[k][0]][1] = int(df.values[k])#positive

  print(tot_val)
  return tot_val

def calc_max_info_gain(tot_val):
  tot_len = len(data)
  tot_pos = data[data['PlayTennis']=='Yes']['PlayTennis'].count()#count total number of positives of all rows
  max_gain = -1
  root = ''

  for i in tot_val:
    s=0
    for j in tot_val[i].values():
      tot = j[0]
      pos = j[1]
      neg = tot - pos
      s+=calc_entropy(pos, neg) * ((pos+neg) / tot_len)#add entropy

    inf_gain = round(calc_entropy(tot_pos, tot_len-tot_pos) - s,4) #calc info gain
    print('{}: {}'.format(i, inf_gain))

    if(inf_gain>max_gain):#calc max info gain
      max_gain = inf_gain
      root = i

  return (max_gain, root)#return root node and info gain

if __name__=='__main__':
  data = pd.read_csv('Decision_Tree.csv') #read csv file
  print(data,end='\n\n')
  tot_val = count_total_positive(data)#count total and positive values for each category of each column and store in dict
  print()
  max_gain, root = calc_max_info_gain(tot_val)
  print('\nRoot Node:', root)
  print('Information Gain:', max_gain)