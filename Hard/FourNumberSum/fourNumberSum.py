def fourNumberSum(array, targetSum):
    pairs = {}
    output = []

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            currSum = array[i] + array[j]
            diff = targetSum - currSum

            if diff in pairs:
                for pair in pairs[diff]:
                    output.append(pair + [array[i], array[j]])

        for k in range(0, i):
            currSum = array[k] + array[i]

            if currSum in pairs:
                pairs[currSum].append([array[k], array[i]])
            else:
                pairs[currSum] = [[array[k], array[i]]]

    return output
