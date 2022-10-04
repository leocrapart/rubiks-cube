(ns main
  (:require [clojure.data.json :as json]
            [clojure.algo.generic.functor :as functor]))
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

(defn red?    [number] (= number 1))
(defn green?  [number] (= number 2))
(defn orange? [number] (= number 3))
(defn blue?   [number] (= number 4))
(defn yellow? [number] (= number 5))
(defn white?  [number] (= number 6))

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

(defn M1 [cube]
  (M (M (M cube))))


(defn D [cube]
  (-> cube
    (assoc-in [:front 2 0] (get-in cube [:left 2 0]))
    (assoc-in [:front 2 1] (get-in cube [:left 2 1]))
    (assoc-in [:front 2 2] (get-in cube [:left 2 2]))

    (assoc-in [:right 2 0] (get-in cube [:front 2 0]))
    (assoc-in [:right 2 1] (get-in cube [:front 2 1]))
    (assoc-in [:right 2 2] (get-in cube [:front 2 2]))

    (assoc-in [:back 0 0] (get-in cube [:right 2 2]))
    (assoc-in [:back 0 1] (get-in cube [:right 2 1]))
    (assoc-in [:back 0 2] (get-in cube [:right 2 0]))

    (assoc-in [:left 2 0] (get-in cube [:back 0 2]))
    (assoc-in [:left 2 1] (get-in cube [:back 0 1]))
    (assoc-in [:left 2 2] (get-in cube [:back 0 0]))

    (assoc :bottom (clockwise-rotated (cube :bottom)))))


(defn D1 [cube]
  (D (D (D cube))))

(defn B [cube]
  (-> cube
    (assoc-in [:top 0 0] (get-in cube [:right 0 2]))
    (assoc-in [:top 0 1] (get-in cube [:right 1 2]))
    (assoc-in [:top 0 2] (get-in cube [:right 2 2]))

    (assoc-in [:left 0 0] (get-in cube [:top 0 2]))
    (assoc-in [:left 1 0] (get-in cube [:top 0 1]))
    (assoc-in [:left 2 0] (get-in cube [:top 0 0]))

    (assoc-in [:bottom 2 0] (get-in cube [:left 0 0]))
    (assoc-in [:bottom 2 1] (get-in cube [:left 1 0]))
    (assoc-in [:bottom 2 2] (get-in cube [:left 2 0]))

    (assoc-in [:right 0 2] (get-in cube [:bottom 2 2]))
    (assoc-in [:right 1 2] (get-in cube [:bottom 2 1]))
    (assoc-in [:right 2 2] (get-in cube [:bottom 2 0]))

    (assoc :back (clockwise-rotated (cube :back)))))

(defn B1 [cube]
  (B (B (B cube))))


(defn E [cube]
  (-> cube
    (assoc-in [:left 1 0] (get-in cube [:front 1 0]))
    (assoc-in [:left 1 1] (get-in cube [:front 1 1]))
    (assoc-in [:left 1 2] (get-in cube [:front 1 2]))

    (assoc-in [:front 1 0] (get-in cube [:right 1 0]))
    (assoc-in [:front 1 1] (get-in cube [:right 1 1]))
    (assoc-in [:front 1 2] (get-in cube [:right 1 2]))
    
    (assoc-in [:right 1 0] (get-in cube [:back 1 2]))
    (assoc-in [:right 1 1] (get-in cube [:back 1 1]))
    (assoc-in [:right 1 2] (get-in cube [:back 1 0]))

    (assoc-in [:back 1 0] (get-in cube [:left 1 2]))
    (assoc-in [:back 1 1] (get-in cube [:left 1 1]))
    (assoc-in [:back 1 2] (get-in cube [:left 1 0]))))

(defn E1 [cube]
  (E (E (E cube))))

(defn S [cube]
  (-> cube
    (assoc-in [:top 1 0] (get-in cube [:left 2 1]))
    (assoc-in [:top 1 1] (get-in cube [:left 1 1]))
    (assoc-in [:top 1 2] (get-in cube [:left 0 1]))

    (assoc-in [:right 0 1] (get-in cube [:top 1 0]))
    (assoc-in [:right 1 1] (get-in cube [:top 1 1]))
    (assoc-in [:right 2 1] (get-in cube [:top 1 2]))
    
    (assoc-in [:bottom 1 0] (get-in cube [:right 2 1]))
    (assoc-in [:bottom 1 1] (get-in cube [:right 1 1]))
    (assoc-in [:bottom 1 2] (get-in cube [:right 0 1]))

    (assoc-in [:left 0 1] (get-in cube [:bottom 1 0]))
    (assoc-in [:left 1 1] (get-in cube [:bottom 1 1]))
    (assoc-in [:left 2 1] (get-in cube [:bottom 1 2]))))

(defn S1 [cube]
  (S (S (S cube))))

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

(def XXZ-cube
  (move-cube cube "XXZ"))

; XXZ-cube

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


;;--------- orientate cube --------------------------------------------------------------------------
; place blue face at left, and yellow face at top

(def blue-face-to-left
  {:left ""
   :top "Z1"
   :right "ZZ"
   :bottom "Z"
   :front "Y"
   :back "Y1"    
    })

(def yellow-face-to-top
  {:top ""
   :front "X"
   :back "X1"
   :bottom "XX"   
    })

(defn center [face]
  (get-in face [1 1]))

; (center [[4 4 4] [4 6 4] [4 4 4]])

(defn centers-of-cube [cube]
  {:left   (center (cube :left))
   :right  (center (cube :right))
   :bottom (center (cube :bottom))
   :top    (center (cube :top))
   :front  (center (cube :front))
   :back   (center (cube :back))})

(def cube
  {:left   [[4 4 4] [4 4 4] [4 4 4]]
   :right  [[2 2 2] [2 2 2] [2 2 2]]
   :bottom [[6 6 6] [6 6 6] [6 6 6]]
   :top    [[5 5 5] [5 5 5] [5 5 5]]
   :front  [[1 1 1] [1 1 1] [1 1 1]]
   :back   [[3 3 3] [3 3 3] [3 3 3]]})

(def XXZ-cube
  (move-cube cube "XXZ"))

(defn locate-blue-face [cube]
  ((clojure.set/map-invert (centers-of-cube cube)) 4))

(defn locate-yellow-face [cube]
  ((clojure.set/map-invert (centers-of-cube cube)) 5))

(locate-blue-face cube)
(locate-yellow-face cube)
(locate-yellow-face (X cube))

(defn orientate-cube [cube]
  (let [blue-face-location (locate-blue-face cube)
        moves-blue (blue-face-to-left blue-face-location)
        blue-at-left-cube (move-cube cube moves-blue)

        yellow-face-location (locate-yellow-face blue-at-left-cube)
        moves-yellow (yellow-face-to-top yellow-face-location)
        orientated-cube (move-cube cube moves-yellow)
        ]
        ; [(str moves-blue moves-yellow) orientated-cube]
        orientated-cube))

; (orientate-cube XXZ-cube)

;;--------- end orientate cube --------------------------------------------------------------------



;;--------- solve blue-white edge -----------------------------------------------------------------

; locate blue white edge
;   <blue>-<white>
;   :LD = left down = solved
;   8x2 possibles positions left-bottom left-bottom
; best move for each case

;; locate blue-white edge

;; returns the edge-of the given edge.
;; given [:left 2 1], returns [:bottom 1 0]
(def edge-of 
{[:left 0 1] [:top 1 0]
 [:left 1 0] [:back 1 0]
 [:left 1 2] [:front 1 0]
 [:left 2 1] [:bottom 1 0]

 [:front 0 1] [:top 2 1]
 [:front 1 0] [:left 1 2]
 [:front 1 2] [:right 1 0]
 [:front 2 1] [:bottom 0 1]

 [:top 0 1] [:back 2 1]
 [:top 1 0] [:left 0 1]
 [:top 1 2] [:right 0 1]
 [:top 2 1] [:front 0 1]

 [:right 0 1] [:top 1 2]
 [:right 1 0] [:front 1 2]
 [:right 1 2] [:back 1 2]
 [:right 2 1] [:bottom 1 2]

 [:bottom 0 1] [:front 2 1]
 [:bottom 1 0] [:left 2 1]
 [:bottom 1 2] [:right 2 1]
 [:bottom 2 1] [:back 0 1]

 [:back 0 1] [:bottom 2 1]
 [:back 1 0] [:left 1 0]
 [:back 1 2] [:right 1 2]
 [:back 2 1] [:top 0 1]
  })

; (edge-of [:left 2 1])

(def edges (keys edge-of))
; edges

; given a sticker-pos [:left 2 1] = left face down edge
; returns the edge color : here [:bottom 1 0] may be white
(defn edge-color-of [cube sticker-pos]
  (get-in cube (edge-of sticker-pos)))

(def cube
  {:left   [[4 4 4] [4 4 4] [4 4 4]]
   :right  [[2 2 2] [2 2 2] [2 2 2]]
   :bottom [[6 6 6] [6 6 6] [6 6 6]]
   :top    [[5 5 5] [5 5 5] [5 5 5]]
   :front  [[1 1 1] [1 1 1] [1 1 1]]
   :back   [[3 3 3] [3 3 3] [3 3 3]]})

(edge-color-of cube [:left 0 1]) ;;5
(edge-color-of cube [:left 1 0]) ;;3
(edge-color-of cube [:left 1 2]) ;;1
(edge-color-of cube [:left 2 1]) ;;6

(map (partial edge-color-of cube) edges)

;; blue edges
(def)
(conj [:left 0 1] [4 6])

(defn color-of-sticker [cube sticker]
  (get-in cube sticker))

; (color-of-sticker cube [:left 0 1])

(defn edge-color-of-sticker [cube sticker]
  [(color-of-sticker cube sticker)
   (color-of-sticker cube (edge-of sticker))])

; (edge-color-of-sticker cube [:left 0 1])

(defn conj-edge-color [cube sticker]
  (conj sticker (edge-color-of-sticker cube sticker)))

; (conj-edge-color cube [:left 0 1])

(defn edges-with-edge-color [cube]
  (map (partial conj-edge-color cube) edges))

; (edges-with-edge-color cube)

(defn blue-white-edge? [edge-with-edge-color]
  (= (last edge-with-edge-color) [4 6]))

; (blue-white-edge? [:bottom 1 2 [4 6]])

(defn blue-white-edge-blue-sticker-pos [cube]
  (vec
    (drop-last
      (first
        (filter blue-white-edge?
          (edges-with-edge-color cube))))))

; (blue-white-edge-blue-sticker-pos cube)

(def face-to-letter-notation
{:left "L"
 :front "F"
 :right "R"
 :back "B"
 :top "U"
 :bottom "D"
 })

(defn edge-sticker-to-edge-notation [edge-sticker-1]
  (let [edge-sticker-2 (edge-of edge-sticker-1)
        face-1 (first edge-sticker-1)
        face-2 (first edge-sticker-2)
        face-1-letter (face-to-letter-notation face-1)
        face-2-letter (face-to-letter-notation face-2)]
    (keyword
      (str face-1-letter face-2-letter))
    ))

; (edge-sticker-to-edge-notation [:left 0 1])
; (edge-sticker-to-edge-notation [:back 2 1])


(defn locate-blue-white-edge [cube]
  (edge-sticker-to-edge-notation
    (blue-white-edge-blue-sticker-pos cube)))

; (locate-blue-white-edge cube)

(def blue-white-edge-solutions
{:LD ""
 :DL "L1F1D1"
 :LF "L"
 :FL "F1D1"
 :LU "LL"
 :UL "LF1D1"
 :LB "L1"
 :BL "LLF1D1"

 :FU "ULL"
 :UF "MD1"
 :FD "D1"
 :DF "MD"
 :BU "M1M1D1"
 :UB "BL1"
 :DB "M1D1"
 :BD "D"

 :FR "FD1"
 :RF "R1D1D1"
 :RD "D1D1"
 :DR "RFD1"
 :RB "RD1D1"
 :BR "B1D"
 :RU "U1U1LL"
 :UR "R1FD1"
  })

(defn blue-white-edge-solution [cube]
  (blue-white-edge-solutions (locate-blue-white-edge cube)))

; (blue-white-edge-solution cube)
; (blue-white-edge-solution (D cube))
; (blue-white-edge-solution (F cube))
; (blue-white-edge-solution (move-cube cube "LLUU"))


(defn solve-blue-white [cube]
  (move-cube cube (blue-white-edge-solution cube)))

; (solve-blue-white cube)
; (solve-blue-white (move-cube cube "LRMUFBBLDD"))


(defn blue-white-edge-positioned? [cube]
  (and (blue? (color-of-sticker cube [:left 2 1]))
       (white? (color-of-sticker cube [:bottom 1 0]))))

(blue-white-edge-positioned? cube)

; (blue-white-edge-positioned? 
;   (solve-blue-white cube))

; (blue-white-edge-positioned?
;  (solve-blue-white (move-cube cube "LRMUFBBLDD")))

;;--------- end solve blue-white edge -----------------------------------------------------------------

;;--------- solve blue-red-white pair  -----------------------------------------------------------------

;; locate blue-red edge
;; place blue-red edge on buffer

;; locate blue-red-white corner
;; place blue-red-white corner on top
;; de-orientate blue-red-white corner (not white on top)

;; pair blue-red edge with blue-red-white corner
;; create blue-red-white pair 

;; place blue-red-white pair 

;;--------- end solve blue-red-white pair  -----------------------------------------------------------------


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