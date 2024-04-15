! pip install deap
!pip install scoop

import random
import deap
from deap import base, creator, tools, algorithms
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler


iris = load_iris()
X = iris.data
y = iris.target

scaler = StandardScaler()
X_normalized = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

def evaluate(individual):
    neurons = individual[0]
    layers = individual[1]

    model = MLPClassifier(hidden_layer_sizes=(neurons,) * layers, random_state=42, max_iter=10000)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f'n_Neurons: {neurons}. n_Layers:{layers}. ___ACC___: {accuracy}\n')

    return accuracy,

POPULATION_SIZE = 10
GENERATIONS = 5

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_neurons", random.randint, 1, 100)
toolbox.register("attr_layers", random.randint, 1, 5)
toolbox.register("individual", tools.initCycle, creator.Individual, (toolbox.attr_neurons, toolbox.attr_layers), n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=1, up=100, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=POPULATION_SIZE)

for gen in range(GENERATIONS):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    fitnesses = toolbox.map(toolbox.evaluate, offspring)
    for ind, fit in zip(offspring, fitnesses):
        ind.fitness.values = fit

    population = toolbox.select(offspring, k=len(population))

best_individual = tools.selBest(population, k=1)[0]
best_params = best_individual

print("Best Parameters:", best_params)