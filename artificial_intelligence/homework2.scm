;; ;;test map, just for testing
;; (define amap '((empty empty empty empty empty empty empty empty empty empty)
;; 	       (barrier empty barrier barrier empty empty barrier barrier barrier empty)
;; 	       (barrier empty barrier barrier empty barrier barrier empty empty empty)
;; 	       (barrier empty barrier barrier empty barrier barrier empty barrier empty)
;; 	       (barrier empty (goal 100) barrier empty barrier barrier (goal 1000) barrier empty)
;; 	       (barrier empty barrier barrier empty barrier barrier barrier barrier empty)
;; 	       (empty empty empty barrier empty empty empty empty empty empty)
;; 	       (empty barrier barrier barrier barrier barrier barrier empty barrier barrier)
;; 	       (empty barrier barrier barrier barrier barrier barrier empty empty empty)
;; 	       (empty empty empty empty (goal 20) barrier barrier barrier barrier empty)))

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

;;this function is a variant of above find-biggest, it takes in a nested list, returns the biggest first-element among all the lists in that nested list.
(define (find-biggest2 alist)
  (if (null? (cdr alist)) (car (car alist))
      (if (> (car (car alist)) (find-biggest2 (cdr alist)))
	  (car (car alist))
	  (find-biggest2 (cdr alist)))))

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

;;this function takes in an action, which are "TURN-LEFT" "TURN-RIGHT" "MOVE-1" "MOVE-2" "MOVE-3", as well as a state, returns a new state applied by the action.
(define (apply-action action state)
  (let ((x (nth-item 1 action)) (y (nth-item 2 action)) (dir (nth-item 3 action)))
    (cond ((equal? state "MOVE-1") (cond ((equal? dir (quote N)) (replace-nth-item 2 action (+ y 1)))
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

;;this function is implemented as getting the length of a list, which is useful in following programming.
(define (get-length lst)
  (if (null? lst) 0
      (+ 1 (get-length (cdr lst)))))

;; return a raw goal list, which recursively search the whole map, adding the found goal to the initial goal-list. This fucntion will be called in the get-goals API.
(define (generate-goals amap x y)
  (cond ((equal? amap '(()))
	 '())
	((null? (car amap))
	 (generate-goals (cdr amap) 0 (- y 1)))
	((or (equal? (car (car amap)) 'empty)
	     (equal? (car (car amap)) 'barrier))
	 (generate-goals (cons (cdr (car amap)) (cdr amap)) (+ x 1) y))
	(else (cons (list (car (cdr (car (car amap)))) x y)
		    (generate-goals (cons (cdr (car amap))
					  (cdr amap))
				    (+ x 1) y)))))

;;preprocess the goal list, adding a new field goal cost into goal-list. So that the formal representation of a goal list is [goal-cost, goal-val, x-coordinate, y-coordinate]
(define (preprocess-goals goal-lists max-goal)
  (if (null? goal-lists) '()
      (let ((curr-row (car goal-lists)))
	(cons (cons (- max-goal (nth-item 1 curr-row)) curr-row)
	      (preprocess-goals (cdr goal-lists) max-goal)))))

;;this is the outter get-goals API, it first calls generate-goals above, and scan for the maximum one, then calls preprocess-goals above to get standard representation of goal-lists.
(define (get-goals amap)
  (let* ((margin (- (get-length amap) 1))
	 (all-goals (generate-goals amap 0 margin))
	 (max-goal (find-biggest2 all-goals)))
    (preprocess-goals all-goals max-goal)))

;;get goal value API, which will be used when find a goal, query for the value of that goal.
(define (goal-val amap state)
  (let ((goal-lists (get-goals amap)))
    (goal-val-helper goal-lists state)))

;;this is the helper function for goal-val, which takes in a goal-lists and a state, return s the goal value of that goal.
(define (goal-val-helper goal-lists state)
  (cond ((null? goal-lists) #f)
	((and (= (nth-item 3 (car goal-lists)) (nth-item 1 state))
	      (= (nth-item 4 (car goal-lists)) (nth-item 2 state)))
	 (nth-item 2 (car goal-lists)))
	(else (goal-val-helper (cdr goal-lists) state))))

;;get goal cost API, which will be used when calculating the heuristic for the other goals.
(define (get-goal-cost amap state)
  (let ((goal-lists (get-goals amap)))
    (goal-cost-helper goal-lists state)))

;;this is the helper function for get-goal-cost, which takes in a goal list, and a state, returns the goal cost of that state.
(define (goal-cost-helper goal-lists state)
  (cond ((null? goal-lists) #f)
	((and (= (nth-item 3 (car goal-lists)) (nth-item 1 state))
	      (= (nth-item 4 (car goal-lists)) (nth-item 2 state)))
	 (nth-item 1 (car goal-lists)))
	(else (goal-cost-helper (cdr goal-lists) state))))

;;is-goal? API, takse in a map and a state, it calls get-goals first to accquire the goal list, then calls is-goal-helper to check wheter it is a goal?
(define (is-goal? amap state)
  (let* ((goal-lists (get-goals amap))
	 (x (nth-item 1 state))
	 (y (nth-item 2 state)))
    (is-goal-helper goal-lists x y)))

;;this function is the helper function for is-goal? which takes in a goal-list, x and y, and check whether (x, y) coordinates is in goal-lists or not.
(define (is-goal-helper goal-lists x y)
  (cond ((null? goal-lists) #f)
	((and (equal? (nth-item 3 (car goal-lists)) x)
	      (equal? (nth-item 4 (car goal-lists)) y))
	 #t)
	(else (is-goal-helper (cdr goal-lists) x y))))

;;this fucntion checks whether current (x, y) is empty or not?
(define (is-empty? x y amap)
  (let* ((length (get-length amap))
	 (row (nth-item (- length y) amap))
	 (col (nth-item (+ x 1) row)))
    (if (equal? col 'empty) #t
	#f)))

;;this fucntion checks whether current (x, y) is a barrier or not?
(define (is-barrier? x y amap)
  (let* ((length (get-length amap))
	 (row (nth-item (- length y) amap))
	 (col (nth-item (+ x 1) row)))
    (if (equal? col 'barrier) #t
	#f)))

;; ;;this is old-version of expand kids, this one cause the a* tree running extremely slow, because of it containing lots of redundant turnings, so I incorporate an optimized expand-kids function below
;; (define (expand-kids-helper curr-state amap)
;;   (let* ((curr-location (nth-item 2 curr-state))
;; 	 (path (nth-item 3 curr-state))
;; 	 (path-length (get-length path))
;; 	 (remainder (cdr (cdr curr-state))))
;;     (list (cons "TURN-LEFT" (cons (apply-action curr-location "TURN-LEFT") remainder))
;; 	  (cons "TURN-RIGHT" (cons (apply-action curr-location "TURN-RIGHT") remainder))
;; 	  (cons "MOVE-1" (cons (apply-action curr-location "MOVE-1") remainder))
;; 	  (cons "MOVE-2" (cons (apply-action curr-location "MOVE-2") remainder))
;; 	  (cons "MOVE-3" (cons (apply-action curr-location "MOVE-3") remainder)))))


;;this version of expand kids did some optimization, get rid of unnecessary turns and moves to be added as kids.
;;If parent is turn-left or turn-right, I discard all the turns for next step since it will either bring agent back to grandparent state or the opposite direction of parent.
;;If parent is move-1 or move2, I discard all the moves for next step based on the characteristic of our model, greedyly choose move-3.
(define (expand-kids-helper curr-state amap)
  (let* ((curr-location (nth-item 2 curr-state))
	 (path (nth-item 3 curr-state))
	 (path-length (get-length path))
	 (remainder (cdr (cdr curr-state)))
	 (all-possibility (list (cons "TURN-LEFT" (cons (apply-action curr-location "TURN-LEFT") remainder))
				(cons "TURN-RIGHT" (cons (apply-action curr-location "TURN-RIGHT") remainder))
				(cons "MOVE-1" (cons (apply-action curr-location "MOVE-1") remainder))
				(cons "MOVE-2" (cons (apply-action curr-location "MOVE-2") remainder))
				(cons "MOVE-3" (cons (apply-action curr-location "MOVE-3") remainder)))))
    (cond ((= path-length 0) all-possibility)
	  ((or (equal? (nth-item path-length path) "TURN-RIGHT")
	       (equal? (nth-item path-length path) "TURN-LEFT"))
	   (cdr (cdr all-possibility)))
	  ((equal? (nth-item path-length path) "MOVE-1") (get-sublist all-possibility 1 2))
	  ((equal? (nth-item path-length path) "MOVE-2") (get-sublist all-possibility 1 2))
	  (#t all-possibility))))

;;this fucntion takes in a kids list and a map, then returns a valid list of kids which are within the grid and not barriers. It also responsible for calculating the f value for the frontier, adding the action to the end the current path, adding the action cost to total path cost, constructing the state list.
(define (add-valid-kids all-kids amap)
  (if (null? all-kids) '()
      (let* ((first (car all-kids))
	     (step (nth-item 1 first))
	     (state (nth-item 2 first))
	     (path (nth-item 3 first))
	     (cost (nth-item 4 first))
	     (margin (- (get-length amap) 1))
	     (x (nth-item 1 state))
	     (y (nth-item 2 state))
	     (h-value (heuristic-function amap state)))
	(cond ((equal? step "TURN-LEFT") (cons (cons (+ h-value cost 5)
						     (list state (append path (list step)) (+ cost 5)))
					       (add-valid-kids (cdr all-kids) amap)))
	      ((equal? step "TURN-RIGHT") (cons (cons (+ h-value cost 5)
						      (list state (append path (list step)) (+ cost 5)))
						(add-valid-kids (cdr all-kids) amap)))
	      (else (if (and (<= 0 x margin)
			     (<= 0 y margin)
			     (not (is-barrier? x y amap)))
			(cond ((equal? step "MOVE-1") (cons (cons (+ h-value cost 10)
								  (list state (append path (list step)) (+ cost 10)))
							    (add-valid-kids (cdr all-kids) amap)))
			      ((equal? step "MOVE-2") (cons (cons (+ h-value cost 15)
								  (list state (append path (list step)) (+ cost 15)))
							    (add-valid-kids (cdr all-kids) amap)))
			      ((equal? step "MOVE-3") (cons (cons (+ h-value cost 18)
								  (list state (append path (list step)) (+ cost 18)))
							    (add-valid-kids (cdr all-kids) amap)))
			      (#t #t))
			'()))))))

;;this fucntion is the expand-kids API, which calls expand-kids helper first, adding all possible kids, then calls add-valid-kids to remove invalid kids such as barriers or out of boundary positions.
(define (expand-kids curr-state amap)
  (let ((all-kids (expand-kids-helper curr-state amap)))
    (add-valid-kids all-kids amap)))

;;this is the heuristic value for the distance dimension, here I relax the constraint that only considering the difference of x coordinates and the difference of y coordinates to the goal.
(define (distance-heuristic x1 y1 x2 y2)
  (let* ((x-diff (abs (- x1 x2)))
	 (y-diff (abs (- y1 y2)))
	 (x-by3 (quotient x-diff 3))
	 (x-by2 (quotient (modulo x-diff 3) 2))
	 (x-by1 (- x-diff (* x-by3 3) (* x-by2 2)))
	 (y-by3 (quotient y-diff 3))
	 (y-by2 (quotient (modulo y-diff 3) 2))
	 (y-by1 (- y-diff (* y-by3 3) (* y-by2 2))))
    (+ (* x-by3 18)
       (* x-by2 15)
       (* x-by1 10)
       (* y-by3 18)
       (* y-by2 15)
       (* y-by1 10))))

;;this is the heuristic value for direction dimension, which calculates at least how much it costs to turn to the same direction as goal.
(define (direction-heuristic x1 y1 dir x2 y2)
  (cond ((= x1 x2) (cond ((or (= y1 y2)
			      (and (< y1 y2) (equal? dir 'N))
			      (and (> y1 y2) (equal? dir 'S))) 0)
			 ((or (equal? dir 'E)
			      (equal? dir 'W)) 5)
			 (else 10)))
	((= y1 y2) (cond ((or (= x1 x2)
			      (and (< x1 x2) (equal? dir 'E))
			      (and (> x1 x2) (equal? dir 'W))) 0)
			 ((or (equal? dir 'S)
			      (equal? dir 'N)) 5)
			 (else 10)))
	(else (if (or (and (< x1 x2) (equal? dir 'E))
		      (and (> x1 x2) (equal? dir 'W))
		      (and (< y1 y2) (equal? dir 'N))
		      (and (> y1 y2) (equal? dir 'S)))
		  5
		  10))))

;;this is intermediate heuristic helper function, it returns the heuristic value of the input state based on the goal-lists.
(define (heuristic-helper amap goal-lists state)
  (let* ((x (nth-item 1 state))
	 (y (nth-item 2 state))
	 (dir (nth-item 3 state))
	 (goal-cost (nth-item 1 (car goal-lists)))
	 (goal-x (nth-item 3 (car goal-lists)))
	 (goal-y (nth-item 4 (car goal-lists)))
	 (curr-heuristic (if (is-goal? amap state) (get-goal-cost amap state)
			     (+ goal-cost (distance-heuristic x y goal-x goal-y) (direction-heuristic x y dir goal-x goal-y)))))
    (if (null? (cdr goal-lists)) curr-heuristic
	(if (<= curr-heuristic (heuristic-helper amap (cdr goal-lists) state))
	    curr-heuristic
	    (heuristic-helper amap (cdr goal-lists) state)))))

;;this is the outer heuristic function API, takes in a map and a state, it then calls heuristic-helper to do next.
(define (heuristic-function amap state)
  (let ((goal-lists (get-goals amap)))
    (heuristic-helper amap goal-lists state)))

;;this function takes in a state list and a frontier list, insert the state into the frontier, then sort the frontier by the f value.
(define (insert-into-frontier curr-state frontier)
  (let ((new-frontier (cons curr-state frontier)))
    (sort new-frontier (lambda (x y) (< (car x) (car y))))))

;;this function takes in a list of valid kids and the frontier, then insert each kid into frontier recursively.
(define (update-frontier kids frontier)
  (if (null? kids) frontier
      (let* ((curr-state (car kids))
	     (new-frontier (insert-into-frontier curr-state frontier)))
	(update-frontier (cdr kids) new-frontier))))

;;this function update the frontier in a dfs way, which adding kids to the front of the frontier
(define (dfs-update-frontier kids frontier)
  (append kids frontier))

;;this is the helper function of a*-tree-search, examing the frontier recursively
;;the commented region in the following code do the things of returning a list constructed by the steps and the score. But in order to make result more clear, I incorparate a new (print-result result) fucntion to display the result separately, feel free to switch the comment back if you only want a whole list with both steps and score.
(define (a*-helper amap energy frontier)
  (cond ((null? frontier) #f)
	(else (let* ((candidate (car frontier))
		     (f-val (nth-item 1 candidate))
		     (state (nth-item 2 candidate))
		     (path (nth-item 3 candidate))
		     (cost (nth-item 4 candidate)))
		(if (and (is-goal? amap state)
			 (>= energy cost))
		    (append path (list (- (+ energy (goal-val amap state)) cost)))
		    ;;(print-result (cons (- (+ energy (goal-val amap state)) cost) path))
		    (if (< energy cost)
			(a*-helper amap energy (cdr frontier))
			(let* ((kids (expand-kids candidate amap))
			       (new-frontier (update-frontier kids (cdr frontier))))
			  (a*-helper amap energy new-frontier))))))))

;;this function initilize the frontier, so that we can modify the initial state easily.
(define (initial-frontier amap state)
  (let ((initial-hvalue (heuristic-function amap state)))
    (cons (list initial-hvalue state '() 0) '())))

;;This is the a*-tree-search API, input is a map and an evergy level, it will then calls the helper function a*-helper
(define (a*-tree-search amap energy)
  (let ((frontier (initial-frontier amap '(0 0 N))))
    (a*-helper amap energy frontier)))  

;;This function can check whether the element is part of the list. Returns #t if yes, otherwise #f
(define (member? elem alist)
  (if (null? alist) #f
      (if (equal? elem (car alist)) #t
	  (member? elem (cdr alist)))))

;;this function is writtern for the a*-graph serach, which can track the close list, and avoidiing add visited states into frontier.
(define (update-frontier-without-dup kids frontier close-list)
  (if (null? kids) frontier
      (let* ((curr-state (car kids))
	     (state (nth-item 2 curr-state)))
	(if (member? state close-list)
	    (update-frontier-without-dup (cdr kids) frontier close-list)
	    (let ((new-frontier (insert-into-frontier curr-state frontier)))
	      (update-frontier-without-dup (cdr kids) new-frontier close-list))))))

;;this is a helper function for a*-graph search, which takes in a map, an energy level, a frontier list and also a close list. It then recursively examing the states in the frontier until it find a goal or the frontier is empty.
;;the commented region in the following code do the things of returning a list constructed by the steps and the score. But in order to make result more clear, I incorparate a new (print-result result) fucntion to display the result separately, feel free to switch the comment back if you only want a whole list with both steps and score.
(define (a*-graph-helper amap energy frontier close-list)
  (cond ((null? frontier) #f)
	(else (let* ((candidate (car frontier))
		     (state (nth-item 2 candidate))
		     (path (nth-item 3 candidate))
		     (cost (nth-item 4 candidate))
		     (new-close-list (cons state close-list)))
		(if (and (is-goal? amap state)
			 (>= energy cost))
		    (append path (list (- (+ energy (goal-val amap state)) cost)))
		    ;;(print-result (cons (- (+ energy (goal-val amap state)) cost) path))
		    (if (< energy cost)
			(a*-graph-helper amap energy (cdr frontier) new-close-list)
			(let* ((kids (expand-kids candidate amap))
			       (new-frontier (update-frontier-without-dup kids (cdr frontier) new-close-list)))
			  (a*-graph-helper amap energy new-frontier new-close-list))))))))

;;this is a*-graph-search API, which takes in a map and an energy level, it then calls a*-graph-helper to do the recursive things.
(define (a*-graph-search amap energy)
  (let ((frontier (initial-frontier amap '(0 0 N))))
    (a*-graph-helper amap energy frontier '())))

;;this is a variant dfs search, which incoporate two additional parameters (curr-limit, next-limit). At each call, it does the dfs search based on current limit, also updates next limit. This function will be called by (ida*-tree-helper) fucntion to realize ida* tree search.
(define (dfs-variant amap energy frontier curr-limit next-limit)
  (cond ((null? frontier) (list curr-limit next-limit))
	(else (let* ((candidate (car frontier))
		     (f-val (nth-item 1 candidate))
		     (state (nth-item 2 candidate))
		     (path (nth-item 3 candidate))
		     (cost (nth-item 4 candidate)))
		(cond ((< energy cost)
		       (dfs-variant amap energy (cdr frontier) curr-limit next-limit))
		      ((and (> f-val curr-limit)
			    (< f-val next-limit))
		       (dfs-variant amap energy (cdr frontier) curr-limit f-val))
		      ((<= f-val curr-limit)
		       (if (is-goal? amap state)
			   (append candidate (list (- (+ energy (goal-val amap state)) cost)))
			   (let* ((kids (expand-kids candidate amap))
				  (new-frontier (dfs-update-frontier kids (cdr frontier))))
			     (dfs-variant amap energy new-frontier curr-limit next-limit))))
		      (else (dfs-variant amap energy (cdr frontier) curr-limit next-limit)))))))

;;this if ida* helper function, which do the outter recursive loop for ida*. Continuously increase the current limit to the next limit of last loop and calls (dfs-variant) fucntion to explore nodes. If current limit == next limit, then it means we have explored all the nodes without finding a solution to the goal, just return #f. If the function returns a list of 5 items (which includes f-value, current state, path to the current state, path cost, metric score), then this is a optimal solution.
(define (ida*-tree-helper amap energy curr-limit next-limit)
  (let* ((frontier (initial-frontier amap '(0 0 N)))
	 (return-val (dfs-variant amap energy frontier curr-limit next-limit)))
    (if (= (get-length return-val) 5)
	(append (nth-item 3 return-val) (list (nth-item 5 return-val)))
	;;(print-result (cons (nth-item 5 return-val) (nth-item 3 return-val)))
	(cond ((< curr-limit next-limit)
	       (ida*-tree-helper amap energy (car (cdr return-val)) +inf.0))
	      (else #f)))))

;;this is ida*-tree-search API, takes in a amap and en energy level, prints out the list of steps as well as the performance metric score if there is a solution, otherwise return #f
(define (ida*-tree-search amap energy)
  (let ((frontier (initial-frontier amap '(0 0 N))))
    (ida*-tree-helper amap energy (car (car frontier)) +inf.0)))

;;this function prints out the search result for the search algorithm, input is a list combined with steps and metric score.
(define (print-result result)
  (begin (display "The steps to reach a goal is: ")
	 (display (cdr result))
	 (newline)
	 (display "The performance metric score is: ")
	 (display (car result))
	 (newline)))
