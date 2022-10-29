(print "Enter the value of n ");prompt user
(setq n(read));get input
(terpri);nextline

(setq a -1);init a = -1
(setq b 1);init b = 1

(defun fibo(n);function definition
    ( loop for x from 1 to n ;loop from 1 to n
           do( setq c (+ a b));c=a+b
           do( setq a b);a = b
           do( setq b c);b = c
           (print c))
)

(fibo n);function call