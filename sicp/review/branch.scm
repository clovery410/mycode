(define (absolute x)
  (if (>= x 0) x
      (- 0 x)))

(define (revert x)
  (if (= x 0) #f
      (/ 1 x)))

(define (convert x)
  (if (<= 33 x 126)
      (integer->char x)
      #F))

(define (multiply x y z)
  (and (positive? x)
       (positive? y)
       (positive? z)
       (* a b c)))

(define (multiply2 x y z)
  (if (or (negative? x)
	  (negative? y)
	  (negative? z))
      (* x y z)))

(define (score x)
  (cond ((>= x 80) 'A)
	((<= 60 x 79) 'B)
	((<= 40 x 59) 'C)
	(else 'D)))
