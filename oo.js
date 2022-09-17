let _ = require("lodash")

class Cube {
	constructor(cube) {
		this.left = cube.left
		this.right = cube.right
		this.bottom = cube.bottom
		this.top = cube.top
		this.front = cube.front
		this.back = cube.back
	}

	R() {
		let copyFront = JSON.parse(JSON.stringify(this.front))

		// bottom goes to front
		this.front[0][2] = this.bottom[0][2]
		this.front[1][2] = this.bottom[1][2]
		this.front[2][2] = this.bottom[2][2]

		// back goes to bottom
		this.bottom[0][2] = this.back[0][2]
		this.bottom[1][2] = this.back[1][2]
		this.bottom[2][2] = this.back[2][2]

		// top goes to back
		this.back[0][2] = this.top[0][2]
		this.back[1][2] = this.top[1][2]
		this.back[2][2] = this.top[2][2]

		// front goes to top
		this.top[0][2] = copyFront[0][2]
		this.top[1][2] = copyFront[1][2]
		this.top[2][2] = copyFront[2][2]
	}

	R1() {
		this.R()
		this.R()
		this.R()
	}

	L() {
		let copyBottom = JSON.parse(JSON.stringify(this.bottom))

		this.bottom[0][0] = this.front[0][0]
		this.bottom[1][0] = this.front[1][0]
		this.bottom[2][0] = this.front[2][0]

		this.front[0][0] = this.top[0][0]
		this.front[1][0] = this.top[1][0]
		this.front[2][0] = this.top[2][0]

		this.top[0][0] = this.back[0][0]
		this.top[1][0] = this.back[1][0]
		this.top[2][0] = this.back[2][0]

		this.back[0][0] = copyBottom[0][0]
		this.back[1][0] = copyBottom[1][0]
		this.back[2][0] = copyBottom[2][0]
	}

	L1() {
		this.L()
		this.L()
		this.L()
	}

	M() {
		let copyFront = JSON.parse(JSON.stringify(this.front))

		this.front[0][1] = this.top[0][1]
		this.front[1][1] = this.top[1][1]
		this.front[2][1] = this.top[2][1]

		this.top[0][1] = this.back[0][1]
		this.top[1][1] = this.back[1][1]
		this.top[2][1] = this.back[2][1]

		this.back[0][1] = this.bottom[0][1]
		this.back[1][1] = this.bottom[1][1]
		this.back[2][1] = this.bottom[2][1]

		this.bottom[0][1] = copyFront[0][1]
		this.bottom[1][1] = copyFront[1][1]
		this.bottom[2][1] = copyFront[2][1]
	}

	M1() {
		this.M()
		this.M()
		this.M()
	}

	U() {
		let copyFront = JSON.parse(JSON.stringify(this.front))

		this.front[0][0] = this.right[0][0]
		this.front[0][1] = this.right[0][1]
		this.front[0][2] = this.right[0][2]

		this.right[0][0] = this.back[0][0]
		this.right[0][1] = this.back[0][1]
		this.right[0][2] = this.back[0][2]

		this.back[0][0] = this.left[0][0]
		this.back[0][1] = this.left[0][1]
		this.back[0][2] = this.left[0][2]

		this.left[0][0] = copyFront[0][0]
		this.left[0][1] = copyFront[0][1]
		this.left[0][2] = copyFront[0][2]
	}

	U1() {
		this.U()
		this.U()
		this.U()
	}

	F1() {
		let copyFront = JSON.parse(JSON.stringify(this.front))

		this.front[0][0] = copyFront[0][2]
		this.front[0][1] = copyFront[1][2]
		this.front[0][2] = copyFront[2][2]

		this.front[0][2] = copyFront[2][0]
		this.front[1][2] = copyFront[2][1]
		this.front[2][2] = copyFront[2][2]

		this.front[2][0] = copyFront[0][0]
		this.front[2][1] = copyFront[1][0]
		this.front[2][2] = copyFront[2][0]

		this.front[0][0] = copyFront[0][0]
		this.front[1][0] = copyFront[0][1]
		this.front[2][0] = copyFront[0][2]

	}

	F() {
		this.F1()
		this.F1()
		this.F1()
	}

	toJson() {
		return JSON.parse(JSON.stringify(this))
	}

}

// colors
// red 1
// green 2
// orange 3
// blue 4
// yellow 5
// white 6

let cube = new Cube(
	{left: [[4,4,4],[4,4,4],[4,4,4]],
	 right: [[2,2,2],[2,2,2],[2,2,2]],
	 bottom: [[6,6,6],[6,6,6],[6,6,6]],
	 top:  [[5,5,5],[5,5,5],[5,5,5]],
	 front: [[1,1,1],[1,1,1],[1,1,1]],
	 back: [[3,3,3],[3,3,3],[3,3,3]]
	})


// clearly needs some visual representation
// 2d patron

function displayCube(cube) {

}

// console.log(cube)
// testing isometrys
let initialCube = cube.toJson()
cube.F()
cube.F1()
cube.R()
cube.R1()
cube.U()
cube.U1()
cube.L()
cube.L1()
cube.M()
cube.M1()
console.assert(_.isEqual(cube.toJson(), initialCube),
  "isometry failed",
  "\n initialCube", initialCube,
  "\n cube", cube.toJson())


