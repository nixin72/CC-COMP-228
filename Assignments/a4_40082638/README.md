# COMP-228 Assignment 4

### Name: Philip Dumaresq
### Student ID: 40082638
### Email: phdumaresq@gmail.com

The purpose of this assignment is to learn the basics of computer architecture using the MARIE assembly language.

#### Difficulties
I don't believe that I really had difficulties with much in this assignment. It was my only programming assignment this semester, so I'm glad that I got to work on it.

#### Comments
Ignore the word document, the PDF was exported from it.

Ignore the extra folder. It just contains extra work I did for fun on the assignment. If you're curious:

- I wrote an integer division and modulus function so that I could convert numbers to unicode to print them out so that all output could be done in unicode instead of DEC or HEX.
- I used modulus to get the last value of the number, add 30 to it for it's unicode value, push it onto a stack, then divided by 10 to cut off the right most digit. Repeat until no digits. Then pop off the stack one at a time, output it, and then it'll print as unicode.
- I used this method to add a "%d" modifier to the printf function so that I could emulate C's as closely as possible. It won't accept an arbitrary number of inputs like C, but it accepts a mode and a string to print at least.

That code isn't part of my actual submission. Mode code = more bugs, and I don't want to get docked for some of the extra stuff I have.
