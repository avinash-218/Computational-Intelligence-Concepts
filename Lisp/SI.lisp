(print "Enter P,R,T")
(terpri)
(setq p(read))
(setq r(read))
(setq ti(read))

(defun SI(p r ti)
    (/ (* p r ti) 100)
    )

(setq simple_interest (SI p r ti))
(write simple_interest)