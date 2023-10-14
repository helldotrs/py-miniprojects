SLIDERS = [
    [True, False, True, True],
    [True, True, False, False],
    [False, True, False, False]
]

slider_pos = ["right", "right", "right"]  # val --> left/right

def calculate_col_totals(side):
    col_totals = [0] * len(SLIDERS[0])  # Initialize col_totals list with zeros

    # Iterate through sliders and update col_totals based on their positions
    for i in range(len(SLIDERS)):
        for j in range(len(SLIDERS[i])):
            if slider_pos[i] == side and SLIDERS[i][j]:
                col_totals[j] += 1

    return col_totals

# Check slide side (for now assume all are on the right side)
side = "right"
col_totals = calculate_col_totals(side)
print(f"Column totals for sliders on the {side} side: {col_totals}")
