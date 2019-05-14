Two data consistency problems solved with Python.

Problem 1:

A group of ethnographers analyze some oral history data they've collected by interviewing members of a village to learn about the lives of the people who've lived there over the past few hundred years. Every bit of data provided by the villagers comes in one of two forms:

-For some i and j, person Pi died before person Pj was born
-For some i and j, the life spans of Pi and Pj overlapped

Figure out if the data provided by the villagers is consistent.

Problem 2:
Given a set of unsigned paintings created by two different artists whom we will call X and Y, researchers are trying to figure out which artist painted each one. They don't have any data on which artist painted each painting, but they do have data of the following form:

-For some i and j, the same artist created paintings Pi and Pj
-For some i and j, different artists created paintings Pi and Pj

We can't reason about which artist painted each painting from this data, but we can figure out if it is consistent.

A writeup of solution proofs is provided in FinalProject.pdf

This requires Python 3 and networkx(https://networkx.github.io/documentation/stable/index.html) which can be installed using pip:

>pip install networkx

or

>pip install networkx[all]

to include dependencies

Run with

>python GraphTheoryProject1.py

or

>python GraphTheoryProject2.py
