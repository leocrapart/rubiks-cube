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

(defn R [cube]
	(let [cube1 (assoc-in cube [:front 0 2] (get-in cube [:bottom 0 2]))
		  cube2 (assoc-in cube1 [:front 1 2] (get-in cube [:bottom 1 2]))
		  cube3 (assoc-in cube2 [:front 2 2] (get-in cube [:bottom 2 2]))

		  cube4 (assoc-in cube3 [:top 0 2] (get-in cube [:front 0 2]))
		  cube5 (assoc-in cube4 [:top 1 2] (get-in cube [:front 1 2]))
		  cube6 (assoc-in cube5 [:top 2 2] (get-in cube [:front 2 2]))

  		  cube7 (assoc-in cube6 [:back 0 2] (get-in cube [:top 0 2]))
		  cube8 (assoc-in cube7 [:back 1 2] (get-in cube [:top 1 2]))
		  cube9 (assoc-in cube8 [:back 2 2] (get-in cube [:top 2 2]))

		  cube10 (assoc-in cube9 [:bottom 0 2] (get-in cube [:back 0 2]))
		  cube11 (assoc-in cube10 [:bottom 1 2] (get-in cube [:back 1 2]))
		  cube12 (assoc-in cube11 [:bottom 2 2] (get-in cube [:back 2 2]))
		 ]
		cube12))

(defn R1 [cube]
	(R (R (R cube))))


(defn L [cube]
	(let [cube1 (assoc-in cube [:front 0 0] (get-in cube [:top 0 0]))
		  cube2 (assoc-in cube1 [:front 1 0] (get-in cube [:top 1 0]))
		  cube3 (assoc-in cube2 [:front 2 0] (get-in cube [:top 2 0]))

		  cube4 (assoc-in cube3 [:top 0 0] (get-in cube [:back 0 0]))
		  cube5 (assoc-in cube4 [:top 1 0] (get-in cube [:back 1 0]))
		  cube6 (assoc-in cube5 [:top 2 0] (get-in cube [:back 2 0]))

  		  cube7 (assoc-in cube6 [:back 0 0] (get-in cube [:bottom 0 0]))
		  cube8 (assoc-in cube7 [:back 1 0] (get-in cube [:bottom 1 0]))
		  cube9 (assoc-in cube8 [:back 2 0] (get-in cube [:bottom 2 0]))
		
		  cube10 (assoc-in cube9 [:bottom 0 0] (get-in cube [:front 0 0]))
		  cube11 (assoc-in cube10 [:bottom 1 0] (get-in cube [:front 1 0]))
		  cube12 (assoc-in cube11 [:bottom 2 0] (get-in cube [:front 2 0]))
		 ]
		cube12))

(defn L1 [cube]
	(L (L (L cube))))

(defn U [cube]
	(let [cube1 (assoc-in cube [:front 0 0] (get-in cube [:right 0 0]))
		  cube2 (assoc-in cube1 [:front 0 1] (get-in cube [:right 0 1]))
		  cube3 (assoc-in cube2 [:front 0 2] (get-in cube [:right 0 2]))

		  cube4 (assoc-in cube3 [:left 0 0] (get-in cube [:front 0 0]))
		  cube5 (assoc-in cube4 [:left 0 1] (get-in cube [:front 0 1]))
		  cube6 (assoc-in cube5 [:left 0 2] (get-in cube [:front 0 2]))

		  cube7 (assoc-in cube6 [:back 0 0] (get-in cube [:left 0 0]))
		  cube8 (assoc-in cube7 [:back 0 1] (get-in cube [:left 0 1]))
		  cube9 (assoc-in cube8 [:back 0 2] (get-in cube [:left 0 2]))

		  cube10 (assoc-in cube9 [:right 0 0] (get-in cube [:back 0 0]))
		  cube11 (assoc-in cube10 [:right 0 1] (get-in cube [:back 0 1]))
		  cube12 (assoc-in cube11 [:right 0 2] (get-in cube [:back 0 2]))
		 ]
		cube12))

(defn U1 [cube]
	(U (U (U cube))))
		


(def cube
{:left [[4 4 4] [4 4 4] [4 4 4]]
 :right [[2 2 2] [2 2 2] [2 2 2]]
 :bottom [[6 6 6] [6 6 6] [6 6 6]]  
 :top [[5 5 5] [5 5 5] [5 5 5]] 
 :front [[1 1 1] [1 1 1] [1 1 1]]
 :back [[3 3 3] [3 3 3] [3 3 3]]
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


cube


; maybe a transducer version

; clojure sublimed upgrades
; tree result unfolding like atom (or slightly better)
; multiexpressions sync evaluation show all results (currently everything sync evaled, but only last printed)