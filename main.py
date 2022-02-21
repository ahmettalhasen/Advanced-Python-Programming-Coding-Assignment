input_file = open("input.txt", "r")
passwords = input_file.read()
password_list = passwords.split("\n")[:-1]
input_file.close()


# -----   PART 1   -----

def check_password_policy(*, password_policy: str) -> bool:
    policy, password = password_policy.split(":")
    policy_counts, policy_char = policy.split(" ")
    policy_min, policy_max = [int(item) for item in policy_counts.split("-")]

    char_count = password.count(policy_char)
    if policy_min <= char_count and policy_max >= char_count:
        return True
    return False


print(sum(
    check_password_policy(password_policy=password_policy)
    for password_policy in password_list
))  # 625


# -----   PART 2   -----

def check_password_policy_2(*, password_policy: str) -> bool:
    policy, password = password_policy.split(":")
    policy_counts, policy_char = policy.split(" ")
    location_1, location_2 = [int(item) for item in policy_counts.split("-")]

    # XOR Gate
    if (password[location_1] == policy_char) ^ (password[location_2] == policy_char):
        return True
    return False


print(sum(
    check_password_policy_2(password_policy=password_policy)
    for password_policy in password_list
))  # 391

