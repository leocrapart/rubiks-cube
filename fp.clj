#_{:clj-kondo/ignore [:namespace-name-mismatch]}
(ns main
  (:require [clojure.data.json :as json]
            clojure.string))
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
      (assoc-in [0 0] (get-in face [0 2]))))

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

      (assoc :right (clockwise-rotated (cube :right)))))

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

      (assoc :left (clockwise-rotated (cube :left)))))

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

      (assoc :top (clockwise-rotated (cube :top)))))


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

      (assoc :front (anti-clockwise-rotated (cube :front)))))

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
      (assoc-in [:bottom 2 1] (get-in cube [:front 2 1]))))

(defn E [cube]
  cube)

(defn E1 [cube]
  cube)

(defn S [cube]
  cube)

(defn S1 [cube]
  cube)



(defn M1 [cube]
  (M (M (M cube))))

(defn X [cube]
  (R (M1 (L1 cube))))

(defn X1 [cube]
  (R1 (M (L cube))))

(defn Y [cube]
  (U (E1 (D1 cube))))

(defn Y1 [cube]
  (U1 (E (D cube))))

(defn Z [cube]
  (F (S (B1 cube))))

(defn Z1 [cube]
  (F1 (S1 (B cube))))


(def cube
  {:left   [[4 4 4] [4 4 4] [4 4 4]]
   :right  [[2 2 2] [2 2 2] [2 2 2]]
   :bottom [[6 6 6] [6 6 6] [6 6 6]]
   :top    [[5 5 5] [5 5 5] [5 5 5]]
   :front  [[1 1 1] [1 1 1] [1 1 1]]
   :back   [[3 3 3] [3 3 3] [3 3 3]]})

(println
 (json/write-str cube))


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
(def front-face-multicolor-cube
  {:left   [[4 4 4] [4 4 4] [4 4 4]]
   :right  [[2 2 2] [2 2 2] [2 2 2]]
   :bottom [[6 6 6] [6 6 6] [6 6 6]]
   :top    [[5 5 5] [5 5 5] [5 5 5]]
   :front  [[1 2 3] [4 5 6] [7 8 9]]
   :back   [[3 3 3] [3 3 3] [3 3 3]]})

((F1 front-face-multicolor-cube) :front)
; should be [[3 6 9] [2 5 8] [1 4 7]]
(assert
 (= ((F1 front-face-multicolor-cube) :front) [[3 6 9] [2 5 8] [1 4 7]]))


;;process parse-string                 v
;   "RRU'" ;; moves-str
;=> "RRU1"         ;; primes->ones     v
;=> "R R U1 "      ;; identify moves   v
;=> ["R" "R" "U1"] ;; vectorize        v
;=> for in call    ;; apply moves      v

(defn prime->one [char]
  (if (= char \')
    \1
    char))

;(prime->one \')

(defn primes->ones [moves-str]
  (clojure.string/join
   (map prime->one moves-str)))

;(primes->ones "RRU'")

(defn is-invert-move [char next-char]
  (if (= next-char \1)
    true
    false))

(defn is-normal-move [char next-char]
  (not (is-invert-move char next-char)))


(defn identify-move [moves-str idx char]
  (let [next-char (get moves-str (inc idx))]
    (if (is-normal-move char next-char)
      (str char " ")
      (str char))))

; (is-invert-move \R \R)
; (is-normal-move \R \R)
; (identify-move "RRU1" 0 \R)
; (identify-move "RRU1" 1 \R)
; (identify-move "RRU1" 2 \U)
; (identify-move "RRU1" 3 \1)
; (def identify-move-set (partial identify-move "RRU1"))
; (identify-move-set 0 \R)
; (identify-move-set 1 \R)
; (identify-move-set 2 \U)
; (identify-move-set 3 \1)

(defn identify-moves [moves-str]
  (let [identify-move-set (partial identify-move moves-str)]
    (clojure.string/join
     (map-indexed identify-move-set moves-str))))

; (identify-moves "RRU1")

(defn vectorize [spaced-moves-str]
  (clojure.string/split spaced-moves-str #" "))

; (vectorize "R R U1")

(defn remove-empties [moves]
  (vec
    (filter not-empty moves)))



(defn parse-moves-str [moves-str]
  (if (empty? moves-str)
    []
    (-> moves-str
        primes->ones
        identify-moves
        vectorize
        remove-empties)))

(parse-moves-str "RRU'")
(parse-moves-str "R1RU'")
(parse-moves-str "MM'M'R'U'")
(parse-moves-str "F R U' R' U' R U R' F' R U R' U' R' F R F'")
(parse-moves-str "")

(defn call [this & that]
  (apply (resolve (symbol this)) that))

(comment

  (empty? ["M"])

  (first (rest ["M" "M1" "M4"])))

(defn move-cube-vec [cube moves]
  (if (empty? moves)
    cube
    (let [move (first moves)
          new-cube (call move cube)]
      (move-cube-vec new-cube (rest moves)))))


(defn move-cube [cube moves-str]
  (move-cube-vec cube (parse-moves-str moves-str)))


(comment
  (move-cube cube "RRU")
  (move-cube cube ""))


;; orientate
; create x y z moves

;; blue-white

; locate blue white edge
;   <blue>-<white>
;   8x2 possibles positions left-bottom left-bottom
; best move for each case


(def blue-white-solve 
{:left-bottom ""
 :bottom-left "L1L1 U1 F1 L"
 :left-front "L"
  })

(defn solve-blue-white [cube]
  )

;;    formulas 

(defn t-perm [cube]
  (move-cube cube "R U R' U' R' F RR U' R' U' R U R' F'"))

(defn y-perm [cube]
  (move-cube cube "F R U' R' U' R U R' F' R U R' U' R' F R F'"))


(defn to-json [cube]
  (let [model-str (json/write-str cube)
        data-str (str "data = '" model-str "'")]
    (spit "model.json" data-str)))

(def cube
  {:left   [[4 4 4] [4 4 4] [4 4 4]]
   :right  [[2 2 2] [2 2 2] [2 2 2]]
   :bottom [[6 6 6] [6 6 6] [6 6 6]]
   :top    [[5 5 5] [5 5 5] [5 5 5]]
   :front  [[1 1 1] [1 1 1] [1 1 1]]
   :back   [[3 3 3] [3 3 3] [3 3 3]]})


cube
(t-perm cube)
(move-cube cube "R'UU")
(to-json (move-cube cube "R'UU"))




;; next
;; playable cube : reframe with moves button and see cube state changed
;; 3d cube
;; 3d playable cube
;; roux-solve


; turn display into a reframe app

; maybe a transducer version

; clojure sublimed upgrades
; tree result unfolding like atom (or slightly better)
; multiexpressions sync evaluation show all results (currently everything sync evaled, but only last printed)



;;;; find good coding env for clojurescript