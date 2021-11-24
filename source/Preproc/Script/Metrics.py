# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:00:25 2020

@author: cipop
"""


import sys
from sklearn import metrics
import numpy

# =============================================================================
# auc
# =============================================================================

def auc(X, Y):
    X = eval(X)
    Y = eval(Y)
    try:
        auc = metrics.auc(X, Y)
        auc = auc.tolist()
        return str(auc)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# average_precision_score
# =============================================================================

def average_precision(y_true, y_scores, average, dtype_pos_label, pos_label, sample_weight):
    y_true = eval(y_true)
    y_scores = eval(y_scores)
    if average == 'None':
        average = None
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    if sample_weight == []:
        sample_weight = None
    try:
        average_precision_score = metrics.average_precision_score(y_true, y_scores, average, pos_label, sample_weight)
        average_precision_score = average_precision_score.tolist()
        return str(average_precision_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# balanced_accuracy_score
# =============================================================================

def balanced_accuracy_score(y_true, y_pred, sample_weight, adjusted):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    try:
        balanced_accuracy_score = metrics.balanced_accuracy_score(y_true, y_pred, sample_weight, adjusted)
        balanced_accuracy_score = balanced_accuracy_score.tolist()
        return str(balanced_accuracy_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# brier_score_loss
# =============================================================================

def brier_score_loss(y_true, y_prob, sample_weight, dtype_pos_label, pos_label):
    y_true = eval(y_true)
    y_prob = eval(y_prob)
    if sample_weight == []:
        sample_weight = None
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    elif dtype_pos_label == 'None':
        pos_label = None
    try:
        brier_score_loss = metrics.brier_score_loss(y_true, y_prob, sample_weight, pos_label)
        brier_score_loss = brier_score_loss.tolist()
        return str(brier_score_loss)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# classification_report
# =============================================================================

def classification_report(y_true, y_pred, labels, target_names, sample_weight, digits, output_dict, dtype_zero_division, zero_division):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if labels == []:
        labels = None
    if target_names == []:
        target_names = None
    if sample_weight == []:
        sample_weight = None
    if dtype_zero_division == 'int':
        zero_division = eval(zero_division)
    try:
        classification_report = metrics.classification_report(y_true, y_pred, labels, target_names, sample_weight, digits, output_dict, zero_division)
        return str(classification_report)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# cohen_kappa_score
# =============================================================================

def cohen_kappa_score(y1, y2, labels, weights, sample_weight):
    y1 = eval(y1)
    y2 = eval(y2)
    if labels == []:
        labels = None
    if sample_weight == []:
        sample_weight = None
    if weights == 'None':
        weights = None
    try:
        cohen_kappa_score = metrics.cohen_kappa_score(y1, y2, labels, weights, sample_weight)
        cohen_kappa_score = cohen_kappa_score.tolist()
        return str(cohen_kappa_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# fbeta_score
# =============================================================================

def fbeta_score(y_true , y_pred, beta, labels, dtype_pos_label, pos_label, average, sample_weight, dtype_zero_division, zero_division):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if labels == []:
        labels = None
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    if average == 'None':
        average = None
    if sample_weight == []:
        sample_weight = None
    if dtype_zero_division == 'int':
        zero_division = eval(zero_division)
    try:
        fbeta_score = metrics.fbeta_score(y_true , y_pred, beta, labels, pos_label, average, sample_weight, zero_division)
        fbeta_score = fbeta_score.tolist()
        return str(fbeta_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# hinge_loss
# =============================================================================

def hinge_loss(y_true, pred_decision, labels, sample_weight):
    y_true = eval(y_true)
    pred_decision = eval(pred_decision)
    if labels == []:
        labels = None
    if sample_weight == []:
        sample_weight = None
    try:
        hinge_loss = metrics.hinge_loss(y_true, pred_decision, labels, sample_weight)
        hinge_loss = hinge_loss.tolist()
        return str(hinge_loss)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# matthews_corrcoef
# =============================================================================

def matthews_corrcoef(y_true, y_pred, sample_weight):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    try:
        matthews_corrcoef = metrics.matthews_corrcoef(y_true, y_pred, sample_weight)
        matthews_corrcoef = matthews_corrcoef.tolist()
        return str(matthews_corrcoef)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# multilabel_confusion_matrix
# =============================================================================

def multilabel_confusion_matrix(y_true, y_pred, sample_weight, dtype_labels, labels, samplewise):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    if dtype_labels == 'None':
        labels = None
    elif dtype_labels == int:
        labels = exec(labels)
    else:
        pass
    try:
        multilabel_confusion_matrix = metrics.multilabel_confusion_matrix(y_true, y_pred, sample_weight, labels, samplewise)
        multilabel_confusion_matrix = multilabel_confusion_matrix.tolist()
        return str(multilabel_confusion_matrix)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# precision_recall_curve
# =============================================================================

def precision_recall_curve(y_true, probas_pred, dtype_pos_label, pos_label, sample_weight, returns):
    y_true = eval(y_true)
    probas_pred = eval(probas_pred)
    if sample_weight == []:
        sample_weight = None
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    elif dtype_pos_label == 'None':
        pos_label = None
    try:
        precision, recall, thresholds = metrics.precision_recall_curve(y_true, probas_pred, pos_label, sample_weight)
        if returns == 'precision':
            precision_recall_curve = precision.tolist()
            return str(precision_recall_curve)
        elif returns == 'recall':
            precision_recall_curve = recall.tolist()
            return str(precision_recall_curve)
        else:
            precision_recall_curve = thresholds.tolist()
            return str(precision_recall_curve)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# precision_recall_fscore_support
# =============================================================================

def precision_recall_fscore_support(y_true, y_pred, beta, labels, dtype_pos_label, pos_label, average, warn_for, sample_weight, dtype_zero_division, zero_division, returns):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if labels == [] or labels[0] == 'None':
        labels = None
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    if average == 'None':
        average = None
    if sample_weight == []:
        sample_weight = None
    if dtype_zero_division == 'int':
        zero_division = eval(zero_division)
    try:
        precision, recall, fbeta_score, support = metrics.precision_recall_fscore_support(y_true, y_pred, beta, labels, pos_label, average, warn_for, sample_weight, zero_division)
        if returns == 'precision':
            precision_recall_fscore_support = precision.tolist()
            return str(precision_recall_fscore_support)
        elif returns == 'recall':
            precision_recall_fscore_support = recall.tolist()
            return str(precision_recall_fscore_support)
        elif returns == 'fbeta_score':
            precision_recall_fscore_support = fbeta_score.tolist()
            return str(precision_recall_fscore_support)
        else: 
            precision_recall_fscore_support = support.tolist()
            return str(precision_recall_fscore_support)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# roc_auc_score
# =============================================================================

def roc_auc_score(y_true, y_score, average, sample_weight, max_fpr, multi_class, labels):
    y_true = eval(y_true)
    y_score = eval(y_score)
    if average == 'None':
        average = None
    if sample_weight == []:
        sample_weight = None
    if max_fpr == 'None':
        max_fpr = None
    else:
        max_fpr = eval(max_fpr)
    if labels == [] or labels[0] == 'None':
        labels = None
    try:
        roc_auc_score = metrics.roc_auc_score(y_true, y_score, average, sample_weight, max_fpr, multi_class, labels)
        roc_auc_score = roc_auc_score.tolist()
        return str(roc_auc_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# roc_curve
# =============================================================================

def roc_curve(y_true, y_score, dtype_pos_label, pos_label, sample_weight, drop_intermediate, returns):
    y_true = eval(y_true)
    y_score = eval(y_score)
    if dtype_pos_label == 'int':
        pos_label = eval(pos_label)
    if dtype_pos_label == 'None':
        pos_label = None
    if sample_weight == []:
        sample_weight = None
    try:
        fpr, tpr, thresholds = metrics.roc_curve(y_true, y_score, pos_label, sample_weight, drop_intermediate)
        if returns == 'fpr':
            roc_curve = fpr.tolist()
            return str(roc_curve)
        elif returns == 'tpr':
            roc_curve = tpr.tolist()
            return str(roc_curve)
        else:
            roc_curve = thresholds.tolist()
            return str(roc_curve)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# roc_curve
# =============================================================================

def zero_one_loss(y_true, y_pred, normalize, sample_weight):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    try:
        zero_one_loss = metrics.zero_one_loss(y_true, y_pred, normalize, sample_weight)
        zero_one_loss = zero_one_loss.tolist()
        return str(zero_one_loss)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# mean_poisson_deviance
# =============================================================================

def mean_poisson_deviance(y_true, y_pred, sample_weight):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    try:
        mean_poisson_deviance = metrics.mean_poisson_deviance(y_true, y_pred, sample_weight)
        mean_poisson_deviance = mean_poisson_deviance.tolist()
        return str(mean_poisson_deviance)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# mean_gamma_deviance
# =============================================================================

def mean_gamma_deviance(y_true, y_pred, sample_weight):
    y_true = eval(y_true)
    y_pred = eval(y_pred)
    if sample_weight == []:
        sample_weight = None
    try:
        mean_gamma_deviance = metrics.mean_gamma_deviance(y_true, y_pred, sample_weight)
        mean_gamma_deviance = mean_gamma_deviance.tolist()
        return str(mean_gamma_deviance)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# coverage_error
# =============================================================================

def coverage_error(y_true, y_score, sample_weight):
    y_true = eval(y_true)
    y_score = eval(y_score)
    if sample_weight == []:
        sample_weight = None
    try:
        coverage_error = metrics.coverage_error(y_true, y_score, sample_weight)
        coverage_error = coverage_error.tolist()
        return str(coverage_error)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# label_ranking_average_precision_score
# =============================================================================

def label_ranking_average_precision_score(y_true, y_score, sample_weight):
    y_true = eval(y_true)
    y_score = eval(y_score)
    if sample_weight == []:
        sample_weight = None
    try:
        label_ranking_average_precision_score = metrics.label_ranking_average_precision_score(y_true, y_score, sample_weight)
        label_ranking_average_precision_score = label_ranking_average_precision_score.tolist()
        return str(label_ranking_average_precision_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# label_ranking_loss
# =============================================================================

def label_ranking_loss(y_true, y_score, sample_weight):
    y_true = eval(y_true)
    y_score = eval(y_score)
    if sample_weight == []:
        sample_weight = None
    try:
        label_ranking_loss = metrics.label_ranking_loss(y_true, y_score, sample_weight)
        label_ranking_loss = label_ranking_loss.tolist()
        return str(label_ranking_loss)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# adjusted_mutual_info_score
# =============================================================================

def adjusted_mutual_info_score(labels_true, labels_pred, average_method):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        adjusted_mutual_info_score = metrics.adjusted_mutual_info_score(labels_true, labels_pred, average_method)
        adjusted_mutual_info_score = adjusted_mutual_info_score.tolist()
        return str(adjusted_mutual_info_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# adjusted_rand_score
# =============================================================================

def adjusted_rand_score(labels_true, labels_pred):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        adjusted_rand_score = metrics.adjusted_rand_score(labels_true, labels_pred)
        return str(adjusted_rand_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# calinski_harabasz_score
# =============================================================================

def calinski_harabasz_score(X, labels):
    X = eval(X)
    labels = eval(labels)
    try:
        calinski_harabasz_score = metrics.calinski_harabasz_score(X, labels)
        calinski_harabasz_score = calinski_harabasz_score.tolist()
        return str(calinski_harabasz_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# davies_bouldin_score
# =============================================================================

def davies_bouldin_score(X, labels):
    X = eval(X)
    labels = eval(labels)
    try:
        davies_bouldin_score = metrics.davies_bouldin_score(X, labels)
        davies_bouldin_score = davies_bouldin_score.tolist()
        return str(davies_bouldin_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# completeness_score
# =============================================================================

def completeness_score(labels_true, labels_pred):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        completeness_score = metrics.completeness_score(labels_true, labels_pred)
        completeness_score = completeness_score.tolist()
        return str(completeness_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# contingency_matrix
# =============================================================================

def contingency_matrix(labels_true, labels_pred, eps, sparses):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    if eps == 'None':
        eps = None
    else:
        eps = eval(eps)
    try:
        contingency_matrix = metrics.cluster.contingency_matrix(labels_true, labels_pred, eps, sparses)
        dtype = type(contingency_matrix)
        if dtype == numpy.ndarray:
            contingency_matrix = contingency_matrix.tolist()
            return str(contingency_matrix)
        else:
            Mat = contingency_matrix.tocoo()
            return str(list(zip(Mat.row, Mat.col, Mat.data)))
        return dtype
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# fowlkes_mallows_score
# =============================================================================

def fowlkes_mallows_score(labels_true, labels_pred, sparses):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        fowlkes_mallows_score = metrics.fowlkes_mallows_score(labels_true, labels_pred, sparses)
        fowlkes_mallows_score = fowlkes_mallows_score.tolist()
        return str(fowlkes_mallows_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# homogeneity_score
# =============================================================================

def homogeneity_score(labels_true, labels_pred):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        homogeneity_score = metrics.homogeneity_score(labels_true, labels_pred)
        homogeneity_score = homogeneity_score.tolist()
        return str(homogeneity_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# homogeneity_completeness_v_measure
# =============================================================================

def homogeneity_completeness_v_measure(labels_true, labels_pred, beta, returns):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        homogeneity, completeness, v_measure = metrics.homogeneity_completeness_v_measure(labels_true, labels_pred, beta)
        if returns == 'homogeneity':
            homogeneity_completeness_v_measure = homogeneity.tolist()
            return str(homogeneity_completeness_v_measure)
        elif returns == 'completeness':
            homogeneity_completeness_v_measure = completeness.tolist()
            return str(homogeneity_completeness_v_measure)
        else:
            homogeneity_completeness_v_measure = v_measure.tolist()
            return str(homogeneity_completeness_v_measure)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# mutual_info_score
# =============================================================================

def mutual_info_score(labels_true, labels_pred, contingency):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    if contingency == '':
        contingency = None
    else:
        contingency = eval(contingency)
    try:
        mutual_info_score = metrics.mutual_info_score(labels_true, labels_pred, contingency)
        mutual_info_score = mutual_info_score.tolist()
        return str(mutual_info_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message

# =============================================================================
# normalized_mutual_info_score
# =============================================================================

def normalized_mutual_info_score(labels_true, labels_pred, average_method):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        normalized_mutual_info_score = metrics.normalized_mutual_info_score(labels_true, labels_pred, average_method)
        normalized_mutual_info_score = normalized_mutual_info_score.tolist()
        return str(normalized_mutual_info_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# silhouette_score
# =============================================================================

def silhouette_score(X, labels, metric, sample_size, random_state):
    list_metric = ['precomputed', 'sqeuclidean', 'cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'nan_euclidean', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']
    X = eval(X)
    labels = eval(labels)
    if metric not in list_metric:
        metric = eval(metric) 
    if sample_size == 'None':
        sample_size = None
    if random_state == -1:
        random_state = None
    try:
        silhouette_score = metrics.silhouette_score(X, labels, metric, sample_size, random_state)
        silhouette_score = silhouette_score.tolist()
        return str(silhouette_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# silhouette_samples
# =============================================================================

def silhouette_samples(X, labels, metric):
    list_metric = ['precomputed', 'sqeuclidean', 'cityblock', 'cosine', 'euclidean', 'l1', 'l2', 'manhattan', 'nan_euclidean', 'braycurtis', 'canberra', 'chebyshev', 'correlation', 'dice', 'hamming', 'jaccard', 'kulsinski', 'mahalanobis', 'minkowski', 'rogerstanimoto', 'russellrao', 'seuclidean', 'sokalmichener', 'sokalsneath', 'sqeuclidean', 'yule']
    X = eval(X)
    labels = eval(labels)
    if metric not in list_metric:
        metric = eval(metric) 
    try:
        silhouette_samples = metrics.silhouette_samples(X, labels, metric)
        silhouette_samples = silhouette_samples.tolist()
        return str(silhouette_samples)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
# =============================================================================
# v_measure_score
# =============================================================================

def v_measure_score(labels_true, labels_pred, beta):
    labels_true = eval(labels_true)
    labels_pred = eval(labels_pred)
    try:
        v_measure_score = metrics.v_measure_score(labels_true, labels_pred, beta)
        v_measure_score = v_measure_score.tolist()
        return str(v_measure_score)
    except:
        erreur = sys.exc_info()
        typerr = u"%s" % (erreur[0])
        typerr = typerr[typerr.find("'")+1:typerr.rfind("'")]
        msgerr = u"%s" % (erreur[1])
        message = str('/!\\ {0} : {1}'. format(typerr,msgerr))
        return message
    
