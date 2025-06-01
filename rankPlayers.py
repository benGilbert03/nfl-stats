import choix
import numpy as np
import streamlit as st

if 'comparisons' not in st.session_state:
    st.session_state['comparisons'] = []

def addComparison(winner, loser):
    st.session_state['comparisons'].append((winner, loser))

def rank():
    """
    Given a list of (winner, loser) comparisons, returns:
    - normalized strengths of each item
    - list of item indices ranked from best to worst
    """
    comparisons = st.session_state['comparisons']

    # Get unique item indices
    item_ids = set()
    for winner, loser in comparisons:
        item_ids.update([winner, loser])
    item_ids = sorted(item_ids)
    id_map = {item_id: idx for idx, item_id in enumerate(item_ids)}
    reverse_map = {idx: item_id for item_id, idx in id_map.items()}

    # Remap comparisons to 0-based indexing
    remapped_comparisons = [(id_map[w], id_map[l]) for w, l in comparisons]
    n_items = len(item_ids)

    # Fit Bradley-Terry model
    log_strengths = choix.ilsr_pairwise(n_items, remapped_comparisons)
    strengths = np.exp(log_strengths)
    normalized_strengths = strengths / np.sum(strengths)

    # Get ranking (highest strength first)
    ranked_indices = np.argsort(-normalized_strengths)
    ranked_items = [reverse_map[i] for i in ranked_indices]

    return normalized_strengths, ranked_items

# --------------------------- Example usage -------------------------------
# First number beats second number

# comparisons = [    
#     (0, 1), (0, 1), (0, 1),  
#     (1, 2), (1, 2),          
#     (0, 2),                  
#     (2, 0),                  
#     (3, 0), (3, 2), (1, 3)
# ]

# strengths, ranking = rank(comparisons)

# print("Normalized strengths:", strengths)
# print("Ranking (best to worst):", ranking)