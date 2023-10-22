# Next part of the Unity Network code: The CivicPoints and Voting Mechanism

class CivicPoints:
    def __init__(self):
        self.points = 0

    def add_points(self, points_to_add):
        self.points += points_to_add

    def subtract_points(self, points_to_subtract):
        self.points -= points_to_subtract

class UnityTokenHolder:
    def __init__(self, id):
        self.id = id
        self.civic_points = CivicPoints()

    def vote_for_guardian(self, guardian_id):
        # Placeholder for voting logic
        return True

class VotingMechanism:
    def __init__(self):
        self.pending_guardians = []
        self.approved_guardians = []

    def add_pending_guardian(self, guardian):
        self.pending_guardians.append(guardian)

    def approve_guardian(self, unity_token_holders):
        for guardian in self.pending_guardians:
            votes = [holder.vote_for_guardian(guardian.id) for holder in unity_token_holders]
            if sum(votes) / len(unity_token_holders) >= 0.75:  # 75% majority needed
                self.approved_guardians.append(guardian)
                print(f"Guardian {guardian.id} approved by Unity Token holders.")
            else:
                print(f"Guardian {guardian.id} not approved. Not enough votes from Unity Token holders.")