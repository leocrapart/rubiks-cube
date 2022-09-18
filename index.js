// let model = { left: [
//         [4, 4, 4],
//         [4, 4, 4],
//         [4, 4, 4]
//     ], right: [
//         [2, 2, 2],
//         [2, 2, 2],
//         [2, 2, 2]
//     ], bottom: [
//         [6, 6, 6],
//         [6, 6, 6],
//         [6, 6, 6]
//     ], top: [
//         [5, 5, 5],
//         [5, 5, 5],
//         [5, 5, 5]
//     ], front: [
//         [5, 5, 5],
//         [5, 5, 5],
//         [5, 5, 5]
//     ], back: [
//         [3, 3, 3],
//         [3, 3, 3],
//         [3, 3, 3]
//     ] }

// read it from json
let model = JSON.parse(data)

function removeColorClasses(element) {
	element.classList.remove(red)
	element.classList.remove(blue)
	element.classList.remove(orange)
	element.classList.remove(green)
	element.classList.remove(white)
	element.classList.remove(yellow)
}

// params : 
// let sticker-x-spacing = 1
// let sticker-y-spacing = 1
// let stickerless = false
// let face-x-spacing = 4
// let face-y-spacing = 4
// let sticker-size = 10

let orange = "bg-orange-500"
let red = "bg-red-500"
let blue = "bg-blue-500"
let yellow = "bg-yellow-500"
let white = "bg-gray-200"
let green = "bg-green-500"

let numberToColor = {
	1: red,
	2: green,
	3: orange,
	4: blue,
	5: yellow,
	6: white
}

var back00 = document.getElementById("back00")
removeColorClasses(back00)
back00.classList.add(numberToColor[1])

function colorize(model) {
	colorizeBack(model)
	colorizeTop(model)
	colorizeFront(model)
	colorizeBottom(model)
	colorizeLeft(model)
	colorizeRight(model)
}

function colorizeBack(model) {
	var back00 = document.getElementById("back00")
	removeColorClasses(back00)
	back00.classList.add(numberToColor[model.back[0][0]])

	var back01 = document.getElementById("back01")
	removeColorClasses(back01)
	back01.classList.add(numberToColor[model.back[0][1]])

	var back02 = document.getElementById("back02")
	removeColorClasses(back02)
	back02.classList.add(numberToColor[model.back[0][2]])


	var back10 = document.getElementById("back10")
	removeColorClasses(back10)
	back10.classList.add(numberToColor[model.back[1][0]])

	var back11 = document.getElementById("back11")
	removeColorClasses(back11)
	back11.classList.add(numberToColor[model.back[1][1]])

	var back12 = document.getElementById("back12")
	removeColorClasses(back12)
	back12.classList.add(numberToColor[model.back[1][2]])


	var back20 = document.getElementById("back20")
	removeColorClasses(back20)
	back20.classList.add(numberToColor[model.back[2][0]])

	var back21 = document.getElementById("back21")
	removeColorClasses(back21)
	back21.classList.add(numberToColor[model.back[2][1]])

	var back22 = document.getElementById("back22")
	removeColorClasses(back22)
	back22.classList.add(numberToColor[model.back[2][2]])
}

function colorizeTop(model) {
	var top00 = document.getElementById("top00")
	removeColorClasses(top00)
	top00.classList.add(numberToColor[model.top[0][0]])

	var top01 = document.getElementById("top01")
	removeColorClasses(top01)
	top01.classList.add(numberToColor[model.top[0][1]])

	var top02 = document.getElementById("top02")
	removeColorClasses(top02)
	top02.classList.add(numberToColor[model.top[0][2]])


	var top10 = document.getElementById("top10")
	removeColorClasses(top10)
	top10.classList.add(numberToColor[model.top[1][0]])

	var top11 = document.getElementById("top11")
	removeColorClasses(top11)
	top11.classList.add(numberToColor[model.top[1][1]])

	var top12 = document.getElementById("top12")
	removeColorClasses(top12)
	top12.classList.add(numberToColor[model.top[1][2]])


	var top20 = document.getElementById("top20")
	removeColorClasses(top20)
	top20.classList.add(numberToColor[model.top[2][0]])

	var top21 = document.getElementById("top21")
	removeColorClasses(top21)
	top21.classList.add(numberToColor[model.top[2][1]])

	var top22 = document.getElementById("top22")
	removeColorClasses(top22)
	top22.classList.add(numberToColor[model.top[2][2]])
}

function colorizeFront(model) {
	var front00 = document.getElementById("front00")
	removeColorClasses(front00)
	front00.classList.add(numberToColor[model.front[0][0]])

	var front01 = document.getElementById("front01")
	removeColorClasses(front01)
	front01.classList.add(numberToColor[model.front[0][1]])

	var front02 = document.getElementById("front02")
	removeColorClasses(front02)
	front02.classList.add(numberToColor[model.front[0][2]])


	var front10 = document.getElementById("front10")
	removeColorClasses(front10)
	front10.classList.add(numberToColor[model.front[1][0]])

	var front11 = document.getElementById("front11")
	removeColorClasses(front11)
	front11.classList.add(numberToColor[model.front[1][1]])

	var front12 = document.getElementById("front12")
	removeColorClasses(front12)
	front12.classList.add(numberToColor[model.front[1][2]])


	var front20 = document.getElementById("front20")
	removeColorClasses(front20)
	front20.classList.add(numberToColor[model.front[2][0]])

	var front21 = document.getElementById("front21")
	removeColorClasses(front21)
	front21.classList.add(numberToColor[model.front[2][1]])

	var front22 = document.getElementById("front22")
	removeColorClasses(front22)
	front22.classList.add(numberToColor[model.front[2][2]])
}

function colorizeBottom(model) {
	var bottom00 = document.getElementById("bottom00")
	removeColorClasses(bottom00)
	bottom00.classList.add(numberToColor[model.bottom[0][0]])

	var bottom01 = document.getElementById("bottom01")
	removeColorClasses(bottom01)
	bottom01.classList.add(numberToColor[model.bottom[0][1]])

	var bottom02 = document.getElementById("bottom02")
	removeColorClasses(bottom02)
	bottom02.classList.add(numberToColor[model.bottom[0][2]])


	var bottom10 = document.getElementById("bottom10")
	removeColorClasses(bottom10)
	bottom10.classList.add(numberToColor[model.bottom[1][0]])

	var bottom11 = document.getElementById("bottom11")
	removeColorClasses(bottom11)
	bottom11.classList.add(numberToColor[model.bottom[1][1]])

	var bottom12 = document.getElementById("bottom12")
	removeColorClasses(bottom12)
	bottom12.classList.add(numberToColor[model.bottom[1][2]])


	var bottom20 = document.getElementById("bottom20")
	removeColorClasses(bottom20)
	bottom20.classList.add(numberToColor[model.bottom[2][0]])

	var bottom21 = document.getElementById("bottom21")
	removeColorClasses(bottom21)
	bottom21.classList.add(numberToColor[model.bottom[2][1]])

	var bottom22 = document.getElementById("bottom22")
	removeColorClasses(bottom22)
	bottom22.classList.add(numberToColor[model.bottom[2][2]])
}

function colorizeLeft(model) {
	var left00 = document.getElementById("left00")
	removeColorClasses(left00)
	left00.classList.add(numberToColor[model.left[0][0]])

	var left01 = document.getElementById("left01")
	removeColorClasses(left01)
	left01.classList.add(numberToColor[model.left[0][1]])

	var left02 = document.getElementById("left02")
	removeColorClasses(left02)
	left02.classList.add(numberToColor[model.left[0][2]])


	var left10 = document.getElementById("left10")
	removeColorClasses(left10)
	left10.classList.add(numberToColor[model.left[1][0]])

	var left11 = document.getElementById("left11")
	removeColorClasses(left11)
	left11.classList.add(numberToColor[model.left[1][1]])

	var left12 = document.getElementById("left12")
	removeColorClasses(left12)
	left12.classList.add(numberToColor[model.left[1][2]])


	var left20 = document.getElementById("left20")
	removeColorClasses(left20)
	left20.classList.add(numberToColor[model.left[2][0]])

	var left21 = document.getElementById("left21")
	removeColorClasses(left21)
	left21.classList.add(numberToColor[model.left[2][1]])

	var left22 = document.getElementById("left22")
	removeColorClasses(left22)
	left22.classList.add(numberToColor[model.left[2][2]])
}

function colorizeRight(model) {
	var right00 = document.getElementById("right00")
	removeColorClasses(right00)
	right00.classList.add(numberToColor[model.right[0][0]])

	var right01 = document.getElementById("right01")
	removeColorClasses(right01)
	right01.classList.add(numberToColor[model.right[0][1]])

	var right02 = document.getElementById("right02")
	removeColorClasses(right02)
	right02.classList.add(numberToColor[model.right[0][2]])


	var right10 = document.getElementById("right10")
	removeColorClasses(right10)
	right10.classList.add(numberToColor[model.right[1][0]])

	var right11 = document.getElementById("right11")
	removeColorClasses(right11)
	right11.classList.add(numberToColor[model.right[1][1]])

	var right12 = document.getElementById("right12")
	removeColorClasses(right12)
	right12.classList.add(numberToColor[model.right[1][2]])


	var right20 = document.getElementById("right20")
	removeColorClasses(right20)
	right20.classList.add(numberToColor[model.right[2][0]])

	var right21 = document.getElementById("right21")
	removeColorClasses(right21)
	right21.classList.add(numberToColor[model.right[2][1]])

	var right22 = document.getElementById("right22")
	removeColorClasses(right22)
	right22.classList.add(numberToColor[model.right[2][2]])
}

console.log(model)
colorize(model)