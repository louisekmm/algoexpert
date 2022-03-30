def isValidSubsequence(array, sequence):
	is_sequence = True
	qty_equal = 0
    # Write your code here.
	print(array)
	print(sequence)
	s_aux = sequence
	if len(sequence) > len(array):
		return False

	for s in sequence:
		for i in array:
			if s == i:
				qty_equal += 1
				s_aux.remove()

	if qty_equal == len(sequence):
		return True

	return False
