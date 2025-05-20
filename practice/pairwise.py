# 2. Bradley-Terry Model (Statistical Ranking)
# A more robust way to rank with incomplete pairwise data is using the Bradley-Terry model, 
# which estimates the probability that item A beats item B based on their latent scores.

# Example:

import choix  # For Bradley-Terry model

# List of comparisons (winner, loser)
comparisons = [
    (0, 1),  # Item 0 beats Item 1
    (2, 0),
    (2, 1),
    (3, 2),
    # More comparisons...
]

n_items = 32
# Fit Bradley-Terry model
strengths = choix.ilsr_pairwise(n_items, comparisons)

# Rank by strength
ranked = sorted(range(n_items), key=lambda x: strengths[x], reverse=True)

print("\nBradley-Terry Ranking:")
for i, idx in enumerate(ranked, 1):
    print(f"{i}. Item {idx} (Score: {strengths[idx]:.2f})")


# choix.ilsr_pairwise() uses Iterative Luce Spectral Ranking, a reliable method for ranking from incomplete data.