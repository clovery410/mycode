(define (initialize-agent)
  "OK")

;;this function returns the smallest element in a given list
(define (find-smallest alist)
  (if (null? (cdr alist)) (car alist)
      (if (< (car alist) (find-smallest (cdr alist)))
	  (car alist)
	  (find-smallest (cdr alist)))))

;;this function returns a biggest element in a given list
(define (find-biggest alist)
  (if (null? (cdr alist)) (car alist)
      (if (> (car alist) (find-biggest (cdr alist)))
	  (car alist)
	  (find-biggest (cdr alist)))))

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

;;this function get the corresponding content of a percept from x, y coordinates
(define (get-location percept x y)
  (if (= y 1) (nth-item (+ x 2) (car percept))
      (get-location (cdr percept) (+ x 1) (- y 1))))

;;this function tell whether this location is an empty spot
(define (is-empty? location)
  (if (equal? location 'empty)
      #t
      #f))

;;this function tell whether this location is a barrier
(define (is-barrier? location)
  (if (equal? location 'barrier)
      #t
      #f))

;;this function tell whether this location is a vegetation or not
(define (is-vegetation? location)
  (if (and (list? location) (= (length location) 3))
      #t
      #f))

;;this function get the current vegetable energy from a location
(define (get-vegetation-energy location)
  (nth-item 3 location))

;;this function tell whether this location is a predator or not
(define (is-predator? location)
  (if (and (list? location) (= (length location) 2))
      #t
      #f))

;;this fucntion get the id of a predator from a location
(define (get-predator-id location)
  (nth-item 2 location))

;;this function tell whether this location is other agent or not
(define (is-agent? location)
  (if (and (list? location) (= (length location) 4))
      #t
      #f))

;;this function calculate the log base 2 value of a number
(define (log-base2 number)
  (/ (log number) (log 2)))

;;this function get the approximate energy level of an agent
(define (get-agent-energy location)
  (expt 2 (nth-item 3 location)))

;;this function get the direction of an agent
(define (get-agent-direction location)
  (nth-item 4 location))

;;this function return the new state after apply corresponding action
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

;;this function determines whether the agent was attacked by predator in last turn
(define (is-attacked? previous-events)
  (if (null? previous-events) #f
      (let ((curr-event (car previous-events)))
	(if (equal? (car curr-event) 'attacked-by) #t
	    (is-attacked? (cdr previous-events))))))

;;this function returns the damage level from is-attacked?
(define (get-damage-level previous-events)
  (if (not (is-attacked? previous-events)) 0
      (let ((curr-event (car previous-events)))
	(if (equal? (car curr-event) 'attacked-by) (nth-item 3 curr-event)
	    (get-damage-level (cdr previous-events))))))
      
;;this function determines whether the agent eat the vegetation in last turn
(define (is-ate? previous-events)
  (if (null? previous-events) #f
      (let ((curr-event (car previous-events)))
	(if (equal? (car curr-event) 'ate) #t
	    (is-ate? (cdr previous-events))))))

;;this function determines whether the agent was fought by other agent in last turn
(define (is-fought? previous-events)
  (if (null? previous-events) #f
      (let ((curr-event (car previous-events)))
	(if (equal? (car curr-event) 'fought) #t
	    (is-fought? (cdr previous-events))))))

;;this function tells whether a location is surrounded by predator
(define (surround-by-predator? x y percepts)
  (or (is-predator? (get-location percepts x (+ y 1)))
      (is-predator? (get-location percepts (- x 1) y))
      (is-predator? (get-location percepts (+ x 1) y))))

;;this function tells whether a location is surrounded by vegetation
(define (surround-by-vegetation? x y percepts)
  (or (is-vegetation? (get-location percepts x (+ y 1)))
      (is-vegetation? (get-location percepts (- x 1) y))
      (is-vegetation? (get-location percepts (+ x 1) y))))

;;this function returns #f if there is no other agents around a location or the agents all weaker than me, otherwise return #t
(define (stronger-than-me? x y percepts my-energy)
  (let ((above (get-location percepts x (+ y 1)))
	(left (get-location percepts (- x 1) y))
	(right (get-location percepts (+ x 1) y)))
    (or (and (is-agent? above)
	     (> (get-agent-energy above) my-energy))
	(and (is-agent? left)
	     (> (get-agent-energy left) my-energy))
	(and (is-agent? right)
	     (> (get-agent-energy right) my-energy)))))

;;this function tells whether the straight line has vegetation
(define (has-vegetation-this-line? percepts)
  (or (is-vegetation? (get-location percepts 0 1))
      (is-vegetation? (get-location percepts 0 2))
      (is-vegetation? (get-location percepts 0 3))
      (is-vegetation? (get-location percepts 0 4))
      (is-vegetation? (get-location percepts 0 5))))

;;this function calculate the score of stay
(define (stay-score previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (cond ((is-attacked? previous-events) -1000)
	  ((is-barrier? origin-state) -1000)
	  ((is-predator? origin-state) -1000)
	  ((is-ate? previous-events) -1)
	  (#t -10))))
	 
;;this function calculate the score of turn left
(define (turn-left-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-left (get-location percepts -1 1)))
    (cond ((is-barrier? origin-state) (- 50 2))
	  ((is-barrier? origin-left) -1000)
	  ((is-predator? origin-state) (- 50 2))
	  ((is-ate? previous-events) (- 40 2))
	  ((and (is-attacked? previous-events)
		(is-empty? origin-state)) -102)
	  (#t -2))))
	 
;;this function calculate the score of turn right
(define (turn-right-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-right (get-location percepts 1 1)))
    (cond ((is-barrier? origin-state) (- 50 2))
	  ((is-barrier? origin-right) -1000)
	  ((is-predator? origin-state) (- 50 2))
	  ((is-ate? previous-events) (- 40 2))
	  ((and (is-attacked? previous-events)
		(is-empty? origin-state)) -102)
	  (#t -2))))

;;this function calculate the score of turn around
(define (turn-around-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (cond ((is-barrier? origin-state) (- 50 2))
	  ((is-predator? origin-state) (- 50 2))
	  ((is-ate? previous-events) (- 40 2))
	  ((and (is-attacked? previous-events)
		(is-empty? origin-state)) -102)
	  (#t -2))))

;;this function calculate the score of move passive 1
(define (move-passive-1-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (cond ((not (is-empty? origin-state)) -1000)
	  ((surround-by-predator? 0 1 percepts) -1000)
	  ((is-attacked? previous-events) 100)
	  ((surround-by-vegetation? 0 1 percepts) 200)
	  ((has-vegetation-this-line? percepts) 200)
	  (#t -10))))
	 
;;this function calculate the score of move passive 2
(define (move-passive-2-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2)))
    (cond ((or (not (is-empty? origin-state))
	       (not (is-empty? origin-above-state))) -1000)
	  ((surround-by-predator? 0 2 percepts) -1000)
	  ((is-attacked? previous-events) 200)
	  ((surround-by-vegetation? 0 2 percepts) 200)
	  ((has-vegetation-this-line? percepts) 150)
	  (#t -30))))

;;this function calculate the score of move passive 3
(define (move-passive-3-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2))
	 (origin-above2-state (get-location percepts 0 3)))
    (cond ((or (not (is-empty? origin-state))
	       (not (is-empty? origin-above-state))
	       (not (is-empty? origin-above2-state))) -1000)
	  ((surround-by-predator? 0 3 percepts) -1000)
	  ((is-attacked? previous-events) 300)
	  ((surround-by-vegetation? 0 3 percepts) 200)
	  ((has-vegetation-this-line? percepts) 120)
	  (#t -60))))

;;this function calculate the score of move aggressive 1
(define (move-aggressive-1-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (cond ((not (is-empty? origin-state)) -1000)
	  ((surround-by-predator? 0 1 percepts) -1000)
	  ((is-attacked? previous-events) 120)
	  ((surround-by-vegetation? 0 1 percepts) 220)
	  ((has-vegetation-this-line? percepts) 200)
	  (#t -10))))

;;this function calculate the score of move aggressive 2
(define (move-aggressive-2-score previous-events percepts)
    (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2)))
    (cond ((or (not (is-empty? origin-state))
	       (not (is-empty? origin-above-state))) -1000)
	  ((surround-by-predator? 0 2 percepts) -1000)
	  ((is-attacked? previous-events) 220)
	  ((surround-by-vegetation? 0 2 percepts) 220)
	  ((has-vegetation-this-line? percepts) 150)
	  (#t -30))))

;;this function calculate the score of move aggressive 3
(define (move-aggressive-3-score previous-events percepts)
    (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2))
	 (origin-above2-state (get-location percepts 0 3)))
    (cond ((or (not (is-empty? origin-state))
	       (not (is-empty? origin-above-state))
	       (not (is-empty? origin-above2-state))) -1000)
	  ((surround-by-predator? 0 3 percepts) -1000)
	  ((is-attacked? previous-events) 320)
	  ((surround-by-vegetation? 0 3 percepts) 220)
	  ((has-vegetation-this-line? percepts) 120)
	  (#t -60))))

;;this function calculate the score after passive eating
(define (eat-passive-score previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (cond ((and (is-vegetation? origin-state)
		(> (get-vegetation-energy origin-state)
		   (get-damage-level previous-events)) 500))
	  (#t -5))))

;;this function calculate the score after aggressive eating
(define (eat-aggressive-score current-energy previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (cond ((and (is-vegetation? origin-state)
		(> (get-vegetation-energy origin-state)
		   (get-damage-level previous-events))
		(not (stronger-than-me? 0 1 percepts current-energy))) 700)
	  (#t -5))))

(define (choose-action current-energy previous-events percepts)
  (let* ((s-score (stay-score previous-events percepts))
	 (tr-score (turn-right-score previous-events percepts))
	 (tf-score (turn-left-score previous-events percepts))
	 (ta-score (turn-around-score previous-events percepts))
	 (mp1-score (move-passive-1-score previous-events percepts))
	 (mp2-score (move-passive-2-score previous-events percepts))
	 (mp3-score (move-passive-3-score previous-events percepts))
	 (ma1-score (move-aggressive-1-score previous-events percepts))
	 (ma2-score (move-aggressive-2-score previous-events percepts))
	 (ma3-score (move-aggressive-3-score previous-events percepts))
	 (ep-score (eat-passive-score previous-events percepts))
	 (ea-score (eat-aggressive-score current-energy previous-events percepts))
	 (max-score (find-biggest (list s-score tr-score tf-score ta-score
					mp1-score mp2-score mp3-score ma1-score
					ma2-score ma3-score ep-score ea-score))))
    (cond ((equal? max-score s-score) "STAY")
	  ((equal? max-score tr-score) "TURN-RIGHT")
	  ((equal? max-score tf-score) "TURN-LEFT")
	  ((equal? max-score ta-score) "TURN-AROUND")
	  ((equal? max-score mp1-score) "MOVE-PASSIVE-1")
	  ((equal? max-score mp2-score) "MOVE-PASSIVE-2")
	  ((equal? max-score mp3-score) "MOVE-PASSIVE-3")
	  ((equal? max-score ma1-score) "MOVE-AGGRESSIVE-1")
	  ((equal? max-score ma2-score) "MOVE-AGGRESSIVE-2")
	  ((equal? max-score ma3-score) "MOVE-AGGRESSIVE-3")
	  ((equal? max-score ep-score) "EAT-PASSIVE")
	  ((equal? max-score ea-score) "EAT-AGGRESSIVE")
	  (#f "STAY"))))
