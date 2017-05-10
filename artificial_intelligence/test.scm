
(define (is-in-range val lower upper)
        (cond ((> val upper) #f)
              ((< val lower) #f)
              (#t #t)))

(define (is-in-range val lower upper)
        (if (and (<= val upper)
                 (>= val lower))
            #t
            #f))

; (define (is-in-range val lower upper)
;        (and (<= val upper)
;             (>= val lower)))
;

(define (count-elems alist)
        (if (null? alist) 0
            (+ 1 (count-elems (cdr alist)))))

(define (add-const alist num)
        (if (null? alist) '()
            (cons (+ (car alist) num)
                  (add-const (cdr alist) num))))

; Print the numbers up to 6, starting at num
(define (print-num num)
        (if (> num 6)
            (newline)
            (begin (display num)
                   (newline)
                   (print-num (+ 1 num)))))

(define (print-one-to-six)
        (print-num 1))


