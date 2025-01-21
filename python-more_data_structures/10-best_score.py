#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    best_score = max(a_dictionary.values(), default=None)
    for key, value in a_dictionary.items():
        if value == best_score:
            return key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))