import pandas
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import numpy as np

titanic = pandas.read_csv("/home/cooper/Downloads/UP-Hapur-Wheat-Price(2006-16)", delim_whitespace=True, header=None)
predictors = [9, 10, 11]
alg = LinearRegression()
kf = KFold(titanic.shape[0], n_folds=3, random_state=1)
predictions = []
for train, test in kf:
    # The predictors we're using the train the algorithm.  Note how we only take the rows in the train folds.
    train_predictors = (titanic[predictors].iloc[train, :])
    # The target we're using to train the algorithm.
    train_target = titanic[8].iloc[train]
    # Training the algorithm using the predictors and target.
    alg.fit(train_predictors, train_target)
    # We can now make predictions on the test fold
    test_predictions = alg.predict(titanic[predictors].iloc[test, :])
    predictions.append(test_predictions)
# print predictions
predictions = np.concatenate(predictions, axis=0)
tt = pandas.read_csv("/home/cooper/PycharmProjects/cam_calib/test.txt",delim_whitespace= True, header=None)
new_predictions = []
test_new_predictors = alg.predict(tt[[0,1,2]])
new_predictions.append(test_new_predictors)
predict = np.concatenate(new_predictions,axis=0)
f = open("result.txt","w")
d = 1
m = 9
y = 2016
count = 0
while y<2019:
    if d<31:
        f.write(str(d))
        f.write(" ")
        if m<13:
            f.write(str(m))
            f.write(" ")
            if y<2019:
                f.write(str(y))
                f.write(" ")
                f.write(str(predict[count]))
                f.write("\n")
                d = d + 1
                count +=1
        else:
            m=1
            y += 1
    else:
        m = m+1
        d=1
f.close()


'''sum = 0
i = 0
while i != 25:
    print predictions[i]
    print titanic[8][i]
    if predictions[i] == titanic[8][i]:
        sum += 1
    i += 1

print sum
accuracy = sum / len(predictions)
print accuracy '''

'''accuracy = sum(predictions) / len(predictions)
print sum(predictions)
print len(predictions)
print accuracy'''
