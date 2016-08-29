SimplePyGA
==========

This project demonstrates a simple Genetic Algorithm (GA) in Python.

System Requirements
===================

This project was built with Python 3.5.2 64-bit and Anaconda 4.1.1 on
Windows 10. It does not yet use any Anaconda-specific features and
should work with Python 3.5.x on any platform but this has not been
tested. It will not work with Python 2.

A Visual Studio 2015 solution and project file are included for those
who like to edit using Visual Studio.

Design
======

Background
----------

GAs simulate the evolution of organisms by natural selection,
incorporating the concepts of fitness, cross-breeding and mutation.
There is a population of individuals that evolve over many generations
until some kind of termination criteria are met. Typically this means
that one or more individuals in the population evolves to be some
desired level of fitness.

For a given GA application:

-  Individuals represent something you want to improve, such as a design
   or algorithm
-  Individuals have a set of characteristics, usually referred to as their
chromosomes or genes and usually represented by numeric parameters or lists of values
-  Individuals may mutate, in which case one or more genes may randomly
   change on its own
-  Individuals may cross-breed, in which case one or more new
   individuals result from combining the genes of one or more parents
   (usually two)
-  A population is simply a collection of those individuals which can
   evolve together by natural selection
-  There is some kind of goal or ideal end state which defines the best
   possible individual
-  There is a fitness function that measures how close a given
   individual is to the goal
-  Within a given generation, the fittest Individuals have a better
   chance of cross-breeding and producing offspring for the next
   generation, so that over time the average fitness of the population
   increases and eventually (you hope) you get an individual that
   matches or gets close to the goal, terminating the GA experiment

Implementation
--------------

In SimplePyGA, there are Python classes for:

-  Gene (a named attribute with a numeric value and allowed range)
-  Individual (a single “creature” with one or more Genes)
-  Population (a collection of Individuals)
-  Environment (the world that a Population evolves in; settings for
   each GA run)
-  FitnessCalc (a set of methods for determining an Individual’s fitness
   with respect to a Goal)

Then there is a main script, SimplyPyGA.py, that runs the whole GA.

Credits
=======

The original version of this code, back when it was all in one script
file, was based on the article `Creating a genetic algorithm for
beginners`_ by Lee Jaconson at The Project Spot.

Improvements to the selection algorithm for cross-breeding came from the
article `Genetic Algorithm for Solving Simple Mathematical Equality
Problem`_ by Denny Hermawanto.

.. _Creating a genetic algorithm for beginners: http://www.theprojectspot.com/tutorial-post/creating-a-genetic-algorithm-for-beginners/3
.. _Genetic Algorithm for Solving Simple Mathematical Equality Problem: https://arxiv.org/ftp/arxiv/papers/1308/1308.4675.pdf