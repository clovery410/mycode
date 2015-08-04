def default_strategy(score, opponent_score):
    return 5

def make_default_strategy():
    def default_strategy(score, opponent_score):
        return 5
    return default_strategy


def make_weird_strategy(num_rolls):
    def weird_strategy(score, opponent_score):
        return max(num_rolls, (score + opponent_score) // 20)
    return weird_strategy
