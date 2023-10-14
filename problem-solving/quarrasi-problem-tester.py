SLIDERS = [
    [True, False, True, True],
    [True, True, False, False],
    [False, True, False, False]
]

slider_pos = ["right", "right", "right"]  # val --> left/right

def calculate_col_totals(side):
    col_totals = [0] * len(SLIDERS[0])  # Initialize col_totals list with zeros

    # Iterate through sliders and update col_totals based on their positions # this comment seems like "# this is a comment"?
    for i in range(len(SLIDERS)):
        for j in range(len(SLIDERS[i])):
            if slider_pos[i] == side and SLIDERS[i][j]:
                col_totals[j] += 1

    return col_totals

def test_alarm(side): # could probably be split into two functions  
    return sum(1 for a in side if a == 2) == 1 # my solution
    
    return side.count(2) == 1 # result of asking ml to improve it, wont be executed    

def test_alarms(left,right): # is this name unique enough of could it be something like test_both_alarms()? or should I just stack??
    return test_alarm(left) or test_alarm(right) # FIXME: assuming non-exclusivity here. look up rules.

def main()
    pass

cols_right   = calculate_col_totals("right")
print(f"cols_right: {cols_right}") # test
alarm_right  = test_alarm(cols_right)
print(f"alarm_right: {alarm_right}")

cols_left    = calculate_col_totals("left")
print(f"cols_left: {cols_left}") # test
alarm_left  = test_alarm(cols_left)
print(f"alarm_left: {alarm_left}")

alarms = test_alarms(cols_left, cols_right)
print(f"alarms: {alarms}
