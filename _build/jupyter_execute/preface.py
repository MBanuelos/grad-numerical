#!/usr/bin/env python
# coding: utf-8

# # Preface
# 
# This book grew out of lecture notes, classroom activities, code, examples, exercises,
# projects, and challenge problems for my introductory course on
# numerical methods.  The prerequisites for this material include a firm understanding of
# single variable calculus (though multivariable calculus doesn't hurt), a good
# understanding of the basics of linear algebra, a good understanding of the basics of
# differential equations, and some exposure to scientific computing (as seen in other math
# classes or perhaps from a computer science class). The primary audience is any
# undergraduate STEM major with an interest in using computing to solve problems.
# 
# A note on the book's title: I do not call these materials ``numerical
# analysis'' even though that is often what this course is called.  In these materials I
# emphasize ``methods'' and implementation over rigorous mathematical ``analysis.''  While
# this may just be semantics I feel that it is important to point out.  If you are looking
# for a book that contains all of the derivations and rigorous proofs of the primary results
# in elementary numerical analysis, then this not the book for you.  I have
# intentionally written this material with an inquiry-based emphasis which means that this
# is not a traditional text on numerical analysis -- there are plenty of those on the market
# and I cite several wonderful traditional texts in the bibliography at the end of this
# book.
# 
# ## To The Student
# 
# ### The Inquiry-Based Approach
# % % The inquiry-based approach can by summarized by one quote:
# % \begin{quote}
# %     {\it Any creative endeavor is built on the ash heap of failures.}
# % \end{quote}
# % The material in this book is meant to make you think, build, construct, fail, struggle,
# % and ultimately succeed in learning numerical methods.

# \begin{problem}[Setting The Stage]
#     Let's start the book off right away with a problem designed for groups, discussion,
#     disagreement, and deep critical thinking.  This problem is inspired by Dana Ernst's
#     first day IBL activity titled: \href{http://danaernst.com/setting-the-stage/}{Setting
#     the Stage}.
#     \begin{itemize}
#         \item Get in groups of size 3-4.
#         \item Group members should introduce themselves.
#         \item For each of the questions that follow I will ask you to:
#             \begin{enumerate}
#                 \item {\bf Think} about a possible answer on your own
#                 \item {\bf Discuss} your answers with the rest of the group
#                 \item {\bf Share} a summary of each group's discussion
#             \end{enumerate}
#     \end{itemize}
#     {\bf Questions:} 
#     \begin{description}
#         \item[Question \#1:] What are the goals of a university education?
#         \item[Question \#2:] How does a person learn something new?
#         \item[Question \#3:] What do you reasonably expect to remember from your courses
#             in 20 years?
#         \item[Question \#4:] What is the value of making mistakes in the learning process?
#         \item[Question \#5:] How do we create a safe environment where risk taking is
#             encouraged and productive failure is valued?
#     \end{description}
# \end{problem}
# 
# 
# This material is written with an Inquiry-Based Learning (IBL) flavor. In that sense, this
# document could be used as a stand-alone set of materials for the course but these notes
# are not a {\it traditional textbook} containing all of the expected theorems, proofs,
# code, examples, and exposition. You are encouraged to work through problems and homework,
# present your findings, and work together when appropriate. You will find that this
# document contains collections of problems with only minimal interweaving exposition.  It
# is expected that you do every one of the problems and then only use other more traditional
# texts (or Google) as a backup when you are completely stuck.  Let me say that again: this
# is not the only set of material for the course.  Your brain, your peers, and the books
# linked in the next section are your best resources when you are stuck.
# 
# To learn more about IBL go to
# \href{http://www.inquirybasedlearning.org/about/}{http://www.inquirybasedlearning.org/about/}.
# The long and short of it is that you, the student, are the one that is doing the
# work; proving theorems, writing code, working problems, leading discussions, and pushing
# the pace. The instructor acts as a guide who only steps in to redirect conversations or to
# provide necessary insight. 
# 
# You have the following jobs as a student in this class:
# \begin{enumerate}
#     \item {\bf Fight!}  You will have to fight hard to work through this material.  The fight is
#         exactly what we're after since it is ultimately what leads to innovative thinking.
#     \item {\bf Screw Up!}  More accurately, don't be afraid to screw up.  You should write code,
#     work problems, and prove theorems then be completely unafraid to scrap what you've
#     done and redo it from scratch.  Learning this material is most definitely a non-linear
#     path.
# \item {\bf Collaborate!}  You should collaborate with your peers with the following caveats:
#     \begin{enumerate}
#         \item When you are done collaborating you should go your separate ways.  When you
#             write your solution you should have no written (or digital) record of your
#             collaboration.  
#         \item \underline{The internet is not a collaborator}.  Use of the internet to help
#             solve these problems robs you of the most important part of this class; the
#             chance for original thought.
#     \end{enumerate}
# \item {\bf Enjoy!}  Part of the fun of IBL is that you get to experience what it is like to
#         think like a true mathematician / scientist.  It takes hard work but ultimately
#         this should be fun!
# \end{enumerate}
# 
# \subsection{Online Texts and Other Resources}\label{pref:resources}
# If you are looking for online textbooks for numerical methods or numerical analysis I can
# point you to a few of my favorites.  Some of the following online resources may be a good
# place to help you when you're stuck but they will definitely say things a bit differently.
# Use these resources wisely.
# \begin{itemize}
#     \item Holistic Numerical Methods
#         \href{http://nm.mathforcollege.com/}{http://nm.mathforcollege.com/}\\
#         The Holistic Numerical Methods book is probably the most complete free reference
#         that I've found on the web.  This should be your source to look up deeper
#         explanations of problems, algorithms, and code.
#     \item Scientific Computing with MATLAB
#         \href{http://gribblelab.org/scicomp/scicomp.pdf}{http://gribblelab.org/scicomp/scicomp.pdf}
#     \item Tea Time Numerical Analysis
#         \href{http://lqbrin.github.io/tea-time-numerical/}{http://lqbrin.github.io/tea-time-numerical/}
# \end{itemize}
# 
# 
# \section{To the Instructor}
# If you are an instructor wishing to use these materials then I only ask that you adhere to the
# Creative Commons license.  You are welcome to use, distribute, and remix these materials
# for your own purposes.  Thanks for considering my materials for your course!  Let me know
# if you have questions, edits, or suggestions: esullivan@carroll.edu.
# 
# \subsection{The Inquiry-Based Approach}
# I have written these materials with an inquiry-based flavor.  This means that this is not
# a traditional textbook.  I don't
# lecture through hardly any of the material in the book.  Instead my classes are structured
# so that students are given problems to work before class, we build off of those problems
# in class, and we repeat.  The exercises at the end of the chapters are assigned weekly and
# graded with a revision process in mind -- students redo problems if the coding was
# incorrect, if the mathematics was incorrect, or if they somehow missed the point.  The
# students are tasked with building most of the algorithms, code, intuition, and analysis
# with my intervention only if I deem it necessary. 
# 
# Several of the problems throughout the book are meant to be done in groups either at
# the boards in the classroom or in some way where they can share their work.  Much of my
# class time is spent with students actively building algorithms or group coding.  The
# beauty, as I see it, of IBL is that you can run your course in any way that is comfortable
# for you.  You can lecture through some of the material in a more traditional way, you can
# let the students completely discover some of the methods, or you can do a mix of both.
# 
# You will find that I do not give rigorous (in the mathematical sense) proofs or
# derivations of many of the algorithms in this book.  I tend to lean on
# numerical experiments to allow students to discover algorithms, error estimates, and other
# results without the rigor.
# The makeup of my classes tends to be math majors along with engineering, computer science,
# physics, and data science students.  While the math majors need to eventually see the
# rigorous derivations the other majors, I think, are better served working from an
# experimental approach rather than a theorem-proof approach.
# 
# \subsection{The Projects}
# I have taught this class with anywhere from two to four projects during the semester.
# Each of the projects is designed to give the students an open-ended task where they can
# show off their coding skills and, more importantly, build their mathematical communication
# skills.  Projects can be done in groups or individually depending on the background and
# group dynamics of your class.  Appendix \ref{app:writing_projects} contains several tips
# for how to tackle the writing in the projects.  Appendix \ref{app:latex} gives students
# tips for writing in \LaTeX\ if indeed you want your students using that tool.  
# 
# \subsection{Coding}
# I expect that my students come with some coding experience from other mathematics or
# computer science classes.  With that, I leave the coding help as an appendix (see Appendix
# \ref{app:coding}) and only point the students there for refreshers.  If your students need
# a more thorough ramp up to the coding then you might want to start with Appendix
# \ref{app:coding} to get the students up to speed.  I expect the students to do most of the
# coding the in the class, but occasionally we will code algorithms together (especially
# earlier in the semester when the students are still getting their feet underneath them).
# 
# \ifnum\Python=0 If students are coding in MATLAB then be sure that all students have
# access.  We have a site license that students can log into via a virtual desktop.  A
# student license tends to serve students well. \fi
# \ifnum\Python=1 I encourage students to learn Python.  It is a general purpose language
# that does extremely well with numerical computing when paired with \texttt{numpy} and
# \texttt{matplotlib}.  Appendix \ref{app:coding} has several helpful sections for getting
# students up to speed with Python.
# 
# I encourage you to consider having your students code in Jupyter Notebooks.  The advantage
# is that students can mix their writing and their code in a seamless way.  This allows for
# an iterative approach to coding and writing and gives the students the tools to explain
# what they're doing as they code.
# \fi
# 
# \subsection{Pacing}
# The following is a typical 15-week semester with these materials.
# \begin{itemize}
#     \item Chapter 1 - 1.5 weeks
#     \item Chapter 2 - 1.5 weeks
#     \item Chapter 3 - 2 weeks
#     \item Chapter 4 - 3 weeks
#     \item Chapter 5 - 3 weeks
#     \item Chapter 6 - 3 weeks
# \end{itemize}
# 
# \subsubsection*{Other Considerations:}
# \begin{description}
#     \item[Projects:] I typically assign a project after Chapter 2 or 3, a second project
#         after Chapter 4, and a third project after Chapter 5.  The fourth project, if time
#         allows, typically comes from Chapter 6.  I typically dedicate two class days to
#         the first project and then one class day to each subsequent project. For the final
#         project I typically have students present their work so this takes a day or two
#         out of our class time. 
#     \item[Exercises:] I typically assign one collection of exercises per week.  Students
#         are to work on these outside of class, but in some
#         cases it is worth taking class time to let students work in teams.  Of particular
#         note are the coding exercises in Chapter \ref{ch:intro}.  If your students need
#         practice with coding then it might be worthwhile to mix these exercises in through
#         several assignments and perhaps during a few class periods.  I have also taken
#         extra class time with the exercises in Chapter \ref{ch:odes} to let the students
#         work in pairs on the modeling aspects of some of the problems.
#     \item[Exams:] This is a non-traditional book and as such you might want to consider
#         some non-traditional exam settings.  Some ideas that my colleagues and I have used
#         are: 
#         \begin{itemize}
#             \item Use code and functions that you've written to solve several new
#                 problems during a class period.
#             \item Give the mathematical details and the derivations of key algorithms.
#             \item Take several problems home (under strict rules about collaboration) and
#                 return with working code and a formal write up.
#             \item No exams, but put heavier weight on the projects.
#         \end{itemize}
# \end{description}
# 
# \section{Special Thanks}
# I would first like to thank Dr. Kelly Cline for being brave enough to teach a course that
# he loves out of a rough draft of my notes.  Your time, suggested edits, and thoughts for
# future directions of the book were, and are, greatly appreciated.  Second, I would like to
# thank Johnanna for simply being awesome.  Next I would like to thank the institution
# of Carroll College for seeing this project as a worthy academic pursuit even though the
# end result is not a book or publication in the traditional sense.  Finally, I would like
# to thank all of my colleagues and students, both past and present, in the math department
# at Carroll.  The suggestions, questions, struggles, and triumphs of these folks are what
# have shaped this work into something that I'm proud of and that I hope will be a useful
# resource for future students and instuctors.

# In[ ]:




