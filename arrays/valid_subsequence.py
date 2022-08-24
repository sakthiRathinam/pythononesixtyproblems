def solution_one(array,sequence):
    seq_idx = 0
    for arr in array:
        if seq_idx == len(sequence):
            return True
        if arr == sequence[seq_idx]:
            seq_idx += 1
    return len(sequence) == seq_idx

def solution_two(array,sequence):
    seq_idx = 0
    arr_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1
    return len(sequence) == seq_idx
