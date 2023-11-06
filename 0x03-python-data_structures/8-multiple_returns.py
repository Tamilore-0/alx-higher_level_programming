#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tulpe_a = (0, None)
    else:
        tulpe_a = (len(sentence), sentence[0])
    return tulpe_a
