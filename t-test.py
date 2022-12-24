import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def t_test(data):

    significance_level = .05
    critical_t_val = 1.812

    ss1 = np.sum((data[0] - np.mean(data[0]))**2)
    ss2 = np.sum((data[1] - np.mean(data[1]))**2)

    df = len(data[0]) + len(data[1]) - 2

    pooled_variance = (ss1 + ss2) / df

    stdev = np.sqrt(pooled_variance * 2)

    st_error = stdev / np.sqrt(np.lcm(len(data[0]), len(data[1])))

    t_score = (np.mean(data[0]) - np.mean(data[1])) / st_error
    confidence_interval = np.zeros(2)
    
    confidence_interval[0] = (np.mean(data[0]) - np.mean(data[1])) + (st_error *2.228)
    confidence_interval[1] = (np.mean(data[0]) - np.mean(data[1])) - (st_error *2.228)
    cohens_d = np.mean(data[0]) - np.mean(data[1]) / stdev

    print("t-score: " + str(t_score))

    if(t_score > critical_t_val):
        print("Reject the null hypothesis at a .05 significance level\n")
        print("confidence intervals : " + str(confidence_interval[0]) + ", " + str(confidence_interval[1]))
        print("effect size (cohens d): " + str(cohens_d))
    else:
        print("Null hypothesis is retained at a .05 significance level")





sample_1 = np.array([12, 5, 11, 11, 9, 18])
sample_2 = np.array([7, 3, 4, 6, 3, 13])

joined_dataset = np.vstack((sample_1, sample_2))

t_test(joined_dataset)