;This is iterative procedure
(define (h n)
  (h-iter 2 1 0 n))

(define (h-iter a b c count)
  (if (= count 0)
      c
      (h-iter (+ a (* 2 b) (* 3 c)) a b (- count 1))))


(h 3)
