#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:29:46 2019

@author: matthiasboeker
SPCA Method

Description: 
    SPCA is a similarity measure for matrices and their eigenvalues and eigenvectors. 
    The so called cosine similiarity measures the angle between the eigenvectors of two correlation matrices
    The eigenvalues and eigenvectors of the correlations matrix are derived by PCA
    The function provides two methods: 
        1. SPCA
        2. Weighted SPCA
            While the normal SPCA weights every component are equal, the weighted SPCA assings the used components/eigenvectors
            a weight of their eigenvalue. The eigenvalue can be percieved as the explained variance of that component. 

    Function inputs
        df1 and df2: the two datasets to compare, datasets should be standardized beforehand 
        n_comp: number of principal components, integer from 1 to number of variables in dataset
        method: either 0 or 1 for SPCA or weighted SPCA
        
        


Based on the Paper of:
Pattern Matching in Historical Batch Data Using PCA, 
Author(s):Ashish Singhal & Dale E. Seborg
Between-Groups Comparison of Principal Components
Author(s): W. J. Krzanowski
"""


def SPCA(df1,df2,n_comp=3, method = 0):
    
    
    pca1 = PCA(n_components=n_comp)
    pca2 = PCA(n_components=n_comp)
    pca_fit1 = pca1.fit_transform(df1)
    pca_fit2 = pca2.fit_transform(df2)

    #Calculate the matrices of eigenvectors 

    pca_load_matrix1 = pca1.components_.T
    pca_load_matrix2 = pca2.components_.T
    
    # Get the eigenvalues of PCA
    eigenval1 = pca1.explained_variance_
    eigenval2 = pca2.explained_variance_
    
    # Square root of the eigenvalues 
    Sqrt_eigenval1 = np.sqrt(pca1.explained_variance_)
    Sqrt_eigenval2 = np.sqrt(pca2.explained_variance_)
                        
    #If method call is neither 0 or 1, throw Error to choose between SPCA and weighted SPCA
    if method not in [0,1]:
        print('Please select 0: normal SPCA or 1: weighted SPCA' )
    if method == 0:
        
        #Calculate matrix S = LM'ML' in order to get SPCA
        In = pca_load_matrix2@pca_load_matrix2.transpose()
        LIn = pca_load_matrix1.transpose()@In
        S = LIn@pca_load_matrix1
    
        #SPCA is the trace of S divided by the number of PCA_Components 
        SPCA = S.trace()/n_comp
    
        #SPCA is between 1 similiar and 0  dissimiliar
        return SPCA
    
    if method == 1:
    
        #Modified/ Eigenvalue Weighted SPCA

        #Create Eigenvalue Matrices A1 and A2
        eigenval_matrix1 = np.zeros(shape=(n_comp,n_comp))
        eigenval_matrix2 = np.zeros(shape=(n_comp,n_comp))
    
        np.fill_diagonal(eigenval_matrix1, Sqrt_eigenval1)
        np.fill_diagonal(eigenval_matrix2, Sqrt_eigenval2)
    
        #Modified Subset Matrices R and T 
            #R = LA1 and T = MA2
        
        R = pca_load_matrix1@eigenval_matrix1
        T = pca_load_matrix2@eigenval_matrix2
        
        #Calculate matris S modified S_mod = R'TT'R
        
        In_mod = T@T.transpose()
        LIn_mod = R.transpose()@In_mod
        S_mod = LIn_mod@R
   
        #Calculate the sum of the eigenvalue product
        sum_eigenval_prod = 0 
        for i in range(0,n_comp):
            sum_eigenval_prod = sum_eigenval_prod + (eigenval1[i]*eigenval2[i])
            
                
        #Calculate the final modified/ eigenvalue weighted SPCA
        SPCA_mod = S_mod.trace()/sum_eigenval_prod
        
        if SPCA_mod > 1:
            print('Error, SPCA is higher than 1! Standardize Data and try again!')
        else:
            return SPCA_mod 
                
                
                
    

