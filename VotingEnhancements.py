# voting_mechanism.py

class VotingSystem:
    def __init__(self):
        self.guardian_candidates = {}  # Candidate ID to votes
        self.utility_proposals = {}  # Proposal ID to votes
        self.current_guardians = []  # List of current guardian IDs
        self.unity_token_holders = set()  # Set of Unity token holders
    
    def add_candidate(self, candidate_id):
        self.guardian_candidates[candidate_id] = 0

    def add_unity_token_holder(self, holder_id):
        self.unity_token_holders.add(holder_id)

    def vote_for_guardian(self, holder_id, candidate_id):
        if holder_id not in self.unity_token_holders:
            return "Invalid Unity token holder"
        if candidate_id not in self.guardian_candidates:
            return "Invalid candidate"
        self.guardian_candidates[candidate_id] += 1
        total_votes = len(self.unity_token_holders)
        if self.guardian_candidates[candidate_id] >= 0.75 * total_votes:
            self.current_guardians.append(candidate_id)
            del self.guardian_candidates[candidate_id]

    def propose_utility(self, proposal_id):
        self.utility_proposals[proposal_id] = 0

    def vote_for_utility(self, holder_id, proposal_id):
        if holder_id not in self.unity_token_holders:
            return "Invalid Unity token holder"
        if proposal_id not in self.utility_proposals:
            return "Invalid proposal"
        self.utility_proposals[proposal_id] += 1
        total_votes = len(self.unity_token_holders)
        if self.utility_proposals[proposal_id] >= 0.75 * total_votes:
            # Add code to integrate the new utility token
            del self.utility_proposals[proposal_id]