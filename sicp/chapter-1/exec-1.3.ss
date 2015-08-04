
(define (squar x)
  (* x x))

(define (square-sum a b)
  (+ (squar a) (squar b)))

(define (sum-squar a b c)
  (cond ((and (< a b) (< a c)) (square-sum b c))
	((and (< b c) (< b a)) (square-sum a c))
	((and (< c a) (< c b)) (square-sum a b))))

(sum-squar 1 2 3)
(min 1 2 3)
