def test_palindrome(input_str):
	for item in range(0, len(input_str)):
		if not input_str[item] == input_str[len(input_str)-1-item]:
			print(f"Diff at items { input_str[item]} and {input_str[len(input_str)-1-item]}")
			return False
	return True

test_palindrome("kazk")
# False

test_palindrome("kazak")
# True