
(define (insert-item item alist n)
  (cond ((= n 0)
	 (cons item alist))
	(#t
	 (cons (car alist) (insert-item item (cdr alist) (- n 1))))))

(define (double alist)
  (map (lambda (x) (* x 2)) alist))

(define (minus alist blist)
  (map - alist blist))

(define bank-account
  (let ((balance 10))
    (lambda (n)
      (set! balance (+ balance n))
      balance)))

(define-syntax nil!
  (syntax-rules ()
    ((_ x)
     (set! x '()))))

(define (f-nil! x)
  (set! x '()))

(define (split alist)
  (let loop
      ((numbers alist)
       (nonneg '())
       (neg '()))
    (cond ((null? numbers)
	   (list nonneg neg))
	  ((>= (car numbers) 0)
	   (loop (cdr numbers)
		 (cons (car numbers) nonneg)
		 neg))
	  (else
	   (loop (cdr numbers)
		 nonneg
		 (cons (car numbers) neg))))))
