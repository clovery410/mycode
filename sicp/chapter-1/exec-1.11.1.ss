;This is recursive procedure
(define (f n)
  (cond ((= n 0) 0)
	((= n 1) 1)
	((= n 2) 2)
	(else (+ (f (- n 1))
		 (* 2 (f (- n 2)))
		 (* 3 (f (- n 3)))))))


(f 3)
