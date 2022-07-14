#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# The purpose of this book is to support teaching of the Runge-Kutta methods and computational linear algebra half of the unit Computational Methods in Ordinary Differential Equations which is taught by Jon Shiach. 
# 
# ## Learning and teaching
# 
# Having got to this stage in your studies you should already be familiar with the learning and teaching practices employed at undergraduate level. However, since this is a final year unit there will be certain expectations of the students from the teaching team. Our advice would be to try and stay on top of the material as much as possible and make sure you are completing the required number of hours of independent study outside of class time.
# 
# In order to successfully complete this unit students should:
# 
# - attend all of the lectures and tutorials;
# - complete all examples by yourself -- these notes contain the solutions to the examples which will be worked through in class, however, it is important that you write down the solutions as this will help you understand the material;
# - attempt all of the tutorial exercises;
# - if you are struggling, ask for help at the earliest opportunity.
# 
# In return the teaching team will:
# 
# - provide students with detailed lecture notes and other supporting material;
# - answer student queries regarding the material;
# - provide solutions/answers to worked examples and tutorial exercises;
# - provide formative feedback based on the tutorial exercises;
# - provide exam style questions for use as revision materials.
# 
# Most students find the step up to the final challenging and there will be times during the year that you may not fully understand all of the concepts being taught. In these situations we would advise you to read over the material again, follow the examples given and most importantly ask questions in lectures and tutorials. If there are gaps in your knowledge from previous years, you must make sure that you address these as there will not be much time to go over previous level material again.
# 
# 
# ## Teaching schedule
# 
# The teaching schedule for this part of the unit is as follows
# 
# | Week | Date (w/c) | Lecture | <div style="width:160px">Tutorial</div> |
# |:----:|:----------:|:--------|:---------|
# |  1   | 03/10/2022	| [**Initial Value Problems (IVPs)**](ivp-chapter):<br /> [Definition of an IVP](ivp-definition), the [Taylor series](taylor-series-section), the [Euler method](euler-method-definition), [error analysis](error-analysis-section), the [RK2 method](rk2-section), solving [higher order ODEs](higher-order-odes-section) | Exercises [1.1](ex1.1) to [1.5](ex1.5) |
# |  2   | 10/10/2022 | [**Explicit Runge-Kutta Methods (ERK)**](erk-chapter):<br /> [Definition of a Runge-Kutta method](rk-definition), the [Butcher tableau](butcher-tableau-definition), derivation of the [RK2](rk2-derivation-section) and [RK4](derivation-of-rk4-section) methods | Exercises [2.1](ex2.1) to [2.5](ex2.5) |
# |  3   | 24/10/2022 | [**Explicit Runge-Kutta Methods (ERK) cont**](erk-chapter):<br />  [Solving IVPs using ERK methods](applying-erk-methods-to-solve-ivps-section) | Exercises [2.6](ex2.6) to [2.11](ex2.11) |
# |  4   | 31/10/2022 | [**Implicit Runge-Kutta Methods (IRK)**](irk-chapter):<br /> [Order of an IRK method](order-of-irk-section), [deriving IRK methods](deriving-irk-methods-section), [solving IVPs using IRK methods](solving-ivps-using-irk-methods-section) | Exercises [3.1](ex3.1) to [3.5](ex3.5) |
# |  5   | 07/11/2022 | [**Stability**](stability-chapter): <br> [Definition of stability](stability-definition), [stiff ODEs](stiffness-section), [stability functions](stability-functions-section), [absolute stability](absolute-stability-definition), plotting the [region of absolute stability](plot-stability-region-section), [A-stability](a-stability-definition) | Exercises [4.1](ex4.1) to [4.4](ex4.4) |
# |  6   | 14/11/2022 | [**Boundary Value Problems (BVPS)**](bvp-chapter): <br> Definition, [existence and uniqeness of solutions](existence-and-uniqueness-of-bvp-solutions-section), the [shooting method](shooting-method-section), the [finite-difference method](finite-difference-method-section) | Exercises [5.1](ex5.1) to [5.5](ex5.5) |
# |  8   | 21/11/2022 | [**Direct methods**](direct-methods-chapter): <br> [LU decomposition](lu-section), [Crouts method](crouts-method-section), [LU decomposition with partial pivoting](lup-section) | Exercises [6.1](ex6.1) and [6.2](ex6.2) |
# |  9   | 28/11/2022 | [**Direct methods cont.**](cholesky-section): <br> [Cholesky decomposition](cholesky-section), [QR decomposition](qr-section), the [Gram-Schmidt process](qr-gram-schmidt-section), [Householder transformations](qr-householder-section) | Exercises [6.3](ex6.3) to [6.5](ex6.5) |
# | 10   | 05/12/2022 | [**Indirect methods**](indirect-methods-chapter): <br> [Jacobi](jacobi-method-section), [Gauss-Seidel](gauss-seidel-method-section) and [SOR](sor-method-section) methods,[convergence of indirect methods](convergence-of-indirect-methods-section) | Exercises [7.1](ex7.1) to [7.6](ex7.6) |
# | 11   | 12/12/2022 | **Consolidation and exam preparation** <br> **Coursework deadline 9pm on 16/12/2022** |
# 
# ## Python
# 
# This unit makes extensive use of Python to perform the computations. We encourage you to make sure you have your first year programming skills content to hand to act as a reference. If you do not have this you can download the content [here](https://github.com/drjonshiach/Programming_skills/archive/refs/heads/master.zip). There are numerous examples of Python programs in this book and of course the teaching team will be available during tutorials if you need some help.
# 
# ### Download and install Python on your computer
# 
# [Python](https://www.python.org/) is free for you to download and install on your own computer. There are many different ways which you can do this but perhaps the simplest is to download and install [Anaconda Navigator](https://www.anaconda.com/products/distribution). Anaconda is a suite of programs which includes Python and Jupyter Notebook which you can use to write Python programs.
# 
# ## Contact information
# 
# ```{image} Images/jon_Shiach.jpeg
# :alt: fishy
# :class: bg-primary mb-1
# :width: 100px
# :align: left
# ```
# 
# Dr Jon Shiach <br>
# Email: [j.shiach@mmu.ac.uk](mailto:j.shiach@mmu.ac.uk) <br>
# Tel: 0161 247 1515 <br>
# Office: E115b <br>
