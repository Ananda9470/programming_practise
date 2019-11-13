# O(n) | O(n)
def minRewards(scores):

    if len(scores) == 0:
        return 0
    if len(scores) == 1:
        return 1

    idx = 0
    rewards = []

    while True:

        n_rel_smaller_right_elements = 0
        while scores[idx] > scores[idx+1]:
            n_rel_smaller_right_elements += 1
            idx += 1
            if idx == len(scores)-1:
                break

        if len(rewards) == 0:
            left_rwd = 0
        else:
            left_rwd = rewards[-1]

        reward = max(n_rel_smaller_right_elements+1, left_rwd+1)
        rewards.append(reward)

        reward = n_rel_smaller_right_elements

        for _ in range(n_rel_smaller_right_elements):
            rewards.append(reward)
            reward -= 1

        idx += 1

        if idx >= len(scores)-1:

            if scores[-1] > scores[-2]:
                rewards.append(rewards[-1]+1)

            break

    return sum(rewards)

if __name__ == "__main__":
    scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
    # scores = []
    # scores = [1, 5, 7]
    scores = [1]
    ans = minRewards(scores)
    print(ans)
