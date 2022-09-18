let model = { left: [
        [4, 4, 4],
        [4, 4, 4],
        [4, 4, 4]
    ], right: [
        [2, 2, 2],
        [2, 2, 2],
        [2, 2, 2]
    ], bottom: [
        [6, 6, 6],
        [6, 6, 6],
        [6, 6, 6]
    ], top: [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5]
    ], front: [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], back: [
        [3, 3, 3],
        [3, 3, 3],
        [3, 3, 3]
    ] }

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

console.log(model)
colorize(model)