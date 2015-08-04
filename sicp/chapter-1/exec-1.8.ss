(define (cubt-iter guess x)
  (if (good-enough? guess x)
      guess
      (cubt-iter (improve guess x) x)))

(define (improve guess x)
  (/ (+ (/ x 
	   (square guess))
	(* 2 guess))
     3))

(define (good-enough? guess x)
  (< (abs (- (* guess guess guess) x)) 0.001))

(define (cubt x)
  (cubt-iter 1.0 x))

(cubt 8)
