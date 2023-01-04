from classification_utilities import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler

tr, ts, tr_target, ts_target = prepare_data(MinMaxScaler())

n_jobs = -1
print(f'Number of samples in Training set:', len(tr))
print(f'Number of samples in Test set:', len(ts))

parameters = {
    "n_estimators": range(30, 100, 20),
    "criterion": ["gini", "entropy"],  # , "log_loss"],
    "max_depth": [None] + list(range(5, 100, 20)),
    "min_samples_split": [2, 4],  # 2, 4, 8, 16, 32, 64],
    "min_samples_leaf": [16, 64],  # , 8, 16, 32, 64, 128],
    "max_features": ["auto", "sqrt", "log2", None],
    "max_leaf_nodes": [None] + list(range(3, 10, 2)),
    "min_impurity_decrease": [0.0] #, 0.1, 0.3]  # , 0.5]
}

# rf, results_df = grid_search(RandomForestClassifier, parameters, 'random_forest', tr, ts, tr_target, ts_target,
#                             n_jobs=n_jobs)
grid_search_with_feature_selection(RandomForestClassifier, parameters, 'random_forest', tr, ts, tr_target, ts_target,
                                   n_jobs=n_jobs, folds=4, n_features=25)

'''
parameters_linear = {
    'C': [1**(exp) for exp in [-2,-1,0,1,2,3,4]],
    'kernel': ['linear'],
    'shrinking': [True, False],
    'tol': [1e-8, 1e-4, 1e-2, 1e-1],
    'random_state': [42]
}

gamma_range = ['scale','auto'] + [1**(exp) for exp in [-3,-2,-1,0,1,2]]

parameters_poly = {
    **parameters_linear,
    'kernel': ['poly'],
    'degree': list(range(2,9)),
    'gamma': gamma_range,
}

parameters_rbf_sigmoid = {
    **parameters_linear,
    'kernel': ['rbf','sigmoid'],
    'gamma': gamma_range
}

grid_search(SVC, [parameters_linear,parameters_poly,parameters_rbf_sigmoid], 'svm', tr, ts, tr_target, ts_target, n_jobs=n_jobs)
'''
