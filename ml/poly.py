import pandas
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import numpy as np

titanic = pandas.read_csv("/home/cooper/Downloads/UP-Hapur-Wheat-Price(2006-16)", delim_whitespace=True, header=None)
predictors = titanic[[9,10,11]]
val = titanic[8]
ar = np.polyfit(predictors,val,3)
print ar