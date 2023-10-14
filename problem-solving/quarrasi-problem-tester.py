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

cols_right   = calculate_col_totals(right)
print(f"cols_right: {cols_right}") # test

cols_left    = calculate_col_totals(left)
print(f"cols_left: {cols_left}") # test
