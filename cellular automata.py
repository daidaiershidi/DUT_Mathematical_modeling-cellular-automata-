# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:09:45 2019

@author: dell
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib

listfuyi = []
listyi = []
listwu = []
listfuwu = []
list0 = []


def random_pick(some_list,probabilities):
  x=random.uniform(0,1)
  cumulative_probability=0.0
  for item,item_probability in zip(some_list,probabilities):
      cumulative_probability+=item_probability
      if x < cumulative_probability: break
  return item  
class GameOfLife(object): 
  def __init__(self, cells_shape):
    #初始化矩阵
        #按比例生成0,1,0.5，-0.5
    #按照条件更新
    #画图
    self.cells = np.zeros(cells_shape)
    #0->-1,1,0.5.-0.5的概率
    self.a = 0.05
    self.b = 0.3
    self.c = 0.3
    self.d = 0.35
    #-1->-1
    #1->-0.5,1
    self.w = 2
    self.e = 3
    #0.5->-0.5,1
    self.v = 2.5
    self.f = 0
    #-0.5->-1,-0.5
    self.n = 9
    
    self.k = 4
    #初始化
#    self.cells[1:-1, 1:-1] = np.random.randint(2, size=(cells_shape[0]-2, cells_shape[1]-2))
    for i in range(1, cells_shape[0] - 1):
      for j in range(1, cells_shape[0] - 1):
          self.cells[i][j] = random_pick([0,1],[0.9,0.1])
#    self.cells[0][0] = 1
#    self.cells[0][cells_shape[0]-1] = 1
#    self.cells[cells_shape[0]-1][0] = 1
#    self.cells[cells_shape[0]-1][cells_shape[0]-1] = 1 
    self.timer = 0
  def update_state(self):
    """更新一次状态"""
    buf = np.zeros(self.cells.shape)
    cells = self.cells
    for i in range(1, cells.shape[0] - 1):
      for j in range(1, cells.shape[0] - 1):
        # 计算该细胞周围的存活细胞数
        neighbor = cells[i-1:i+2, j-1:j+2].reshape((-1, ))
        neighbor = np.delete(neighbor, 4, axis=0)
        if(self.timer>self.k):
            if(cells[i, j]==0):
                if(neighbor.tolist().count(1)>1):
                    buf[i, j] = random_pick([-1, 1, 0.5, -0.5], [self.a, self.b, self.c, self.d])
                else:
                    buf[i, j] = 0
            if(cells[i, j]==1):
                if(neighbor.tolist().count(-1)>self.e):
                    buf[i, j] = -0.5
                if(np.sum(neighbor)<self.w):
                    buf[i, j] = -0.5
                else:
                    buf[i, j] = 1
            if(cells[i, j]==0.5):
                if(neighbor.tolist().count(-1)>self.f):
                    buf[i, j] = -0.5
                if(np.sum(neighbor)<self.v):
                    buf[i, j] = -0.5
                else:
                    buf[i, j] = 1
            if(cells[i, j]==-1):
                    buf[i, j] = -1
            if(cells[i, j]==-0.5):
                if(neighbor.tolist().count(-1)>self.n):
                    buf[i, j] = -1
                else:
                    buf[i, j] = -0.5   
        else:
            if(cells[i, j]==0):
                if(neighbor.tolist().count(1)>1):
                    buf[i, j] = random_pick([-1, 1, 0.5, -0.5], [self.a, self.b, self.c, self.d])
                else:
                    buf[i, j] = 0
            if(cells[i, j]==1):
                if(neighbor.tolist().count(-1)>self.e):
                    buf[i, j] = -0.5
                else:
                    buf[i, j] = 1
            if(cells[i, j]==0.5):
                if(neighbor.tolist().count(-1)>self.f):
                    buf[i, j] = -0.5
                else:
                    buf[i, j] = 0.5
            if(cells[i, j]==-1):
                    buf[i, j] = -1
            if(cells[i, j]==-0.5):
                    buf[i, j] = -0.5             
    self.cells = buf
    self.timer += 1
   
  def plot_state(self):
    """画出当前的状态"""
    plt.title('Iter :{}'.format(self.timer))
    plt.imshow(self.cells, prop_cycle=(cycler('color', ['r', 'g', 'b', 'y'])))
    plt.show()
 
  def update_and_plot(self, n_iter):
    """更新状态并画图
    Parameters
    ----------
    n_iter : 更新的轮数
    """
    plt.ion()
    for _ in range(n_iter):
#      print(self.cells)
      print(self.timer)  
      print('辟谣者（-1）：',self.cells.reshape((-1, )).tolist().count(-1))
      listfuyi.append(self.cells.reshape((-1, )).tolist().count(-1))
      print('不知情者（0）：',self.cells.reshape((-1, )).tolist().count(0))
      list0.append(self.cells.reshape((-1, )).tolist().count(0))
      print('传播者（1）：',self.cells.reshape((-1, )).tolist().count(1))
      listyi.append(self.cells.reshape((-1, )).tolist().count(1))
      print('将信将疑者（0.5）：',self.cells.reshape((-1, )).tolist().count(0.5))
      listwu.append(self.cells.reshape((-1, )).tolist().count(0.5))
      print('不信不传者（-0.5）：',self.cells.reshape((-1, )).tolist().count(-0.5))
      listfuwu.append(self.cells.reshape((-1, )).tolist().count(-0.5))
#      plt.title('Iter :{}'.format(self.timer))
      plt.imshow(self.cells)
      self.update_state()
      plt.pause(0.2)
    plt.ioff()
           
 
if __name__ == '__main__':
  game = GameOfLife(cells_shape=(100, 100))
  game.update_and_plot(20)
  matplotlib.rcParams['font.family'] = 'SimHei'  # 用来正常显示中文标签
  matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
  
  print(listyi)
  x = np.linspace(0, 20, 20)
  plt.plot(x, listfuyi, color ="r",label="辟谣者")
  plt.plot(x, listfuwu, color ="g",label="不信不传者")
  plt.plot(x, list0, color ="b",label="不知情者")
  plt.plot(x, listwu, color ="k",label="将信将疑者")
  plt.plot(x, listyi, color ="y",label="传播者")
  plt.xlabel('迭代次数T<20')
  plt.ylabel('元胞数')
  plt.legend()
  plt.show()
