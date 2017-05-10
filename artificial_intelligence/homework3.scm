;;initialize the knowledge base
(define kb
  '())

;;this fucntion can query for current knowledge base, just for test use
(define (show)
  (display kb)
  (newline))

;;this fucntion takes in an index and a list, returns the corresponding element of that index
(define (nth-item index nums)
  (if (= index 1) (car nums)
      (nth-item (- index 1) (cdr nums))))

;;this function takes in an index n, a list and a value, replaces the nth element with the new value, then returns the new lsit.
(define (replace-nth-item n items val)
  (if (= n 1)
      (cons val (cdr items))
      (cons (car items)
	    (replace-nth-item (- n 1) (cdr items) val))))

;;this function takes in an index n, a list, returns a new list after removing the element of that index
(define (remove-nth-item n items)
  (if (= n 1)
      (cdr items)
      (cons (car items)
	    (remove-nth-item (- n 1) (cdr items)))))

;;This function can check whether the element is part of the list. Returns #t if yes, otherwise #f
(define (member? elem alist)
  (if (null? alist) #f
      (if (equal? elem (car alist)) #t
	  (member? elem (cdr alist)))))

;;this function takes in an element and a list, returns the first index of that element in the list. Before calling this fucntion, we will check whether the element in the list and only calls when it does.
(define (get-index-of-element elem alist)
  (if (null? alist) 0
      (if (equal? elem (car alist)) 1
	  (+ 1 (get-index-of-element elem (cdr alist))))))

;;this function returns a new list of the first n element in the input list
(define (get-n-items alist n)
  (if (> n 0)
      (cons (car alist) (get-n-items (cdr alist) (- n 1)))
      '()))

;;this function takes in a list, a start position, and the total number to slice in that list, then returns a sublist, for example, (get-sublist '(1 2 3 4) 1 2) will return (1 2).
(define (get-sublist alist start count)
  (if (> start 1)
      (get-sublist (cdr alist) (- start 1) count)
      (get-n-items alist count)))

;;this function checkes whether a clause is an unit-disjunction
(define (unit-clause? clause)
  (cond ((= (length clause) 1) #t)
	((and (= (length clause) 2)
	      (equal? (car clause) 'NOT)) #t)
	(else #f)))

;;this function checks whether two variables are mutual negated.
(define (is-negate? var1 var2)
  (cond ((and (list? var1) (list? var2)) #f)
	((and (list? var1) (equal? (nth-item 2 var1) var2)) #t)
	((and (list? var2) (equal? (nth-item 2 var2) var1)) #t)
	(else #f)))

;;this function takes in a variable, returns it's negated
(define (negate var)
  (cond ((list? var) (nth-item 2 var))
	(else (list 'NOT var))))

;;this function takes in a literal, returns the negated literal
(define (negate-clause clause)
  (cond ((unit-clause? clause) (list (negate (car clause))))
	(else (cons (negate (car clause)) (negate-clause (cdr clause))))))

;;this function do the work of removing duplicate literals
(define (remove-dup clause)
  (if (null? clause) '()
      (let ((curr (car clause)))
	(if (member? curr (cdr clause))
	    (remove-dup (cdr clause))
	    (cons curr (remove-dup (cdr clause)))))))

;;this is a helper function for resolve function, which iteratively check does any variable in clause1 has its negate in clause2. If it does, it returns the two element's corresponding index. If it doesnot, return #f
(define (resolve-helper clause1 clause2)
  (let loop
      ((variables clause1)
       (curr-index 1))
    (cond ((null? variables)
	   #f)
	  ((member? (negate (car variables)) clause2)
	   (list (get-index-of-element (car variables) clause1)
		 (get-index-of-element (negate (car variables)) clause2)))
	  (else
	   (loop (cdr variables)
		 (+ curr-index 1))))))

;;this is resolve function API, it does two iterations.
(define (resolve clause1 clause2)
  (if (and (= (length clause1) (length clause2) 1)
	   (is-negate? (car clause1) (car clause2)))
      'CONTRADICTION
      (let ((first-iter (resolve-helper clause1 clause2)))
	(if (not first-iter)
	    #f
	    (let* ((index1 (nth-item 1 first-iter))
		   (index2 (nth-item 2 first-iter))
		   (new-clause1 (remove-nth-item index1 clause1))
		   (new-clause2 (remove-nth-item index2 clause2))
		   (second-iter (resolve-helper new-clause1 new-clause2)))
	      (if (not second-iter)
		  (remove-dup (append new-clause1 new-clause2))
		  #f))))))

;;this function takes in a whole clause, then resolve with each other, return the resolved result
(define (resolve-each-other clauses)
  (let iter-i ((i 1)
	       (result clauses))
    (if (> i (length clauses))
	result
	(let iter-j ((j i)
		     (result result))
	  (if (> j (length clauses))
	      (iter-i (+ i 1) result)
	      (iter-j (+ j 1)
		      (let* ((clause1 (nth-item i clauses))
			     (clause2 (nth-item j clauses))
			     (curr-resolvent (resolve clause1 clause2)))
			(if (or (not curr-resolvent)
				(equal? curr-resolvent 'CONTRADICTION))
			    result
			    (if (member? curr-resolvent result)
				result
				(cons curr-resolvent result))))))))))

;;this is a helper function used in ask API, similar as resolve-each-other, only differece is that this function will tackle with CONTRADICTION, which will produce an empty literal.
(define (resolve-find-contradict clauses)
    (let iter-i ((i 1)
	       (result clauses))
    (if (> i (length clauses))
	result
	(let iter-j ((j i)
		     (result result))
	  (if (> j (length clauses))
	      (iter-i (+ i 1) result)
	      (iter-j (+ j 1)
		      (let* ((clause1 (nth-item i clauses))
			     (clause2 (nth-item j clauses))
			     (curr-resolvent (resolve clause1 clause2)))
			(cond ((equal? curr-resolvent 'CONTRADICTION) (cons '() result))
			      ((not curr-resolvent) result)
			      (else
			       (if (member? curr-resolvent result)
				   result
				   (cons curr-resolvent result)))))))))))

;;this is tell function API, accepts cnf sentences, and will update the kb as what been told.
(define (tell clause)
  (if (member? clause kb)
      'OK
      (let loop
	  ((kb-candidate (append kb (list clause))))
	(let ((resolve-result (resolve-each-other kb-candidate)))
	  (begin (set! kb resolve-result)
		 (if (= (length kb-candidate) (length resolve-result))
		     'OK
		     (loop kb)))))))

;;this is ask funtion API, can ask both unit-clause and cnf, returns #t if the negate of the clause contradics kb, otherwise return UNKNOWN
(define (ask clause)
  (let iter-i
      ((i 1)
       (premise (negate-clause clause)))
    (if (> i (length clause)) #f
	(let iter-j
	    ((kb-candidate (cons (list (nth-item i premise)) kb)))
	  (let ((resolve-result (resolve-find-contradict kb-candidate)))
	    (if (member? '() resolve-result) #t
		(if (= (length kb-candidate) (length resolve-result)) (iter-i (+ i 1) premise)
		    (iter-j resolve-result))))))))

;;Following are the codes for Quesiton 3, not finish yet

;;Eliminate biconditional and implies
(define (eliminate-implications p)
  (if (or (not (list? p)) (unit-clause? p)) p
      (cond ((equal? (car p) 'IMPLIES) (list 'OR (list 'NOT (nth-item 2 p)) (nth-item 3 p)))
	    ((equal? (car p) 'BICONDITIONAL)
	     (list 'AND
		   (list 'OR (list 'NOT (nth-item 2 p)) (nth-item 3 p))
		   (list 'OR (list 'NOT (nth-item 3 p)) (nth-item 2 p))))
	    (else (cons (car p) (map eliminate-implications (cdr p)))))))

;;this fucntion do a not first, then move the not inward
(define (move-not-inwards p)
  (if (not (list? p)) (list 'NOT p)
      (let ((op (car p)))
	(cond ((equal? op #t) #f)
	      ((equal? op #f) #t)
	      ((equal? op 'NOT) (cdr p))
	      ((equal? op 'AND) (disjunction (map move-not-inwards (cdr p))))
	      ((equal? op 'OR) (conjunction (map move-not-inwards (cdr p))))))))

(define (simplify sentence)
  (let ((sentence-without-implies (eliminate-implications sentence)))
    (move-not-inwards sentence-without-implies)))


;; ;;not finish yet...
;; (define (convert-to-cnf p)
;;   (begin (set! p (eliminate-implications p))
;; 	 (let ((op (car p)))
;; 	   (cond ((equal? op 'NOT) (let ((p2 (move-not-inwards (cdr p))))
;; 				     (if (unit-clause? p2) p2 (convert-to-cnf p2))))
;; 		 ((equal? op 'OR) (merge-disjuncts (map convert-to-cnf (cdr p))))
;; 		 ((equal? op 'AND) (
  
;;Return a list of the conjuncts in this formula
(define (conjuncts formula)
  (cond ((equal? (car formula) 'AND) (cdr formula))
	(else (list formula))))

;;Return a list of the disjuncts in this formula
(define (disjuncts formula)
  (cond ((equal? (car formula) 'OR) (cdr formula))
	(else (list formula))))

;;Make a conjunction of literals
(define (conjunction clause)
  (if (list? clause)
      (if (= (length clause) 1)
	  (car clause)
	  (cons 'AND clause))
      clause))

;;Make a disjunction of literals
(define (disjunction clause)
  (if (list? clause)
      (if (= (length clause) 1)
	  (car clause)
	  (cons 'OR clause))
      clause))
