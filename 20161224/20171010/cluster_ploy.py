# '''
# Title : ploynomial
# @author: Marco
# Date: 20171014
# '''
# print (__doc__)
# #
# import numpy as np
# from sklearn.preprocessing import PolynomialFeatures
# X = np.arange(6).reshape(3,2)
# print X
# ploy = PolynomialFeatures(degree=2)
# ploy.fit_transform(X)
#
# #
# from sklearn.pipeline import Pipeline
# from sklearn.svm import SVC
# from sklearn.decomposition import PCA
# estimators = [('reduce_dim',PCA()),('clf',SVC())]
# pipe = Pipeline(estimators)
# print  pipe

#
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np
model = Pipeline([('poly',PolynomialFeatures(degree=3)),('linear',LinearRegression(fit_intercept=False))])
#fit to an order-3 ploynomial data
x = np.arange(5)
y = 3 - 2 * x + x ** 2 - x ** 3
model = model.fit(x[:,np.newaxis],y)
model.named_steps['linear'].coef_

