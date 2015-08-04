(define (length items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

(define (getitem items n)
  (if (= n 0)
      (car items)
      (getitem (cdr items) (- n 1))))

(define squares (list 1 4 9 16 25))

(length squares)
(getitem squares 3)
