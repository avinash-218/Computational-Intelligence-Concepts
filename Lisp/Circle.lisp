(print "Enter the radius ");prompt user
(setq r(read));get input
(terpri);nextline
(defconstant PI 3.1416);define constant

(defun Area(r);function definition
(setq A(* PI r r));PI*r*r
(print "Area of Circle =")
(write A))

(defun Circumference(r);function definition
(setq C(* 2 PI r))
(print "Circumference of Circle =")
(write C))

(Area r) ;call function
(Circumference r) ;call function