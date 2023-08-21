#!/usr/bin/env python
# coding: utf-8

# # Module 1: What is Numerical Analysis? 
# 
# ## Intro to Numerical Analysis

# ```{note}
# Song Accompanying This Section: [Are You Bored Yet? - Wallows, Clairo, Big Data](https://open.spotify.com/track/20uK28tZcFs3sGXKlCFVSJ?si=ecabd85ad5e742a2)
# ```

# > In the 1950s and 1960s, the founding fathers of Numerical Analysis discovered that inexact arithmetic can be a source of danger, causing errors in results that 'ought' to be right. The source of such problems is numerical instability: that is, the amplification of rounding errors from microscopic to macroscopic scale by certain modes of computation.''
# 
# **[Oxford Professor Lloyd (Nick) Trefethen (2006)](https://en.wikipedia.org/wiki/Nick_Trefethen)**

# The field of Numerical Analysis is really the study of how to take mathematical problems and perform them efficiently and accurately on a computer. While the field of numerical analysis is quite powerful and wide-reaching, there are some mathematical problems where numerical analysis doesn’t make much sense (e.g. finding an algebraic derivative of a function, proving a theorem, uncovering a pattern in a sequence). However, for many problems a numerical method that gives an approximate answer is both more efficient and more versatile than any analytic technique. Let’s look at several examples. You can also watch a short introduction video here: https://youtu.be/yH0zhca0hbs

# **Example from Algebra:**
# 
# Solve the equation $\ln(x)=\sin(x)$ for $x$ in the interval 
# $x \in (0,\pi)$. Stop and think about all of the algebra that you ever learned. You’ll quickly realize that there are no by-hand techniques that can solve this problem! A numerical approximation, however, is not so hard to come by.

# **Example from Calculus:**
# 
# What if we want to evaluate the following integral?
# 
# $$
# \int\limits^{\pi}_{0} \sin(x^2) \;dx
# $$
# 
# Again, trying to use any of the possible techniques for using the Fundamental Theorem of Calculus, and hence finding an antiderivative, on the function $\sin(x^2)$ is completely hopeless. Substitution, integration by parts, and all of the other techniques that you know will all fail. Again, a numerical approximation is not so difficult and is very fast! By the way, this integral (called the [Fresnel Sine Integral](https://en.wikipedia.org/wiki/Fresnel_integral)) actually shows up naturally in the field of optics and electromagnetism, so it is not just some arbitrary integral that I cooked up just for fun.

# **Example from Differential Equations:**
# 
# Say we needed to solve the differential equation $\frac{dy}{dt} = \sin(y^2) + t$. The nonlinear nature of the problem precludes us from using most of the typical techniques (e.g. separation of variables, undetermined coefficients, Laplace Transforms, etc). However, computational methods that result in a plot of an approximate solution can be made very quickly and likely give enough of a solution to be usable.

# **Example from Linear Algebra:**
# 
# You have probably never row reduced a matrix larger than $3 \times 3$ or perhaps $4 \times 4$ by hand. Instead, you often turn to technology to do the row reduction for you. You would be surprised to find that the standard row reduction algorithm (RREF) that you do by hand is not what a computer uses. Instead, there are efficient algorithms to do the basic operations of linear algebra (e.g. Gaussian elimination, matrix factorization, or eigenvalue decomposition)

# In this chapter we will discuss some of the basic underlying ideas in Numerical Analysis, and the essence of the above quote from Nick Trefethen will be part of the focus of this chapter.
# Particularly, we need to know how a computer stores numbers and when that storage can get us into trouble.  On a more mathematical side, we offer a brief review of the Taylor
# Series from Calculus at the end of this chapter. The Taylor Series underpins many of our approximation methods in
# this class.  Finally, at the end of this chapter we provide several coding exercises that will help you to develop your programming skills.
# 
# Let's begin.

# ## Arithmetic in Base 2
# 
# 
# **Exercise 1.1** By hand (no computers!) compute the first 50 terms of this sequence with the initial condition $x_0 = 1/10$.
# 
# $$
# x_{n+1} = \left\{ \begin{array}{ll} 2x_n, & x_n \in [0,\frac{1}{2}] \\ 2x_n - 1, & x_n \in (\frac{1}{2},1] \end{array} \right.
# $$
# 
# **Exercise 1.2**
# Now use a spreadhseet and to do the computations. Do you get the same answers? 
# 
# **Exercise 1.3**
# Finally, solve this problem with Python. Some starter code is given to you below.
# 
# ```python
# x = 1.0/10
# for n in range(50):
#     if x<= 0.5:
#         # put the correct assignment here
#     else:
#         # put the correct assigment here
#     print(x)
# ```

# **Exercise 1.4**
# What do you notice? What do you think happened on the computer and why did it give you a different answer?  What, do you suppose, is the cautionary tale hiding behind the scenes with this problem?
# 
# **Exercise 1.5**
# Now what happens with this problem when you start with $x_0 = 1/8$?  

# A computer circuit knows two states: on and off.  As such, anything saved in computer
# memory is stored using base-2 numbers.  This is called a binary number system.  To fully
# understand a binary number system it is worth while to pause and reflect on our base-10
# number system for a few moments. These binary digits are called bits, and are the basis of the binary representation of numbers.
# 
# What do the digits in the number ``$735$'' really mean?  The position of each digit tells
# us something particular about the magnitude of the overall number.  The number $735$ can
# be represented as a sum of powers of $10$ as
# 
# $$
# 735 = 700 + 30 + 5 =  7 \times 10^2 + 3 \times 10^1 + 5 \times 10^0
# $$
# 
# and we can read this number as $7$ hundreds, $3$ tens, and $5$ ones.
# As you can see, in a ''positional number system'' such as our base-10 system, the
# position of the number indicates the power of the base, and the value of the digit itself
# tells you the multiplier of that power.  This is contrary to number systems like Roman
# Numerals where the symbols themselves give us the number, and meaning of the position is
# somewhat flexible. The number ''48,329'' can therefore be interpreted as
# 
# $$
# 48,329 = 40,000 + 8,000 + 300 + 20 + 9 = 4 \times 10^4 + 8 \times 10^3 + 3 \times 10^2 + 2
# \times 10^1 + 9 \times 10^0,
# $$
# 
# Four ten thousands, eight thousands, three hundreds, two tens, and nine ones.
# 
# Now let's switch to the number system used by computers: the binary number system.  In a
# binary number system the base is 2 so the only allowable digits are 0 and 1 (just like in
# base-10 the allowable digits were 0 through 9).  In binary (base-2), the number ''$101,101$'' can be interpreted as
# 
# $$
# 101,101_2 = 1 \times 2^5 + 0 \times 2^4 + 1 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1
# \times 2^0
# $$
# 
# (where the subscript ''2'' indicates the base to the reader). If we put this back into base 10, so that we can read it more comfortably, we get
# 
# $$
# 101,101_2 = 32 + 0 + 8 + 4 + 0 + 1 = 45_{10}.
# $$
# 
# The reader should take note that the commas in the numbers are only to allow for greater
# readability -- we can easily see groups of three digits and mentally keep track of what
# we're reading.

# **Exercise 1.6** Express the following binary numbers in base-10.
# 
# * (a) $111_2$
# * (b) $10,101_2$
# * (c) $1,111,111,111_2$
# 
# **Exercise 1.7**
# Discussion: With your group discuss how you would convert a base-10 number into its binary representation.  Once you have a proposed method put it into action on the number $237_{10}$ who's base-2 expression is $11,101,101_2$?
# 
# **Exercise 1.8**
# Convert to following numbers from base 10 to base 2 or visa versa.
# 
# * Write $12_{10}$ in binary             
# 
# * Write $11_{10}$ in binary 
# 
# 
# **Exercise 1.10**
# Now that you have converted several base-10 numbers to base-2, summarize an efficient technique to do the conversion.

# **Example 1.1**
# 
# Convert the number 137 from base 10 to base 2. 
# 
# **Solution:** One way to do the conversion is to first look for the largest power of 2 less than or equal to your number.  In this case, $128=2^7$ is the largest power of 2 that is less than 137. Then looking at the remainder, 9, look for the largest power of 2 that is less than this remainder. Repeat until you have the number. 
# 
# \begin{align*}
#         137_{10} &= 128 + 8 + 1 \\
#         &= 2^7 + 2^3 + 2^0 \\
#         &= 1 \times 2^7 + 0 \times 2^6 + 0 \times 2^5  + 0 \times 2^4  + 1 \times 2^3  + 0
#         \times 2^2  + 0 \times 2^1  + 1 \times 2^0  \\
#         &= 10001001_2
# \end{align*}
# 
# Next we'll work with fractions and decimals.  For example, let's take the base 10 number
# $5.341_{10}$ and expand it out to get
# 
# $$
# 5.341_{10} = 5 + \frac{3}{10} + \frac{4}{100} + \frac{1}{1000} = 5 \times 10^0 + 3 \times
# 10^{-1} + 4 \times 10^{-2} + 1 \times 10^{-3}.
# $$
# 
# The position to the right of the decimal point is the negative power of 10 for the given position. We can do a similar thing with binary decimals.

# **Practice**
# 
# Convert the base 10 decimal $0.635$ to binary using the following steps. 
# 
# * Multiply $0.635$ by 2.  The whole number part of the result is the first binary digit to the right of the decimal point. 
# * Take the result of the previous multiplication and ignore the digit to the left of the decimal point. Multiply the remaining decimal by 2.  The whole number part is the second binary decimal digit. 
# * Repeat the previous step until you have nothing left, until a repeating pattern has revealed itself, or until your precision is close enough.
# 
# Explain why each step gives the binary digit that it does.

# ## Floating Point Arithmetic
# 
# Everything stored in the memory of a computer is a number, but how does a computer
# actually store a number?  More specifically, since computers only have finite memory we
# would really like to know the full range of numbers that are possible to store in a
# computer. Since there is a finite space in a computer, we can only ever store rational numbers (why?). Therefore, we need to know what gaps in our number system to expect when using a computer to store and do computations on numbers.

# --- 
# Consider the number $x = -129.15625$ (in base 10).  This number can be converted into binary,
# 
# $$
# x = -123.15625_{10} = -1111011.00101_2
# $$
# (you should check this).  
# 
# * If a computer needs to store this number, we need the binary version of scientific notation.  In this case, we write 
# 
# $$
# x = -1. \underline{\hspace{1in}} \times 2^{\underline{\hspace{0.25in}}}
# $$
# 
# * Based on the fact that every binary number, other than 0, can bewritten in this way, what three things do you suppose a computer needs to store for any given number?
# * What would a computer need to store forthe binary number $x=10001001.1100110011_2$?

# ---
# 
# ```{note}
# For any base-2 number $x$ we can write
# 
# $$
# x = (-1)^{s} \times (1+ m) \times 2^E
# $$
# 
# 
# where $s \in \{0,1\}$ is called the *sign bit* and $m$ is a binary number such that $0
# \le m < 1$.
# 
# For a number $x = (-1)^{s} \times (1+m) \times 2^E$ stored in a computer, the number $m$ is called the **mantissa** or the **significand**, $s$ is known as the sign bit, and $E$ is known as the exponent.
# ```

# **Example**
# 
# What are the mantissa, sign bit, and exponent for the numbers $7_{10}$, $-7_{10}$, and $(0.1)_{10}$? 

# ---
# In the last part of the previous example we saw that the number $(0.1)_{10}$ is actually a
# repeating decimal in base-2.  This means that in order to completely represent the number
# $(0.1)_{10}$ in base-2, we need infinitely many decimal places.  Obviously that can't
# happen since we are dealing with computers with finite memory.  Over the course of the
# past several decades there have been many systems developed to properly store numbers.
# The IEEE standard that we now use is the accumulated effort of many computer scientists,
# much trial and error, and deep scientific research.  We now have three standard precisions
# for storing numbers on a computer: single, double, and extended precision.  The double
# precision standard is what most of our modern computers use.
# 
# ---

# ```{note}
# There are three standard precisions for storing numbers in a computer.
#  * A **single-precision** number consists of 32 bits, with 1 bit for the sign, 8 for the exponent, and 23 for the significand.
#  * A **double-precision** number consists of 64 bits with 1 bit for the sign, 11 for the exponent, and 52 for the significand.
#  * An **extended-precision** number consists of 80 bits, with 1 bit for the sign, 15 for the exponent, and 64 for the significand.
# ```

# ---
# 
# **Machine precision** is the gap between the number 1 and the next larger floating point number. Often it is represented by the symbol $\epsilon$. To clarify, the number 1 can always be stored in a computer system exactly and if $\epsilon$ is machine precision for that computer then $1+\epsilon$ is the next largest number that can be stored with that machine. 

# For all practical purposes the computer cannot tell the difference between two numbers if the difference is smaller than machine precision. This is of the utmost important when you want to check that something is "zero" since a computer just cannot know the difference between $0$ and $\epsilon$.

# **Exercise 1.11** To make all of these ideas concrete, let's consider with a small computer system where each number is stored in the following format:
# 
# $$
# s\; E\; b_1 b_2 b_3
# $$
# 
# The first entry is a bit for the sign (0$=+$ and $1=-$). The second entry, $E$ is for the exponent, and we'll assume in this example that the exponent can be 0, 1, or -1. The three bits on the right represent the significand of the number.  Hence, every number in this number system takes the form
# 
# $$
# (-1)^s \times (1+ 0.b_1b_2b_3) \times 2^{E}
# $$
# 
# * What is the smallest positive number that can be represented in this form?
# * What is the largest positive number that can be represented in this form?
# * What is the machine precision in this number system? 
# * What would change if we allowed $E \in \{-2,-1,0,1,2\}$?

# **Exercise 1.12** What are the largest and smallest numbers that can be stored in single and double
#     precicision?
# 
# 
# **Exercise 1.13** Explain the behavior of the sequence from the first problem in these notes using what you know about how computers store numbers in double precision.
# 
# $$
# x_{n+1} = \left\{ \begin{array}{ll} 2x_n, & x_n \in [0,\frac{1}{2}] \\ 2x_n - 1, & x_n \in
#         (\frac{1}{2},1] \end{array} \right. \quad \text{with} \quad x_0 = \frac{1}{10}
# $$
# 
# In particular, now that you know about how numbers are stored in a computer, how long do you expect it to take until the error creeps into the computation?

# ### Additional Resources
# 
# * [Number Representation in Computers](https://fabienmaussion.info/scientific_programming/week_04/02-Numbers.html)
# * [Floating Point Arithmetic](https://en.wikipedia.org/wiki/Floating-point_arithmetic)

# ## Approximating Functions
# 
# Numerical analysis is all about doing mathematics on a computer in accurate and predictable ways. Since a computer can only ever store finite bits of information for any number, most of what we do in a computer is naturally an approximation of the real mathematics. In this section we will look at a very powerful way to approximate mathematical functions.
# 
# How does a computer understand a function like $f(x) = e^x$? What happens under the hood, so to speak, when you ask a computer to do a computation with one of these functions? A computer is very good at arithmetic, but working with transcendental functions like these, or really any other sufficiently complicated functions for that matter, causes all sorts of problems in a computer. Approximation of the function is something that is always happening under the hood.

# ---
# **Exercise 1.14** In this problem we’re going to make a bit of a wish list for all of the things that a computer will do when approximating a function. We’re going to complete the following sentence:
# *If we are going to approximate $f(x)$ near the point $x=x_0$ with a simpler function $g(x)$ then ...*
# 
# (I’ll get us started with the first item that seems natural to wish for. The rest of the wish list is for you to complete.)
# 
# * the functions $f(x)$ and $g(x)$ should agree at $x=x_0$. In other words, $f(x_0) = g(x_0)$
# * if $f(x)$ is increasing/decreasing to the right of $x=x_0$, then $g(x)$ ...
# * if $f(x)$ is increasing/decreasing to the left of $x=x_0$, then $g(x)$ ...
# * if $f(x)$ is concave up/down to the right of $x=x_0$, then $g(x)$ ...
# * if $f(x)$ is concave up/down to the left of $x=x_0$, then $g(x)$ ...
# * ... is there anything else you would add?

# ---
# 
# In the previous exercises, you have built up some basic intuition for what we would want out of a mathematical operation that might build an approximation of a complicated function. What we’ve built is actually a way to get better and better approximations for functions out to pretty much any arbitrary accuracy that we like so long as we are near some anchor point (which we called $x_0$)
# 
# One of the points of this whole discussion is to give you a little glimpse as to what is happening behind the scenes in scientific programming languages when you do computations with these functions. A bigger point is to start getting a feel for how we might go in reverse and approximate an unknown function out of much simpler parts. This last goal is one of the big takeaways from numerical analysis: we can mathematically model highly complicated functions out of fairly simple pieces.
# 
# ---

# ```{note}
# **Definition.** Taylor Series) If $f(x)$ is an infinitely differentiable function at the point $x_0$, then the infinite polynomial expansion is called the Taylor Series of the function $f(x)$ 
# 
# $$
# f(x) = \sum\limits^{\infty}_{k=0} \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k
# $$
# 
# Taylor Series are named for the mathematician Brook Taylor.
# ```

# ## Approximation Error (con Taylor Series)

# The great thing about Taylor Series is that they allow for the representation of potentially very complicated functions as polynomials – and polynomials are easily dealt with on a computer since they involve only addition, subtraction, multiplication, division, and integer powers. The down side is that the order of the polynomial is infinite. Hence, every time we use a Taylor series on a computer we are actually going to be using a **Truncated Taylor Series** where we only take a finite number of terms. The idea here is simple in principle

# * If a function $f(x)$ has a Taylor Series representation it can be written as an infinite sum.
# * Computers can’t do infinite sums.
# * So stop the sum at some point $n$ and throw away the rest of the infinite sum.
# * Now $f(x)$ is approximated by some finite sum so long as you stay pretty close to $x=x_0$
# * and everything that we just removed of the end is called the remainder for the finite sum.

# ---
# 
# **Theorem 1.1** The approximation error when using a truncated Taylor Series is roughly proportional to the size of the next term in the Taylor Series.
# 
# ---
