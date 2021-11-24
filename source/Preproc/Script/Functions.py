# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import datasets, feature_extraction, impute, kernel_approximation, metrics, model_selection, preprocessing, random_projection
from sklearn.metrics import pairwise

def Help_GroupKFold():
    return str(help(model_selection.GroupKFold))
    
def Help_GroupShuffleSplit():
    return str(help(model_selection.GroupShuffleSplit))

def Help_KFold():
    return str(help(model_selection.KFold))

def Help_LeaveOneGroupOut():
    return str(help(model_selection.LeaveOneGroupOut))

def Help_LeavePGroupsOut():
    return str(help(model_selection.LeavePGroupsOut))

def Help_LeaveOneOut():
    return str(help(model_selection.LeaveOneOut))

def Help_LeavePOut():
    return str(help(model_selection.LeavePOut))

def Help_PredefinedSplit():
    return str(help(model_selection.PredefinedSplit))

def Help_RepeatedKFold():
    return str(help(model_selection.RepeatedKFold))

def Help_RepeatedStratifiedKFold():
    return str(help(model_selection.RepeatedStratifiedKFold))

def Help_ShuffleSplit():
    return str(help(model_selection.ShuffleSplit))

def Help_StratifiedKFold():
    return str(help(model_selection.StratifiedKFold))

def Help_StratifiedShuffleSplit():
    return str(help(model_selection.StratifiedShuffleSplit))

def Help_TimeSeriesSplit():
    return str(help(model_selection.TimeSeriesSplit))

def Help_train_test_split():
    return str(help(model_selection.train_test_split))

def Help_ParameterGrid():
    return str(help(model_selection.ParameterGrid))

def Help_ParameterSampler():
    return str(help(model_selection.ParameterSampler))

 #-----------------------------------------------------------

def Help_adjusted_mutual_info_score():
    return str(help(metrics.adjusted_mutual_info_score))

def Help_adjusted_rand_score():
    return str(help(metrics.adjusted_rand_score))

def Help_auc():
    return str(help(metrics.auc))

def Help_average_precision_score():
    return str(help(metrics.average_precision_score))

def Help_balanced_accuracy_score():
    return str(help(metrics.balanced_accuracy_score))

def Help_brier_score_loss():
    return str(help(metrics.brier_score_loss))

def Help_classification_report():
    return str(help(metrics.classification_report))

def Help_calinski_harabasz_score():
    return str(help(metrics.calinski_harabasz_score))

def Help_cohen_kappa_score():
    return str(help(metrics.cohen_kappa_score))

def Help_completeness_score():
    return str(help(metrics.completeness_score))

def Help_contingency_matrix():
    return str(help(metrics.cluster.contingency_matrix))

def Help_coverage_error():
    return str(help(metrics.coverage_error))

def Help_davies_bouldin_score():
    return str(help(metrics.davies_bouldin_score))

def Help_fbeta_score():
    return str(help(metrics.fbeta_score))

def Help_fowlkes_mallows_score():
    return str(help(metrics.fowlkes_mallows_score))

def Help_hinge_loss():
    return str(help(metrics.hinge_loss))

def Help_homogeneity_completeness_v_measure():
    return str(help(metrics.homogeneity_completeness_v_measure))

def Help_homogeneity_score():
    return str(help(metrics.homogeneity_score))

def Help_label_ranking_average_precision_score():
    return str(help(metrics.label_ranking_average_precision_score))

def Help_label_ranking_loss():
    return str(help(metrics.label_ranking_loss))

def Help_matthews_corrcoef():
    return str(help(metrics.matthews_corrcoef))

def Help_mean_gamma_deviance():
    return str(help(metrics.mean_gamma_deviance))

def Help_mean_poisson_deviance():
    return str(help(metrics.mean_poisson_deviance))

def Help_multilabel_confusion_matrix():
    return str(help(metrics.multilabel_confusion_matrix))

def Help_mutual_info_score():
    return str(help(metrics.mutual_info_score))

def Help_normalized_mutual_info_score():
    return str(help(metrics.normalized_mutual_info_score))

def Help_precision_recall_curve():
    return str(help(metrics.precision_recall_curve))

def Help_precision_recall_fscore_support():
    return str(help(metrics.precision_recall_fscore_support))

def Help_roc_auc_score():
    return str(help(metrics.roc_auc_score))

def Help_roc_curve():
    return str(help(metrics.roc_curve))

def Help_zero_one_loss():
    return str(help(metrics.zero_one_loss))

def Help_silhouette_samples():
    return str(help(metrics.silhouette_samples))

def Help_silhouette_score():
    return str(help(metrics.silhouette_score))

def Help_v_measure_score():
    return str(help(metrics.v_measure_score))

 #-----------------------------------------------------------

def Help_CountVectorizer():
    return str(help(feature_extraction.text.CountVectorizer))

def Help_DictVectorizer():
    return str(help(feature_extraction.DictVectorizer))

def Help_extract_patches_2d():
    return str(help(feature_extraction.image.extract_patches_2d))

def Help_FeatureHasher():
    return str(help(feature_extraction.FeatureHasher))

def Help_HashingVectorizer():
    return str(help(feature_extraction.text.HashingVectorizer))

def Help_PatchExtractor():
    return str(help(feature_extraction.image.PatchExtractor))

def Help_reconstruct_from_patches_2d():
    return str(help(feature_extraction.image.reconstruct_from_patches_2d))

def Help_TfidfTransformer():
    return str(help(feature_extraction.text.TfidfTransformer))

def Help_TfidfVectorizer():
    return str(help(feature_extraction.text.TfidfVectorizer))

 #-----------------------------------------------------------

def Help_Binarizer(tests):
    test = help(preprocessing.Binarizer)
    return test

def Help_FunctionTransformer():
    return str(help(preprocessing.FunctionTransformer))

def Help_KBinsDiscretizer():
    return str(help(preprocessing.KBinsDiscretizer))

def Help_KernelCenterer():
    return str(help(preprocessing.KernelCenterer))

def Help_LabelBinarizer():
    return str(help(preprocessing.LabelBinarizer))

def Help_LabelEncoder():
    return str(help(preprocessing.LabelEncoder))

def Help_MultiLabelBinarizer():
    return str(help(preprocessing.MultiLabelBinarizer))

def Help_MaxAbsScaler():
    return str(help(preprocessing.MaxAbsScaler))

def Help_MinMaxScaler():
    return str(help(preprocessing.MinMaxScaler))

def Help_Normalizer():
    return str(help(preprocessing.Normalizer))

def Help_OneHotEncoder():
    return str(help(preprocessing.OneHotEncoder))

def Help_OrdinalEncoder():
    return str(help(preprocessing.OrdinalEncoder))

def Help_PolynomialFeatures():
    return str(help(preprocessing.PolynomialFeatures))

def Help_PowerTransformer():
    return str(help(preprocessing.PowerTransformer))

def Help_QuantileTransformer():
    return str(help(preprocessing.QuantileTransformer))

def Help_RobustScaler():
    return str(help(preprocessing.RobustScaler))

def Help_StandardScaler():
    return str(help(preprocessing.StandardScaler))

def Help_add_dummy_feature():
    return str(help(preprocessing.add_dummy_feature))

def Help_binarize():
    return str(help(preprocessing.binarize))

def Help_label_binarize():
    return str(help(preprocessing.label_binarize))

def Help_maxabs_scale():
    return str(help(preprocessing.maxabs_scale))

def Help_minmax_scale():
    return str(help(preprocessing.minmax_scale))

def Help_normalize():
    return str(help(preprocessing.normalize))

def Help_quantile_transform():
    return str(help(preprocessing.quantile_transform))

def Help_robust_scale():
    return str(help(preprocessing.robust_scale))

def Help_scale():
    return str(help(preprocessing.scale))

def Help_power_transform():
    return str(help(preprocessing.power_transform))

#-----------------------------------------------------------
 
def Help_SimpleImputer():
    return str(help(impute.SimpleImputer))

def Help_IterativeImputer():
    return str(help(impute.IterativeImputer))

def Help_MissingIndicator():
    return str(help(impute.MissingIndicator))

def Help_KNNImputer():
    return str(help(impute.KNNImputer))

#-----------------------------------------------------------

def Help_AdditiveChi2Sampler():
    return str(help(kernel_approximation.AdditiveChi2Sampler))

def Help_Nystroem():
    return str(help(kernel_approximation.Nystroem))

def Help_RBFSampler():
    return str(help(kernel_approximation.RBFSampler))

def Help_SkewedChi2Sampler():
    return str(help(kernel_approximation.SkewedChi2Sampler))

#-----------------------------------------------------------

def Help_johnson_lindenstrauss_min_dim():
    return str(help(random_projection.johnson_lindenstrauss_min_dim))

def Help_SparseRandomProjection():
    return str(help(random_projection.SparseRandomProjection))

def Help_GaussianRandomProjection():
    return str(help(random_projection.GaussianRandomProjection))

#-----------------------------------------------------------

def Help_additive_chi2_kernel():
    return str(help(metrics.pairwise.additive_chi2_kernel))

def Help_chi2_kernel():
    return str(help(metrics.pairwise.chi2_kernel))

def Help_cosine_distances():
    return str(help(metrics.pairwise.cosine_distances))

def Help_cosine_similarity():
    return str(help(metrics.pairwise.cosine_similarity))

def Help_euclidean_distances():
    return str(help(metrics.pairwise.euclidean_distances))

def Help_haversine_distances():
    return str(help(metrics.pairwise.haversine_distances))

def Help_laplacian_kernel():
    return str(help(metrics.pairwise.laplacian_kernel))

def Help_linear_kernel():
    return str(help(metrics.pairwise.linear_kernel))

def Help_manhattan_distances():
    return str(help(metrics.pairwise.manhattan_distances))

def Help_nan_euclidean_distances():
    return str(help(metrics.pairwise.nan_euclidean_distances))

def Help_pairwise_kernels():
    return str(help(metrics.pairwise.pairwise_kernels))

def Help_polynomial_kernel():
    return str(help(metrics.pairwise.polynomial_kernel))

def Help_rbf_kernel():
    return str(help(metrics.pairwise.rbf_kernel))

def Help_sigmoid_kernel():
    return str(help(metrics.pairwise.sigmoid_kernel))

def Help_paired_euclidean_distances():
    return str(help(metrics.pairwise.paired_euclidean_distances))

def Help_paired_manhattan_distances():
    return str(help(metrics.pairwise.paired_manhattan_distances))

def Help_paired_cosine_distances():
    return str(help(metrics.pairwise.paired_cosine_distances))

def Help_paired_distances():
    return str(help(metrics.pairwise.paired_distances))

def Help_pairwise_distances():
    return str(help(metrics.pairwise_distances))

def Help_pairwise_distances_argmin():
    return str(help(metrics.pairwise_distances_argmin))

def Help_pairwise_distances_argmin_min():
    return str(help(metrics.pairwise_distances_argmin_min))

def Help_pairwise_distances_chunked():
    return str(help(metrics.pairwise_distances_chunked))

#-----------------------------------------------------------
