'''
autor:zhaoyli
date:2020/5/23
purpose:mean the muti channel(feature map) to one channel(featrue map),But I don't know what this operation does. hhh...

'''
import torch

def  Mean_F(x):
    final_list = [ ]
    for i in range(x.size(0)):
        sum_f = torch.zeros((x.size(2),x.size(3)))
        for j in range(x.size(1)):
            f = x[i,j,:,:]
            sum_f += f
        mean_f = torch.div(sum_f,x.size(1))
        final_list.append(mean_f)
    return final_list

if __name__ == '__main__':

    x = torch.arange(0,16).reshape((2,2,2,2))
    y = Mean_F(x)
    print(y)
    print(len(y))# y的个数等于x.size(0)