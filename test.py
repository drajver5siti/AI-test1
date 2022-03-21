state = (3,7,[0,0,0,0,1,3,4])

for i in range(state[1] - state[0] + 1, state[1]):
    if state[2][i] > state[2][i - 1]:
        print("False")
        break

print("True")