from itertools import permutations


def check(users, banned_id):
    result = set()
    for i in range(len(users)):
        if len(users[i]) == len(banned_id[i]):
            for j in range(len(users[i])):
                if banned_id[i][j] != '*':
                    if banned_id[i][j] == users[i][j]:
                        pass
                    else:
                        return False
            result.add(users[i])
        else:
            return False
    if len(result) == len(banned_id):
        return result
    else:
        return False


def solution(user_id, banned_id):
    answer_set = []
    users_list = list(permutations(user_id, len(banned_id)))
    for users in users_list:
        check_result = check(users, banned_id)
        if check_result and check(users, banned_id) not in answer_set:
            answer_set.append(check_result)
    return len(answer_set)