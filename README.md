# N-Queen Problem
Solving N-Queen problem using genetic algorithm
Chromosom:
      From index 0 to n, each index is the column number and value at each index is the row number at which queen is placed.
Fitness is cumilative fitness of each queen
Each queen has max fitness of how many queens it does not attack, starting from right
  Max fitness of rightmost queen can be 7, next one 6 then 5 and so on..

Crossover is mid point crossover of top two chromosom
Mutation happens every 5 iteration
number of iteration 9999
