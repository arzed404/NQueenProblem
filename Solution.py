import random as r
from tqdm import tqdm

#----------------------------------------
def initialize(populationSize,chromosomSize,maxFitness ):
  population = []
  for i in range(populationSize):
    chromosom = []
    for j in range(chromosomSize):
      chromosom.append(r.randint(0,chromosomSize-1))
    population.append([chromosom, maxFitness])
  return population
#----------------------------------------
def scoreChrom(chromosom):
  for i in range(len(chromosom[0])-1):
    q = i
    inc = 1
    for j in range(q+1,len(chromosom[0])):
        if chromosom[0][q] == chromosom[0][j]+inc or chromosom[0][q] == chromosom[0][j]-inc:
            chromosom[1] = chromosom[1] - 1
           
        inc = inc+1
  for i in range(len(chromosom[0])-1):
    for j in range(i+1,len(chromosom[0])):
      if chromosom[0][i] == chromosom[0][j]:
            chromosom[1] = chromosom[1] - 1
  return chromosom
#----------------------------------------
def evaluate(population):
  newPopulation = []
  for chromosom in population:
    newPopulation.append(scoreChrom(chromosom))
  newPopulation = sorted(newPopulation,key=lambda l:l[1], reverse=True)
  return newPopulation
#----------------------------------------
def crossOver(population):
    chromosom1 = population[1][0][:len(population[1][0])//2] + population[0][0][len(population[0][0])//2:]
    chromosom2 = population[0][0][:len(population[0][0])//2] + population[1][0][len(population[1][0])//2:]
    population.pop()
    population.pop()
    population.append([chromosom1, 28])
    population.append([chromosom2, 28])
    for chromosom in population:
        chromosom[1] = 28
    return population
#----------------------------------------
def mutate(population, chromosomSize):
    population[0][0][r.randint(0,chromosomSize-1)] = r.randint(0,chromosomSize-1)
    population[1][0][r.randint(0,chromosomSize-1)] = r.randint(0,chromosomSize-1)
    return population
#----------------------------------------
def main():
    chromosomSize = 8
    populationSize = 20
    maxFitness = 28
    population  = initialize(populationSize, chromosomSize, maxFitness)
    for i in tqdm(range(9999)):
        population = crossOver(population)
        population = evaluate(population)
        
        if population[0][1] == 28:
            break;
        if i % 5 == 0 : 
            population = mutate(population, chromosomSize)
    print(f"\nBest of all: {population[0]}")
#----------------------------------------
main()
