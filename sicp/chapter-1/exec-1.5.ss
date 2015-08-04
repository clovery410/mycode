(define (p) (p))
(define (test x y)
  (if (= x 0) 0 y))

(p)
(test 0 1)
(test 0 (p))
