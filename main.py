import vegdata
import random 
import pygad
import numpy
areaMax = 400
waterMax = 105200
cropMax = 0
growingDays = 222
f1 = []
f2 = []

def main():
    global f1
    global f2
    global cropMax

    myVeg = vegdata.VegData()

   
    f1 = myVeg.getFunct1()
    cropMax = max(f1)*areaMax
    print(cropMax) 
    # print(f1)
    f2 = myVeg.getFunct2()
    # print(f2)
    # myVeg.printDict()
    num_generations = 10000
    num_parents_mating = 20
    sol_per_pop = 40
    num_genes = len(myVeg.vegList)
    gene_low = 0
    gene_high = areaMax

    ga_instance = pygad.GA(num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        gene_type=int,
                        gene_space={'low': gene_low, 'high': gene_high},
                        fitness_func=fitness_func,
                        parent_selection_type='nsga2')

    ga_instance.run()

    ga_instance.plot_fitness(label=['Obj 1', 'Obj 2', 'Obj 3'])

    solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
    print(f"Parameters of the best solution : {solution}")
    print(f"Fitness value of the best solution = {solution_fitness}")

    prediction = numpy.sum(solution)
    print(f"Total Area of Solution Crop = {prediction} (Square Meters)")

    prediction = numpy.sum((growingDays*solution*f2))
    print(f"Total Water of Solution Crop = {prediction} (liters)")

    for num in range(0,num_genes):
        print(f"{myVeg.vegList[num]}: {solution[num]}(sq.m)")

def fitness_func(ga_instance, solution, solution_idx):
    cropScoreSum = numpy.sum(solution*f1)
    areaSum= numpy.sum(solution) # area total of solution
    waterSum = numpy.sum(growingDays*solution*f2) # water use in litres
    
    fitness1 = 1.0 / (numpy.abs(cropScoreSum - cropMax) + 0.000001) # total crop score
    fitness2 = 1.0 / (numpy.abs(areaSum - areaMax) + 0.000001)
    fitness3 = 1.0 / (numpy.abs(waterSum - waterMax) + 0.000001)
    if fitness2 > areaMax:
        fitness2 = 0
    if fitness3 > waterMax:
        fitness3 = 0    
    return [fitness1, fitness2, fitness3]

if __name__ == "__main__":
    main()    

