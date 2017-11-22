# -*- coding: utf-8 -*-
from sklearn import linear_model
from sklearn.metrics import mean_squared_error,r2_score # mse and r square
regr = linear_model.LinearRegression() # find LR funciton
# 训练模型
regr.fit(x,y) # where x is train ,y is  targert train set
regr.coef_  # regr coefficient
# 使用模型
obj_goal = regr.predict(X)  # X is need predict set




