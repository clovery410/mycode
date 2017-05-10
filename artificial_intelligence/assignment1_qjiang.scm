;1. find-biggest
(define (find-biggest alist)
  (if (null? (cdr alist)) (car alist)
      (if (> (car alist) (find-biggest (cdr alist)))
	  (car alist)
	  (find-biggest (cdr alist)))))

;2. count-from
(define (count-from first second)
  (if (<= first second)
      (begin (display first)
	     (newline)
	     (count-from (+ first 1) second))))

;3. nth-item
(define (nth-item index nums)
  (if (= index 1) (car nums)
      (nth-item (- index 1) (cdr nums))))

;4. replace-nth-item
(define (replace-nth-item n items val)
  (if (= n 1)
      (cons val (cdr items))
      (cons (car items)
	    (replace-nth-item (- n 1) (cdr items) val))))

;5. sorted?
(define (sorted? alist)
  (cond ((or (null? alist) (null? (cdr alist))) #t)
	(else (and (<= (car alist) (car (cdr alist)))
		   (sorted? (cdr alist))))))

;6. apply-action
(define (apply-action action state)
  (let ((x (nth-item 1 action)) (y (nth-item 2 action)) (dir (nth-item 3 action)))
       (cond ((equal? state "STAY") action)
	     ((equal? state "MOVE-1") (cond ((equal? dir (quote N)) (replace-nth-item 2 action (+ y 1)))
					    ((equal? dir (quote S)) (replace-nth-item 2 action (- y 1)))
					    ((equal? dir (quote W)) (replace-nth-item 1 action (- x 1)))
					    ((equal? dir (quote E)) (replace-nth-item 1 action (+ x 1)))
					    (else #t)))
	     ((equal? state "MOVE-2") (cond ((equal? dir (quote N)) (replace-nth-item 2 action (+ y 2)))
					    ((equal? dir (quote S)) (replace-nth-item 2 action (- y 2)))
					    ((equal? dir (quote W)) (replace-nth-item 1 action (- x 2)))
					    ((equal? dir (quote E)) (replace-nth-item 1 action (+ x 2)))
					    (else #t)))
	     ((equal? state "MOVE-3") (cond ((equal? dir (quote N)) (replace-nth-item 2 action (+ y 3)))
					    ((equal? dir (quote S)) (replace-nth-item 2 action (- y 3)))
					    ((equal? dir (quote W)) (replace-nth-item 1 action (- x 3)))
					    ((equal? dir (quote E)) (replace-nth-item 1 action (+ x 3)))
					    (else #t)))
	     ((equal? state "TURN-AROUND") (cond ((equal? dir (quote N)) (replace-nth-item 3 action 'S))
						 ((equal? dir (quote W)) (replace-nth-item 3 action 'E))
						 ((equal? dir (quote S)) (replace-nth-item 3 action 'N))
						 ((equal? dir (quote E)) (replace-nth-item 3 action 'W))
						 (else #t)))
	     ((equal? state "TURN-LEFT") (cond ((equal? dir (quote N)) (replace-nth-item 3 action 'W))
					       ((equal? dir (quote W)) (replace-nth-item 3 action 'S))
					       ((equal? dir (quote S)) (replace-nth-item 3 action 'E))
					       ((equal? dir (quote E)) (replace-nth-item 3 action 'N))
					       (else #t)))
	     ((equal? state "TURN-RIGHT") (cond ((equal? dir (quote N)) (replace-nth-item 3 action 'E))
						((equal? dir (quote W)) (replace-nth-item 3 action 'N))
						((equal? dir (quote S)) (replace-nth-item 3 action 'W))
						((equal? dir (quote E)) (replace-nth-item 3 action 'S))
						(else #t)))
	     (else #t))))

;7. get-location
(define (get-location percept x y)
  (if (= y 1) (nth-item (+ x 2) (car percept))
      (get-location (cdr percept) (+ x 1) (- y 1))))

;8. merge-ordered-lists
(define (merge-ordered-lists lst1 lst2)
  (cond ((null? lst1) lst2)
	((null? lst2) lst1)
	((<= (car lst1) (car lst2))
	 (cons (car lst1)
	       (merge-ordered-lists (cdr lst1) lst2)))
	(else (cons (car lst2)
		    (merge-ordered-lists lst1 (cdr lst2))))))

;9. merge-sort, first define a helper function to calculate the length of the array
(define (get-length lst)
  (if (null? lst) 0
      (+ 1 (get-length (cdr lst)))))

;Then define a second helper function to get the first half elements of the array
(define (get-first-half lst index)
  (if (< index 1) '()
      (cons (car lst) (get-first-half (cdr lst) (- index 1)))))

;Define a third helper function to get the second half elements of the array
(define (get-second-half lst index)
  (if (< index 1) lst
      (get-second-half (cdr lst) (- index 1))))

;Define merge-sort function by above helper functions
(define (merge-sort lst)
  (let ((l (get-length lst)))
    (cond ((= l 0) '())
	  ((= l 1) lst)
	  ((= l 2) (merge-ordered-lists (list (car lst)) (cdr lst)))
	  ((> l 2) (let ((mid (/ l 2)))
		     (merge-ordered-lists (merge-sort (get-first-half lst mid)) (merge-sort (get-second-half lst mid)))))
	  (else #t))))	      
