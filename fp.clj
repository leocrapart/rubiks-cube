(ns main)

; let cube = new Cube(
; 	{left: [[4,4,4],[4,4,4],[4,4,4]],
; 	 right: [[2,2,2],[2,2,2],[2,2,2]],
; 	 bottom: [[6,6,6],[6,6,6],[6,6,6]],
; 	 top:  [[5,5,5],[5,5,5],[5,5,5]],
; 	 front: [[1,1,1],[1,1,1],[1,1,1]],
; 	 back: [[3,3,3],[3,3,3],[3,3,3]]
; 	})

; colors
; red 1
; green 2
; orange 3
; blue 4
; yellow 5
; white 6

(defn up [item]
	[0 0 0])

(assoc [[4 4 4] [4 4 4] [4 4 4]] 0 [1 1 1])

(({:a "a"
  :b "b"
  :c ["cc" "ca" "cb"]} :c) 0)

(get-in 
 {:a "a"
  :b "b"
  :c ["cc" "ca" "cb"]} [:c 0])

([[4 4 4] [4 4 4] [4 4 4]] 0)


(defn anti-clockwise-rotated [face]
		(-> face
			(assoc-in [0 0] (get-in face [0 2]))
			(assoc-in [0 1] (get-in face [1 2]))
			(assoc-in [0 2] (get-in face [2 2]))

			(assoc-in [0 2] (get-in face [2 2]))
			(assoc-in [1 2] (get-in face [2 1]))
			(assoc-in [2 2] (get-in face [2 0]))

			(assoc-in [2 2] (get-in face [2 0]))
			(assoc-in [2 1] (get-in face [1 0]))
			(assoc-in [2 0] (get-in face [0 0]))

			(assoc-in [2 0] (get-in face [0 0]))
			(assoc-in [1 0] (get-in face [0 1]))
			(assoc-in [0 0] (get-in face [0 2]))
	    ))

(defn clockwise-rotated [face]
	(-> face
		anti-clockwise-rotated
		anti-clockwise-rotated
		anti-clockwise-rotated))

(defn R [cube]
	(-> cube
		(assoc-in [:front 0 2] (get-in cube [:bottom 0 2]))
	    (assoc-in [:front 1 2] (get-in cube [:bottom 1 2]))
	    (assoc-in [:front 2 2] (get-in cube [:bottom 2 2]))

	    (assoc-in [:top 0 2] (get-in cube [:front 0 2]))
	    (assoc-in [:top 1 2] (get-in cube [:front 1 2]))
	    (assoc-in [:top 2 2] (get-in cube [:front 2 2]))

	    (assoc-in [:back 0 2] (get-in cube [:top 0 2]))
	    (assoc-in [:back 1 2] (get-in cube [:top 1 2]))
	    (assoc-in [:back 2 2] (get-in cube [:top 2 2]))

	    (assoc-in [:bottom 0 2] (get-in cube [:back 0 2]))
	    (assoc-in [:bottom 1 2] (get-in cube [:back 1 2]))
	    (assoc-in [:bottom 2 2] (get-in cube [:back 2 2]))

			(assoc :right (clockwise-rotated (cube :right)))
	    ))

(defn R1 [cube]
	(R (R (R cube))))


(defn L [cube]
	(-> cube
     	(assoc-in [:front 0 0] (get-in cube [:top 0 0]))
	    (assoc-in [:front 1 0] (get-in cube [:top 1 0]))
	    (assoc-in [:front 2 0] (get-in cube [:top 2 0]))

	    (assoc-in [:top 0 0] (get-in cube [:back 0 0]))
	    (assoc-in [:top 1 0] (get-in cube [:back 1 0]))
	    (assoc-in [:top 2 0] (get-in cube [:back 2 0]))

	    (assoc-in [:back 0 0] (get-in cube [:bottom 0 0]))
	    (assoc-in [:back 1 0] (get-in cube [:bottom 1 0]))
	    (assoc-in [:back 2 0] (get-in cube [:bottom 2 0]))
	
	    (assoc-in [:bottom 0 0] (get-in cube [:front 0 0]))
	    (assoc-in [:bottom 1 0] (get-in cube [:front 1 0]))
	    (assoc-in [:bottom 2 0] (get-in cube [:front 2 0]))

			(assoc :left (clockwise-rotated (cube :left)))
	    ))

(defn L1 [cube]
	(L (L (L cube))))


(defn U [cube]
	(-> cube
		(assoc-in [:front 0 0] (get-in cube [:right 0 0]))
		(assoc-in [:front 0 1] (get-in cube [:right 0 1]))
		(assoc-in [:front 0 2] (get-in cube [:right 0 2]))

		(assoc-in [:left 0 0] (get-in cube [:front 0 0]))
		(assoc-in [:left 0 1] (get-in cube [:front 0 1]))
		(assoc-in [:left 0 2] (get-in cube [:front 0 2]))

		(assoc-in [:back 0 0] (get-in cube [:left 0 0]))
		(assoc-in [:back 0 1] (get-in cube [:left 0 1]))
		(assoc-in [:back 0 2] (get-in cube [:left 0 2]))

		(assoc-in [:right 0 0] (get-in cube [:back 0 0]))
		(assoc-in [:right 0 1] (get-in cube [:back 0 1]))
		(assoc-in [:right 0 2] (get-in cube [:back 0 2]))

		(assoc :top (clockwise-rotated (cube :top)))
		))


(defn U1 [cube]
	(U (U (U cube))))
		

(defn F1 [cube]
	(-> cube
		(assoc-in [:right 0 0] (get-in cube [:bottom 0 0]))
		(assoc-in [:right 1 0] (get-in cube [:bottom 0 1]))
		(assoc-in [:right 2 0] (get-in cube [:bottom 0 2]))

		(assoc-in [:bottom 0 0] (get-in cube [:left 0 2]))
		(assoc-in [:bottom 0 1] (get-in cube [:left 1 2]))
		(assoc-in [:bottom 0 2] (get-in cube [:left 2 2]))

		(assoc-in [:left 0 2] (get-in cube [:top 2 2]))
		(assoc-in [:left 1 2] (get-in cube [:top 2 1]))
		(assoc-in [:left 2 2] (get-in cube [:top 2 0]))

		(assoc-in [:top 2 2] (get-in cube [:right 2 0]))
		(assoc-in [:top 2 1] (get-in cube [:right 1 0]))
		(assoc-in [:top 2 0] (get-in cube [:right 0 0]))

		(assoc :front (anti-clockwise-rotated (cube :front)))
		))

(defn F [cube]
	(F1 (F1 (F1 cube))))


(defn M [cube]
	(-> cube
		(assoc-in [:front 0 1] (get-in cube [:top 0 1]))
		(assoc-in [:front 1 1] (get-in cube [:top 1 1]))
		(assoc-in [:front 2 1] (get-in cube [:top 2 1]))

		(assoc-in [:top 0 1] (get-in cube [:back 0 1]))
		(assoc-in [:top 1 1] (get-in cube [:back 1 1]))
		(assoc-in [:top 2 1] (get-in cube [:back 2 1]))

		(assoc-in [:back 0 1] (get-in cube [:bottom 0 1]))
		(assoc-in [:back 1 1] (get-in cube [:bottom 1 1]))
		(assoc-in [:back 2 1] (get-in cube [:bottom 2 1]))

		(assoc-in [:bottom 0 1] (get-in cube [:front 0 1]))
		(assoc-in [:bottom 1 1] (get-in cube [:front 1 1]))
		(assoc-in [:bottom 2 1] (get-in cube [:front 2 1]))
		))



(defn M1 [cube]
	(M (M (M cube))))


(def cube
{:left   [[4 4 4] [4 4 4] [4 4 4]]
 :right  [[2 2 2] [2 2 2] [2 2 2]]
 :bottom [[6 6 6] [6 6 6] [6 6 6]]
 :top    [[5 5 5] [5 5 5] [5 5 5]]
 :front  [[1 1 1] [1 1 1] [1 1 1]]
 :back   [[3 3 3] [3 3 3] [3 3 3]]
})

(R cube)
((R cube) :front)
((R (R cube)) :front)
((R1 cube) :front)

(L cube)
((L cube) :front)
((L (L cube)) :front)
((L1 cube) :front)

(U cube)
((U cube) :front)
((U (U cube)) :front)
((U1 cube) :front)

(F cube)
((F cube) :front)
((F (F cube)) :front)
((F1 cube) :front)

((F cube) :top)
((F (F cube)) :top)

(M cube)
((M cube) :front)
((M (M cube)) :front)
((M1 cube) :front)

; front face get multicolor 1 2 3 4 5 6 7 8 9
(def cube
{:left   [[4 4 4] [4 4 4] [4 4 4]]
 :right  [[2 2 2] [2 2 2] [2 2 2]]
 :bottom [[6 6 6] [6 6 6] [6 6 6]]
 :top    [[5 5 5] [5 5 5] [5 5 5]]
 :front  [[1 2 3] [4 5 6] [7 8 9]]
 :back   [[3 3 3] [3 3 3] [3 3 3]]
})

((F1 cube) :front)
; should be [[3 6 9] [2 5 8] [1 4 7]]
(assert
	(= ((F1 cube) :front) [[3 6 9] [2 5 8] [1 4 7]]))

cube


; maybe a transducer version

; clojure sublimed upgrades
; tree result unfolding like atom (or slightly better)
; multiexpressions sync evaluation show all results (currently everything sync evaled, but only last printed)