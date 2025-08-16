# Welcome to My Levenshtein
***

## Task
The task here is to write an algorithm that calculates the Qwasar version of a Levenshtein number between two words.

The Qwasar version of a Levenshtein number is simple: it's a value that represents how similar two given strings are. 
It is found by comparing two strings and returning the difference between them.

## Description
The function takes two strings s1 and s2 as input. 
We compare the strings length. if the strings don’t have the same length, the function immediately returns -1.
This is because the comparison is character by character — impossible if lengths differ.

A counter is initialized to store how many positions have different character.

We use zip(), a built-in Python function that combines two (or more) iterables element by element.
It pairs up elements at the same index from each iterable.
It stops when the shortest iterable is exhausted.

here, zip(s1, s2) pairs up characters from both strings at the same index.
If the characters differ, increment the counter.

After looping through all positions, return the number of differences.

## What it actually does?
It counts the number of mismatched characters between two strings of equal length.

This is known as the Hamming distance, not the full Levenshtein distance.

## Flowchart
     Start --> compare len(s1) and len(s2)
     If they differ in length return -1.
     If their length are equal initialize a counter and loop over the characters s1 and s2 using zip()
     For each pair of characters c1,c2 of s1,s2 check whether they are equal.
     If not then increment the counter.
     Return the counter value once the iteration is over.


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img src=https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png  width='60px' /></span>
