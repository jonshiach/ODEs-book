#!/usr/bin/env python
# coding: utf-8

# # Chapter Summary
# 
# - The stage values in an [implicit Runge-Kutta method](irk-chapter) are defined using implicit functions.
# - The $A$ matrix of an implicit method has non-zero elements on the main diagonal or upper triangular region.
# - Implicit methods use fewer stages to achieve the same accuracy as explicit methods.
# - The [derivation of implicit methods](deriving-irk-methods-section) involves choosing values of $a_{ij}$, $b_i$ and $c_i$ to satisfy the [$B(k)$, $C(k)$ and $D(k)$ order conditions](Bk_Ck_Dk_order_conditions).
# - Implicit methods have better stability properties than explicit methods meaning they can be used to solve stiff ODEs with which explicit methods are unsuitable (see next chapter on [stability](stability-chapter));
# - Implicit methods require an [iterative method](solving-ivps-using-irk-methods-section) to calculate the stage values;
# - Implicit methods are more computationally expensive when applied to non-stiff methods than explicit methods.
