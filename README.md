# python-behave vs pytest-bdd feature benchmark

This repository aims at sharing our discoveries while working on improving our existing test base, in the direction of using the BDD approach (Behavior Driver Development).

We compare 2 frameworks of the python eco-system that allows BDD:
 - python-behave
 - pytest-bdd

Disclaimer: the sole purpose of this repository is to keep track of our analysis steps. Some points are probably not solved yet, and our analysis may be partial. We only intend to share our discoveries.

## What is important in a test framework ?

We will evaluate both frameworks on the following points:

- ability to add new tests quickly
- logging capabilities
- test selection capabilities
- code scalability and coherence

To lead such an evaluation, we implemented the same basic (fake) scenarios:



