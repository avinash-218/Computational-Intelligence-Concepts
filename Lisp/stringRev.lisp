(print "Enter the string ");prompt user
(setq s1(string(read)));read input as string
(setq s2(reverse s1));s2 = reverse s1

(if (string-equal s1 s2);string equal s1 & s2
(format t "~%~d is palindrome"s1))

(if (string-not-equal s1 s2);if string not equal
(format t "~%~d is not palindrome"s1))