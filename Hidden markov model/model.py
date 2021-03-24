from pomegranate import *

#Observation model for each state
sun = DiscreteDistribution({
    "umbrella" : 0.2,
    "no umbrella" : 0.8
})

rain = DiscreteDistribution({
    "umbrella" : 0.9,
    "no umbrella" : 0.1
})

states = [sun, rain]

#Transition model
transition = numpy.array(
    [[0.8,0.2],#future prediction if today is sunny
     [0.3, 0.7]] #future prediction if today is rainy
)

#starting probability
starts = numpy.array([0.5, 0.5])

#create the model
model = HiddenMarkovModel.from_matrix(
    transition, states, starts, 
    state_names= ["sun", "rain"]
)
model.bake()
