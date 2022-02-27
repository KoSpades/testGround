from sklearn.linear_model import LogisticRegression
import os
import numpy as np
from sklearn.metrics import accuracy_score, log_loss
import time
import sys

def get_test(test_dir='testing'):
    X_dir = os.path.join(test_dir, "test_X.npy")
    y_dir = os.path.join(test_dir, "test_y.npy")
    return np.load(X_dir), np.load(y_dir)

def get_train(train_dir='training', num=10):
    Xtrains = []
    ytrains = []
    for i in range(num):
        X_dir = os.path.join(train_dir, "train" + str(i) + "_X.npy")
        y_dir = os.path.join(train_dir, "train" + str(i) + "_y.npy")
        Xtrains.append(np.load(X_dir))
        ytrains.append(np.load(y_dir))
    
    X_train = np.concatenate(Xtrains)
    y_train = np.concatenate(ytrains)
    return X_train, y_train

def train_logistic(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def result(model, X_test, y_test):
    loss = log_loss(y_test, model.predict_proba(X_test))
    accuracy = model.score(X_test, y_test)
    return loss, accuracy

# Take in two directory names (and number of partitions) and print out results
# For this to work, it's assumed that those directories will contain the files that are needed
def get_prediction_accuracy(dir_train, dir_test, num_partition):
    dir_train = dir_train
    dir_test = dir_test
    n = num_partition
    xtrain, ytrain = get_train(train_dir=dir_train, num=n)
    xtest, ytest = get_test(test_dir=dir_test)
    start = time.time()
    model = train_logistic(xtrain, ytrain)
    end = time.time()
    print("Model train time is: ")
    print(end-start)
    loss, accuracy = result(model, xtest, ytest)
    # end = time.time()
    print("Prediction accuracy is " + str(accuracy))
    print("Runtime is " + str(end - start))


if __name__ == "__main__":
    # First we call get_prediction_accuracy for MNIST
    # get_prediction_accuracy("training_mnist", "testing_mnist", 8)
    # Then we call get_prediction_accuracy for income
    get_prediction_accuracy("training_income", "testing_income", 8)
