import pandas as pd
import numpy as np
from scipy.stats import shapiro, wasserstein_distance

# core functions to generating synthetic data
def split_db(df_toSplit, target_column):
    """
    Input: dataframe to be split and the Y column used to split the data into classes
    Function first eliminates unaffecting variables
    Then for each class in Y, samples are split into separate dataframes
    Output: dictionary where the keys correspond
    to the Y classifaction of samples and the items are the dataframes of samples
    """
    split_dfs = dict()
    print(f"Splitting dataframe based on {target_column}")
    if target_column in df_toSplit:
        n_unique = len(pd.unique(df_toSplit[target_column]))
        unique_classes = pd.unique(df_toSplit[target_column])
        print(f"Splitting into {n_unique} DataFrames of classes {unique_classes}")
        for i in range(n_unique):
            class_i = unique_classes[i]
            split_dfs[class_i] = df_toSplit.loc[df_toSplit[target_column]==unique_classes[i]]
    else:
        print("That target column doesn't exist in the DataFrame, pick another")
    return split_dfs

# for uncorrelated synthetic data
def mean_std_columns(df):
    """
    Collects mean and standard deviation of columns into dictionary: keys --> column names
                                                                     items -> tuple of (mean, std_dev)
    """
    column_stats = dict()
    for column in df.columns:
        column_stats[column] = df[column].mean(), df[column].std()
    return column_stats

# for correlated synthetic data
def mean_cov_columns(df):
    """
    Input: df of real samples
    Calculates 1D array of column means
    Retrieves 2D covariance matrix of the dist.
    Output: means, cov_matrix
    """
    column_means = []
    for column in df.columns:
        column_means.append(df[column].mean())
    cov_matrix = df.cov().to_numpy()

    return column_means, cov_matrix

def gen_synths_for_classValue(split_df_dict, target_col, target_value, n_samples, corr=True):
    """
    Inputs: dictionary of dfs which are separated by Y-class, the specific Y-class the function will handle
    and the number of total samples (real + synthetic) desired by the user
    Generates muliple synthetic samples, one at a time and complies them into a dataframe
    The index (sample_name) of each synthetic sample follows the syntax: SYNTH_{Y-class}_{n_synth}
    Outputs: synthetic df concatonated to original df of same Y-class (real + synths), just the synthetic df of Y-class
    """
    original_df = split_df_dict[target_value]
    odf_col_mean_cov = mean_cov_columns(original_df)
    odf_col_mean_std = mean_std_columns(original_df)
    synth_df = pd.DataFrame(columns=original_df.columns)

    if n_samples < len(original_df.index):
        print(f"Cannot generate less data than is already there for class {target_value}, increase n_samples")
    else:
        if corr:
            print(f"Generating {n_samples-len(original_df.index)} correlated synthetic data entries for class {target_value}")
            for i in range(n_samples - len(original_df.index)):
                synth_name = f"SYNTH_{target_value}_{i}"
                synth = gen_corr_synth_sample(original_df, target_col, target_value, odf_col_mean_cov[0],
                                              odf_col_mean_cov[1], synth_name)
                synth_df = pd.concat([synth_df, synth], axis=0)
        else:
            print(f"Generating {n_samples-len(original_df.index)} uncorrelated synthetic data entries for class {target_value}")
            for i in range(n_samples - len(original_df.index)):
                synth_name = f"SYNTH_{target_value}_{i}"
                synth = gen_synth_sample(original_df, target_col, target_value, odf_col_mean_std, synth_name)
                synth_df = pd.concat([synth_df, synth], axis=0)
    original_nd_synth_df = pd.concat([original_df, synth_df], axis=0)
    return original_nd_synth_df, synth_df


def gen_synth_sample(class_df, target_col, target_value, column_stats, sample_name):
    """
    Inputs: dataframe of specific Y-class, it's column (mean, std_dev)'s and a name for the genrated sample
    Generates a row/synthetic instance from sampling a normal distribution using (mean, std_dev) of each column
    The sample_name then becomes the index of the sample
    Output: single row df of the synthetic sample
    """
    sample_values = [sample_name]
    column_names = [class_df.index.name]
    for stat in column_stats:
        if stat != target_col:
            mean = column_stats[stat][0]
            std_dev = column_stats[stat][1]
            sampled_col_value = np.random.normal(mean, std_dev)
            sample_values.append(sampled_col_value)
            column_names.append(stat)
        else:
            sample_values.append(target_value)
            column_names.append(target_col)

    sample_df = pd.DataFrame([sample_values], columns=column_names)
    sample_df.set_index(sample_df.columns[0], inplace=True)
    return sample_df

# there is no need for the above and below functions to be separate
# they'd be more efficient if they were combined but sure look
def gen_corr_synth_sample(class_df, target_col, target_value, column_means, cov_matrix, sample_name):
    sample_values = [sample_name]
    column_names = [class_df.index.name]
    desc_values = np.random.multivariate_normal(column_means, cov_matrix, check_valid='ignore')
    desc_names = class_df.columns
    for i in range(len(desc_values)):
        if desc_names[i] != target_col:
            sample_values.append(desc_values[i])
            column_names.append(desc_names[i])
        else:
            sample_values.append(target_value)
            column_names.append(target_col)
    sample_df = pd.DataFrame([sample_values], columns=column_names)
    sample_df.set_index(sample_df.columns[0], inplace=True)
    return sample_df

# gen synths of a specified number (n_synths=300) of synthetic data
# for each target class (0,1). Can be correlate or
# uncorrelated (corr=True/False)
def gen_synths(df_to_gen, target_col, n_synths=200, corr=True):
    """
    Inputs: dataframe of multiple Y-classes, Y column of dataframe to base separation and generation of samples on,
    number of total samples (real + synthetic) desired by the user for each Y-class
    Splits dataframe into samples of specific Y-classes, generates synthetic compounds for each class and then
    recombines the total data into single dataframes
    Outputs: dataframe of both real and generated synthetic samples, dataframe of just synthetic samples
    """
    split_dfs = split_db(df_to_gen, target_col)
    df = pd.DataFrame(columns=split_dfs[0].columns)
    df_synth = pd.DataFrame(columns=split_dfs[0].columns)
    for target_activity in split_dfs:
        synth_real, synths = gen_synths_for_classValue(split_dfs, target_col, target_activity, n_synths, corr=corr)
        df = pd.concat([df, synth_real], axis=0)
        df_synth = pd.concat([df_synth, synths], axis=0)
#     print(f"Synthetic data generated")
    return df, df_synth
# tested: Paul

# generates synthetic samples for the minority class up
# to the number of the majority class
def gen_synths_balance(df_to_gen, target_col, corr=True):
    """
    Same as gen synths except the minimum amount of synthetic data is generated.
    It will measure the size of each split df and generate synths for the smaller one up to the number of the larger one
    Then concatenate as before
    As of now, can only work for binary classes, I don't like how it's hard-coded and I will change this in the future
    """
    split_dfs = split_db(df_to_gen, target_col)
    df = pd.DataFrame(columns=split_dfs[0].columns)
    df_synth = pd.DataFrame(columns=split_dfs[0].columns)
    if split_dfs[0].shape[0] > split_dfs[1].shape[0]:
        total_samples = split_dfs[0].shape[0]
        synths_real, synths = gen_synths_for_classValue(split_dfs, target_col, 1, total_samples, corr=corr)
        synths_real_plusOthrClass = pd.concat([synths_real, split_dfs[0]], axis=0)
        df = pd.concat([df, synths_real_plusOthrClass], axis=0)
    else:
        total_samples = split_dfs[1].shape[0]
        synths_real, synths = gen_synths_for_classValue(split_dfs, target_col, 0, total_samples, corr=corr)
        synths_real_plusOthrClass = pd.concat([synths_real, split_dfs[1]], axis=0)
        df = pd.concat([df, synths_real_plusOthrClass], axis=0)

    df_synth = pd.concat([df_synth, synths], axis=0)
    return df, df_synth

def gen_synths_expanded(df_to_gen, target_col, corr=True):
    split_dfs = split_db(df_to_gen, target_col)
    df = pd.DataFrame(columns=split_dfs[0].columns)
    df_synth = pd.DataFrame(columns=split_dfs[0].columns)

    if split_dfs[0].shape[0] > split_dfs[1].shape[0]:
        minority = 1
        majority = 0
    else:
        minority = 0
        majority = 1

    n_synths_minority = (2 * split_dfs[minority].shape[0])
    n_synths_majority = (split_dfs[majority].shape[0] * n_synths_minority)/(split_dfs[minority].shape[0]) # maintains active : inactive ratio

    minority_synths_real, minority_synths = gen_synths_for_classValue(split_dfs, target_col,
                                                                      minority, n_samples=n_synths_minority, corr=corr)
    df = pd.concat([df, minority_synths_real], axis=0)
    df_synth = pd.concat([df_synth, minority_synths], axis=0)

    majority_synths_real, majority_synths = gen_synths_for_classValue(split_dfs, target_col,
                                                                      majority, n_samples=n_synths_majority, corr=corr)
    df = pd.concat([df, majority_synths_real], axis=0)
    df_synth = pd.concat([df_synth, majority_synths], axis=0)

    return df, df_synth

def standardized_wasserstein_distance(a, b):
    """a and b are numpy arrays to compare distance between"""
    numerator = wasserstein_distance(a, b)
    denominator = np.std(np.concatenate([a,b]))
    return (numerator/denominator) if denominator != .0 else .0


def swd_feature_selection(X, y):  # Standardized Wasserstein Distance
    # split df into active and non-active
    # for each column compare distributions and get swd_score
    print("-----choose most different dist.-----")
    print("Original DB shape is", X.shape)
    active = X[y == True]
    nonactive = X[y == False]
    swd_scores = []
    for col in X.columns:
        swd_col = standardized_wasserstein_distance(active[col].to_numpy(), nonactive[col].to_numpy())
        swd_scores.append(swd_col)

    threshold = np.sort(swd_scores)[-101] + 0.0001
    to_drop = []
    for col in X.columns:
        col_idx = X.columns.get_loc(col)
        if swd_scores[col_idx] < threshold:
            to_drop.append(col)

    X = X.drop(to_drop, axis=1)
    print(f"Choosing 100 most different distributions using threshold {threshold}, DB shape now", X.shape)
    return X, to_drop

def normal_feature_selection(X, y):
    print("-----Eliminate features which are non-normal for active or inactive-----")
    print("Original DB shape is", X.shape)
    active = X[y==True]
    nonactive = X[y==False]
    to_drop = []
    for col in X.columns:
        stat_active, p_active = shapiro(active[col].to_numpy())
        stat_nonactive, p_nonactive = shapiro(nonactive[col].to_numpy())
        if (p_active <= 0.05) and (p_nonactive <= 0.05):
            to_drop.append(col)
    X = X.drop(to_drop, axis=1)
    print("Number of features reamining", X.shape)
    return X, to_drop