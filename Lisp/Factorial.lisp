(print "Enter the value of n ");prompt user
(setq n(read));get input

(defun factorial (n);function definition
  (if (= n 0);if n==0
		1;return 1
	(* n (factorial (- n 1))) ) );return n*(fact(n-1))

(loop for i from 0 to n;loop from 0 to 16
   do (format t "~d! = ~d" i (factorial i)) 
   (terpri);new line
   )
   ;~d - one variable  ~% - newline