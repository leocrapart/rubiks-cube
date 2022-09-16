

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
		let copyBack = JSON.parse(JSON.stringify(this.back))



		// bottom goes to back
		this.back[0][2] = this.bottom[0][2]
		this.back[1][2] = this.bottom[1][2]
		this.back[2][2] = this.bottom[2][2]

		// front goes to bottom
		this.bottom[0][2] = this.front[0][2]
		this.bottom[1][2] = this.front[1][2]
		this.bottom[2][2] = this.front[2][2] 

		// top goes to front
		this.front[0][2] = this.top[0][2]
		this.front[1][2] = this.top[1][2]
		this.front[2][2] = this.top[2][2]

		// back goes to top
		this.top[0][2] = copyBack[0][2]
		this.top[1][2] = copyBack[1][2]
		this.top[2][2] = copyBack[2][2]


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

console.log(cube)
cube.R()
cube.R1()
cube.R1()

console.log(cube)

