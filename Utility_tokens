# Revised and Combined Code for Utility Tokens and Voting Mechanism in Unity Network

# Existing classes and functions for context
class EthicalMetrics:
    def __init__(self, environmental_responsibility, social_equality, economic_fairness, transparency):
        self.environmental_responsibility = environmental_responsibility
        self.social_equality = social_equality
        self.economic_fairness = economic_fairness
        self.transparency = transparency

class UtilityToken:
    def __init__(self, name, validation_function):
        self.name = name
        self.validation_function = validation_function

class Guardian:
    def __init__(self, id):
        self.id = id

    def vote(self, new_token_name, new_token_validation):
        # Placeholder for voting logic
        return True

class UnityNetwork:
    def __init__(self):
        self.guardians = []
        self.utility_tokens = {}

    def add_guardian(self, guardian):
        self.guardians.append(guardian)

    def add_utility_token(self, new_token_name, new_token_validation):
        # Simulated majority vote by guardians
        votes = [guardian.vote(new_token_name, new_token_validation) for guardian in self.guardians]
        if sum(votes) / len(self.guardians) >= 0.75:  # 75% majority needed
            self.utility_tokens[new_token_name] = UtilityToken(new_token_name, new_token_validation)
            print(f"Utility token {new_token_name} added to the Unity Network.")
        else:
            print(f"Failed to add utility token {new_token_name}. Not enough votes from guardians.")

# Example usage
unity_network = UnityNetwork()
guardian1 = Guardian(1)
guardian2 = Guardian(2)
guardian3 = Guardian(3)

unity_network.add_guardian(guardian1)
unity_network.add_guardian(guardian2)
unity_network.add_guardian(guardian3)

# Define new utility token and its validation logic
def new_token_validation(transaction):
    return transaction.get('new_feature', False)

# Try adding the new utility token
unity_network.add_utility_token("NEW_TOKEN", new_token_validation)