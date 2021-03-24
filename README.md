# Markov-and-Hidden-Markov-Models
# Markov Model
 
 Here we gonna predict future's weather using Markov model. Using the Markov assumption, we restrict our previous states (e.g. how many previous days we are going to consider when predicting tomorrow’s weather), thereby making the task manageable. This means that we might get a more rough approximation of the probabilities of interest, but this is often good enough for our needs. Moreover, we can use a Markov model based on the information of the one last event (e.g. predicting tomorrow’s weather based on today’s weather).
 A MARKOV CHAIN is a sequence of random variables where the distribution of each variable follows the Markov assumption. That is, each event in the chain occurs based on the probability of the event before it. To start constructing a Markov chain, we need a transition model that will specify the probability distributions of the next event based on the possible values of the current event.

# Hidden Markov Model
 
  A hidden Markov model is a type of a Markov model for a system with hidden states that generate some observed event. This means that sometimes, the AI has some measurement of the world but no access to the precise state of the world. In these cases, the state of the world is called the hidden state and whatever data the AI has access to are the observations.
  Here our AI wants to infer the weather (the hidden state) and umbrellas(observations) to predict the weather.
