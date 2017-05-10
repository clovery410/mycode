(define (add-one x)
  (+ x 1))

(define (minus-one x)
  (- x 1))

(define pi (* 4 (atan 1.0)))

(define (change-unit degree)
  (* degree (/ pi 180.0))

;; (define (dx vx t)
;;   (* vx t))

;; (define (ff-time vy)
;;   (/ (* vy 2.0) 9.8))

;; (define (distance v ang)
;;   (dx
;;    (* v (cos (change-unit ang)))
;;    (ff-time (* v (sin (change-unit ang))))))
