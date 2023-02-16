class Node:
    def __init__(self, name, parents=None):
        self.name = name
        self.parents = parents or []
        self.probabilities = {}

    def set_probability(self, probabilities):
        self.probabilities = probabilities

    def get_probability(self, value, parent_values):
        key = tuple([value] + parent_values)
        return self.probabilities.get(key)

class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def set_probability(self, node_name, probabilities):
        self.nodes[node_name].set_probability(probabilities)

    def get_probability(self, query, evidence):
        probabilities = {}
        for value in [True, False]:
            new_evidence = dict(evidence)
            new_evidence[query.name] = value
            probabilities[value] = self.enumerate_all(self.nodes.keys(), new_evidence)
        return self.normalize(probabilities)

    def enumerate_all(self, variables, evidence):
        if not variables:
            return 1
        first, *rest = list(variables)
        node = self.nodes[first]
        if first in evidence:
            value = evidence[first]
            parent_values = [evidence[parent] for parent in node.parents]
            return node.get_probability(value, parent_values) * self.enumerate_all(rest, evidence)
        else:
            probabilities = []
            for value in [True, False]:
                new_evidence = dict(evidence)
                new_evidence[first] = value
                parent_values = [new_evidence[parent] for parent in node.parents]
                probabilities.append(node.get_probability(value, parent_values) * self.enumerate_all(rest, new_evidence))
            return sum(probabilities)

    def normalize(self, probabilities):
        total = sum(probabilities.values())
        for key in probabilities:
            probabilities[key] /= total
        return probabilities

    
    def compact(self):
        """
        Returns a string representing the compact version of the Bayesian network.
        """
        node_strings = []
        for node_name, node in self.nodes.items():
            if not node.parents:
                node_string = f"{node_name} ({node.probabilities[(True,)]})"
            else:
                parent_strings = [f"{parent_name}={str(parent_value)}" for parent_name, parent_value in zip(node.parents, [True]*len(node.parents))]
                if (True, True) in node.probabilities:
                    true_prob = node.probabilities[(True, True)]
                else:
                    true_prob = 0.0

                if (True, False) in node.probabilities:
                    false_prob = node.probabilities[(True, False)]
                else:
                    false_prob = 0.0

                node_string = f"{node_name} ({parent_strings[0]}: {true_prob}, not {parent_strings[0]}: {false_prob})"
                for parent_name, parent_value in zip(node.parents[1:], [True]*len(node.parents[1:])):
                    node_string = f"{node_string}, {parent_name}={str(parent_value)}: {node.probabilities[(True, True, parent_value)]}, not {parent_name}={str(parent_value)}: {node.probabilities[(True, False, parent_value)]}"
            node_strings.append(node_string)
        return "\n".join(node_strings)
    
    def IsDefined(self):
            """
            Checks if a Bayesian network is complete.
            """
            for node_name, node in self.nodes.items():
                num_parents = len(node.parents)
                parent_combinations = [[True, False] for _ in range(num_parents)]
                for parents in product_cartesian(*parent_combinations):
                    key = tuple([True] + list(parents))
                    if key not in node.probabilities:
                        return False
            return True

def product_cartesian(*args):
    """
    Returns the Cartesian product of the given sequences.
    """
    if not args:
        yield []
    else:
        for item in args[0]:
            for result in product_cartesian(*args[1:]):
                yield [item] + result