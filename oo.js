

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
		// 
	}

	R1() {

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

console.log(cube)
