from pomegranate import *

#define stating probability
start = DiscreteDistribution({
    "sun" : 0.5,
    "rain" : 0.5
})

#define transition model
transition = ConditionalProbabilityTable([
    ["sun", "sun" , 0.8],
    ["sun", "rain" , 0.2],
    ["rain", "sun" , 0.3],
    ["rain", "rain" , 0.7]
], [start])

#create Markov chain
model = MarkovChain([start, transition])

#sample states from chain
print(model.sample(100))