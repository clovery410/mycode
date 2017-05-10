(load "factor.scm")
;; f1: is-stay
;; f2: is-turn
;; f3: is-move1
;; f4: is-move2
;; f5: is-move3
;; f6: is-eat

;; f7: is-strongest-within-1
;; f8: is-strongest-within-2
;; f9: is-strongest-within-3
;; f10: is-current-not-accessible
;; f11: is-left-hand-vege
;; f12: is-right-hand-vege
;; f13: is-left-side-has-vege
;; f14: is-right-side-has-vege
;; f15: is-straight-line-has-vege
;; f16: is-surround-by-predator
;; f17: is-not-running-away-underattack
;; f18: is-facing-predator-when-stay
;; f19: is-taking-action-underattack
;; f20: is-eating-front-vege-has-gain
;; f21: is-making-turn-facing-barrier
;; f22: is-turning-to-barrier
;; f23: is-making-turn-facing-predator
;; f24: is-making-turn-after-eating
;; f25: is-surround-by-vegetation
;; f26: is-nothing-to-eat
;; f27: is-escaping-mode

(define (initialize-agent)
  "OK")

(define left-corner
  '())

(define right-corner
  '())

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

;;this function tell whether a road (across y-axis) from lower-point to higher-point is empty
(define (is-road-empty? percepts lower higher)
  (if (> lower higher) #t
      (let ((curr-location (get-location percepts 0 lower)))
	(if (is-empty? curr-location) (is-road-empty? percepts (+ lower 1) higher)
	    #f))))

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

;;this function calculate the feature 10, is-current-not-accessible, yes return 1, no return 0
(define (is-current-not-accessible percepts x y)
  (let ((curr-location (get-location percepts x y)))
    (cond ((is-barrier? curr-location) 1)
	  ((is-predator? curr-location) 1)
	  ((is-vegetation? curr-location) 1)
	  ((is-agent? curr-location) 1)
	  (#t (if (= y 1)
		  0
		  (is-current-not-accessible percepts x (- y 1)))))))

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

;;this function calculate the feature19, is-taking-action-underattack, yes reuturn 1, no return 0
(define (is-taking-action-underattack previous-events percepts moving-steps)
  (let ((step1 (get-location percepts 0 1))
	(step2 (get-location percepts 0 2))
	(step3 (get-location percepts 0 3)))
    (if (is-attacked? previous-events)
	(cond ((= moving-steps 1)
	       (if (is-empty? step1) 1 0))
	      ((= moving-steps 2)
	       (if (and (is-empty? step1) (is-empty? step2)) 1 0))
	      ((= moving-steps 3)
	       (if (and (is-empty? step1) (is-empty? step2) (is-empty? step3)) 1 0))
	      (#t 0))
	0)))

;;this function calculate the feature17, is-not-running-away-underattack, yes return 1, no return 0
(define (is-not-running-away-underattack previous-events origin-state action)
  (if (and (is-attacked? previous-events)
	   (is-empty? origin-state)
	   (or (equal? action "STAY")
	       (equal? action "TURN-LEFT")
	       (equal? action "TURN-RIGHT")
	       (equal? action "TURN-AROUND")
	       (equal? action "EAT-PASSIVE")
	       (equal? action "EAT-AGGRESSIVE")))
      1
      0))

;;this function calculate the feature18, is-facing-predator-when-stay, yes return 1, no return 0
(define (is-facing-predator-when-stay percepts)
  (if (is-predator? (get-location percepts 0 1)) 1
      0))

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
  (if (= y 0)
      (or (is-predator? (get-location percepts 0 1))
	  (is-predator? left-corner)
	  (is-predator? right-corner))
      (or (is-predator? (get-location percepts x (+ y 1)))
	  (is-predator? (get-location percepts (- x 1) y))
	  (is-predator? (get-location percepts (+ x 1) y)))))

;;this function calculate feature25, is-surround-by-vegetation, yes return 1, no return 0
(define (is-surround-by-vegetation x y percepts)
  (let ((above (get-location percepts x (+ y 1)))
	(left (get-location percepts (- x 1) y))
	(right (get-location percepts (+ x 1) y)))
    (if (or (and (is-vegetation? above) (> (get-vegetation-energy above) 0))
	    (and (is-vegetation? left) (> (get-vegetation-energy left) 0))
	    (and (is-vegetation? right) (> (get-vegetation-energy right) )))
	1
	0)))
	    
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

;;this function calculate feature7, is-strongest-within-1, yes return #t, no return #f
(define (is-strongest-within-1 my-energy percepts)
  (let ((above1 (get-location percepts 0 2))
	(above2 (get-location percepts 0 3))
	(above3 (get-location percepts 0 4))
	(left1 (get-location percepts -1 1))
	(right1 (get-location percepts 1 1)))
    (and (or (not (is-agent? above1))
	     (> my-energy (get-agent-energy above1)))
	 (or (not (is-agent? above2))
	     (> my-energy (get-agent-energy above2)))
	 (or (not (is-agent? above3))
	     (> my-energy (get-agent-energy above3)))
	 (or (not (is-agent? left1))
	     (> my-energy (get-agent-energy left1)))
	 (or (not (is-agent? right1))
	     (> my-energy (get-agent-energy right1))))))

;;this function calculate feature8, is-strongest-within-2, yes return #t, no return #f
(define (is-strongest-within-2 my-energy percepts)
  (let ((above1 (get-location percepts 0 3))
	(above2 (get-location percepts 0 4))
	(above3 (get-location percepts 0 5))
	(left1 (get-location percepts -1 2))
	(left2 (get-location percepts -2 2))
	(right1 (get-location percepts 1 2))
	(right2 (get-location percepts 2 2)))
    (and (or (not (is-agent? above1))
	     (> my-energy (get-agent-energy above1)))
	 (or (not (is-agent? above2))
	     (> my-energy (get-agent-energy above2)))
	 (or (not (is-agent? above3))
	     (> my-energy (get-agent-energy above3)))
	 (or (not (is-agent? left1))
	     (> my-energy (get-agent-energy left1)))
	 (or (not (is-agent? left2))
	     (> my-energy (get-agent-energy left2)))
	 (or (not (is-agent? right1))
	     (> my-energy (get-agent-energy right1)))
	 (or (not (is-agent? right2))
	     (> my-energy (get-agent-energy right2))))))

;;this function calculate feature9, is-strongest-within-3, yes return #t, no return #f
(define (is-strongest-within-3 my-energy percepts)
  (let ((above1 (get-location percepts 0 4))
	(above2 (get-location percepts 0 5))
	(left1 (get-location percepts -1 3))
	(left2 (get-location percepts -2 3))
	(left3 (get-location percepts -3 3))
	(right1 (get-location percepts 1 3))
	(right2 (get-location percepts 2 3))
	(right3 (get-location percepts 3 3)))
    (and (or (not (is-agent? above1))
	     (> my-energy (get-agent-energy above1)))
	 (or (not (is-agent? above2))
	     (> my-energy (get-agent-energy above2)))
	 (or (not (is-agent? left1))
	     (> my-energy (get-agent-energy left1)))
	 (or (not (is-agent? left2))
	     (> my-energy (get-agent-energy left2)))
	 (or (not (is-agent? left3))
	     (> my-energy (get-agent-energy left3)))
	 (or (not (is-agent? right1))
	     (> my-energy (get-agent-energy right1)))
	 (or (not (is-agent? right2))
	     (> my-energy (get-agent-energy right2)))
	 (or (not (is-agent? right3))
	     (> my-energy (get-agent-energy right3))))))

;;this function tells whether the straight line has vegetation
(define (has-vegetation-this-line? percepts)
  (or (is-vegetation? (get-location percepts 0 1))
      (is-vegetation? (get-location percepts 0 2))
      (is-vegetation? (get-location percepts 0 3))
      (is-vegetation? (get-location percepts 0 4))
      (is-vegetation? (get-location percepts 0 5))))

;;this function caculate the left corner gain, returns the vegetation energy level in last turn, if no vege, returns 0
(define (left-corner-gain left-corner)
  (cond ((null? left-corner) 0)
	((is-vegetation? left-corner) (get-vegetation-energy left-corner))
	(#t 0)))

;;this function calculate the right corner gain, returns the vegetation energy level in last turn, if no vege, returns 0
(define (right-corner-gain right-corner)
  (cond ((null? right-corner) 0)
	((is-vegetation? right-corner) (get-vegetation-energy right-corner))
	(#t 0)))

;;this function calculate the feature11, is-left-hand-vege
(define (is-left-hand-vege left-corner)
  (if (> (left-corner-gain left-corner) 0)
      1
      0))

;;this function calculate the feature12, is-right-hand-vege
(define (is-right-hand-vege right-corner)
  (if (> (right-corner-gain right-corner) 0)
      1
      0))

;;this function calculate the feature20, is-eating-front-vege-has-gain, yes return 1, no return 0
(define (is-eating-front-vege-has-gain percepts previous-events)
  (let ((front-location (get-location percepts 0 1)))
    (if (and (is-vegetation? front-location)
	     (> (get-vegetation-energy front-location)
		(get-damage-level previous-events)))
	1
	0)))

;;this function calculate the feature26, is-nothing-to-eat, yes return 1, no return 0
(define (is-nothing-to-eat percepts)
  (let ((front-location (get-location percepts 0 1)))
    (if (and (is-vegetation? front-location)
	     (> (get-vegetation-energy front-location) 0))
	0
	1)))

;;this function calculate the feature27, is-escaping-mode, yes return 1, no return 0
(define (is-escaping-mode percepts previous-events steps)
  (if (and (is-attacked? previous-events)
	   (is-road-empty? percepts 1 steps))
      1
      0))

;;this function calculate the score of stay
(define (stay-score previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (+ (* (is-not-running-away-underattack previous-events origin-state "STAY") w17)
       (* (is-current-not-accessible percepts 0 1) w10)
       (* (is-facing-predator-when-stay percepts) w18)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       w1)))

;;this function calculate the score of turn left
(define (turn-left-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-left (get-location percepts -1 1)))
    (+ (if (is-barrier? origin-state) w21 0)
       (if (is-barrier? origin-left) w22 0)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       (* (is-left-hand-vege left-corner) w11)
       (if (is-predator? origin-state) w23 0)
       (if (is-ate? previous-events) w24 0)
       (* (is-not-running-away-underattack previous-events origin-state "TURN-LEFT") w17)
       w2)))

;;this function calculate the score of turn right
(define (turn-right-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-right (get-location percepts 1 1)))
    (+ (if (is-barrier? origin-state) w21 0)
       (if (is-barrier? origin-right) w22 0)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       (* (is-right-hand-vege right-corner) w12)
       (if (is-predator? origin-state) w23 0)
       (if (is-ate? previous-events) w24 0)
       (* (is-not-running-away-underattack previous-events origin-state "TURN-RIGHT") w17)
       w2)))

;;this function calculate the score of turn around
(define (turn-around-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (+ (if (is-barrier? origin-state) w21 0)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       (if (is-predator? origin-state) w23 0)
       (if (is-ate? previous-events) w24 0)
       (* (is-not-running-away-underattack previous-events origin-state "TURN-AROUND") w17)
       w2)))

;;this function calculate the score of move passive 1
(define (move-passive-1-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (+ (* (is-current-not-accessible percepts 0 1) w10)
       (if (surround-by-predator? 0 1 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 1) w19)
       (if (has-vegetation-this-line? percepts) w15 0)
       w3)))

;;this function calculate the score of move passive 2
(define (move-passive-2-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2)))
    (+ (* (is-current-not-accessible percepts 0 2) w10)
       (if (surround-by-predator? 0 2 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 2) w19)
       (* (is-escaping-mode percepts previous-events 2) w27)
       (* (is-surround-by-vegetation 0 2 percepts) w25)
       (if (has-vegetation-this-line? percepts) w15 0)
       w4)))

;;this function calculate the score of move passive 3
(define (move-passive-3-score previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2))
	 (origin-above2-state (get-location percepts 0 3)))
    (+ (* (is-current-not-accessible percepts 0 3) w10)
       (if (surround-by-predator? 0 3 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 3) w19)
       (* (is-escaping-mode percepts previous-events 3) w27)
       (* (is-surround-by-vegetation 0 3 percepts) w25)
       (if (has-vegetation-this-line? percepts) w15 0)
       w5)))

;;this function calculate the score of move aggressive 1
(define (move-aggressive-1-score current-energy previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1)))
    (+ (* (is-current-not-accessible percepts 0 1) w10)
       (if (surround-by-predator? 0 1 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 1) w19)
       (if (has-vegetation-this-line? percepts) w15 0)
       (if (is-strongest-within-1 current-energy percepts) w7 0)
       w3)))

;;this function calculate the score of move aggressive 2
(define (move-aggressive-2-score current-energy previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2)))
    (+ (* (is-current-not-accessible percepts 0 2) w10)
       (if (surround-by-predator? 0 2 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 2) w19)
       (* (is-escaping-mode percepts previous-events 2) w27)
	 (* (is-surround-by-vegetation 0 2 percepts) w25)
	 (if (has-vegetation-this-line? percepts) w15 0)
	 (if (is-strongest-within-2 current-energy percepts) w8 0)
	 w4)))

;;this function calculate the score of move aggressive 3
(define (move-aggressive-3-score current-energy previous-events percepts)
  (let* ((origin-state (get-location percepts 0 1))
	 (origin-above-state (get-location percepts 0 2))
	 (origin-above2-state (get-location percepts 0 3)))
    (+ (* (is-current-not-accessible percepts 0 3) w10)
       (if (surround-by-predator? 0 3 percepts) w16 0)
       (* (is-taking-action-underattack previous-events percepts 3) w19)
       (* (is-escaping-mode percepts previous-events 3) w27)
       (* (is-surround-by-vegetation 0 3 percepts) w25)
       (if (has-vegetation-this-line? percepts) w15 0)
       (if (is-strongest-within-3 current-energy percepts) w9 0)
       w5)))

;;this function calculate the score after passive eating
(define (eat-passive-score previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (+ (* (is-eating-front-vege-has-gain percepts previous-events) w20)
       (* (is-nothing-to-eat percepts) w26)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       w6)))

;;this function calculate the score after aggressive eating
(define (eat-aggressive-score current-energy previous-events percepts)
  (let ((origin-state (get-location percepts 0 1)))
    (+ (* (is-eating-front-vege-has-gain percepts previous-events) w20)
       (* (is-nothing-to-eat percepts) w26)
       (if (not (stronger-than-me? 0 1 percepts current-energy)) w7 0)
       (if (surround-by-predator? 0 0 percepts) w16 0)
       w6)))

(define (choose-action current-energy previous-events percepts)
  (let* ((s-score (stay-score previous-events percepts))
	 (tr-score (turn-right-score previous-events percepts))
	 (tf-score (turn-left-score previous-events percepts))
	 (ta-score (turn-around-score previous-events percepts))
	 (mp1-score (move-passive-1-score previous-events percepts))
	 (mp2-score (move-passive-2-score previous-events percepts))
	 (mp3-score (move-passive-3-score previous-events percepts))
	 (ma1-score (move-aggressive-1-score current-energy previous-events percepts))
	 (ma2-score (move-aggressive-2-score current-energy previous-events percepts))
	 (ma3-score (move-aggressive-3-score current-energy previous-events percepts))
	 (ep-score (eat-passive-score previous-events percepts))
	 (ea-score (eat-aggressive-score current-energy previous-events percepts))
	 (max-score (find-biggest (list s-score tr-score tf-score ta-score
					mp1-score mp2-score mp3-score ma1-score
					ma2-score ma3-score ep-score ea-score))))
    (cond ((equal? max-score s-score) "STAY")
	  ((equal? max-score tr-score) (begin (set! left-corner (get-location percepts 1 1))
					      (set! right-corner '())
					      "TURN-RIGHT"))
	  ((equal? max-score tf-score) (begin (set! left-corner '())
					      (set! right-corner (get-location percepts 1 1))
					      "TURN-LEFT"))
	  ((equal? max-score ta-score) (let ((temp-left left-corner))
					 (begin (set! left-corner right-corner)
						(set! right-corner temp-left)
						"TURN-AROUND")))
	  ((equal? max-score mp1-score) (begin (set! left-corner (get-location percepts -1 1))
					       (set! right-corner (get-location percepts 1 1))
					       "MOVE-PASSIVE-1"))
	  ((equal? max-score mp2-score) (begin (set! left-corner (get-location percepts -1 2))
					       (set! right-corner (get-location percepts 1 2))
					       "MOVE-PASSIVE-2"))
	  ((equal? max-score mp3-score) (begin (set! left-corner (get-location percepts -1 3))
					       (set! right-corner (get-location percepts 1 3))
					       "MOVE-PASSIVE-3"))
	  ((equal? max-score ma1-score) (begin (set! left-corner (get-location percepts -1 1))
					       (set! right-corner (get-location percepts 1 1))
					       "MOVE-AGGRESSIVE-1"))
	  ((equal? max-score ma2-score) (begin (set! left-corner (get-location percepts -1 2))
					       (set! right-corner (get-location percepts 1 2))
					       "MOVE-AGGRESSIVE-2"))
	  ((equal? max-score ma3-score) (begin (set! left-corner (get-location percepts -1 3))
					       (set! right-corner (get-location percepts 1 3))
					       "MOVE-AGGRESSIVE-3"))
	  ((equal? max-score ep-score) "EAT-PASSIVE")
	  ((equal? max-score ea-score) "EAT-AGGRESSIVE")
	  (#f "STAY"))))
