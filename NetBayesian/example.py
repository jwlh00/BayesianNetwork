from BayesianNetwork import BayesianNetwork
from BayesianNetwork import Node


# Create nodes
burglary = Node("Burglary")
earthquake = Node("Earthquake")
alarm = Node("Alarm", parents=["Burglary", "Earthquake"])
john_calls = Node("JohnCalls", parents=["Alarm"])
mary_calls = Node("MaryCalls", parents=["Alarm"])

# Create network
bn = BayesianNetwork()
bn.add_node(burglary)
bn.add_node(earthquake)
bn.add_node(alarm)
bn.add_node(john_calls)
bn.add_node(mary_calls)

# Set probabilities
burglary.set_probability({(True,): 0.001, (False,): 0.999})
earthquake.set_probability({(True,): 0.002, (False,): 0.998})
alarm.set_probability({(True, True, True): 0.95, (True, True, False): 0.94, (True, False, True): 0.29, (True, False, False): 0.001, (False, True, True): 0.99, (False, True, False): 0.9, (False, False, True): 0.001, (False, False, False): 0.01})
john_calls.set_probability({(True, True): 0.9, (True, False): 0.05, (False, True): 0.1, (False, False): 0.95})
mary_calls.set_probability({(True, True): 0.7, (True, False): 0.01, (False, True): 0.3, (False, False): 0.99})
alarm.set_probability({(True, True, True): 0.95,(True, True, False): 0.94,(True, False, True): 0.29,(True, False, False): 0.001,(False, True, True): 0.99,(False, True, False): 0.9,(False, False, True): 0.001,(False, False, False): 0.01})
burglary.set_probability({(True,): 0.001, (False,): 0.999, (True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0})


# Get probability of John calling given an alarm
probability = bn.get_probability(john_calls, {"Alarm": True})
print("Is it completely defined: ", bn.IsDefined())
print("=================================================")
print("Compact Network:\n", bn.compact())
print("=================================================")
print("Bayesian Network factors", probability)
print("=================================================")
result = bn.get_probability(john_calls, {"Alarm": True})
print("Algorithm Result: ", result.get(True))
