const elem = document.querySelectorAll('.cards')
let star
console.log(elem[0])

// setInterval(function () {
//     if (document.body.children.length < 6) {
//         document.body.appendChild(document.querySelector('.container').cloneNode(true))
//     }
// }, 100)

star = document.querySelectorAll('.last')

setInterval(() => {
  for (let i = 0; i < star.length; i++) {
    star[i].children[0].children[0].classList.toggle('sign')
  }
}, 500)

const next = document.querySelector('.next')
let target = 0

showCard(target)

next.addEventListener('click', function () {
  target++
  showCard(target)
})
function showCard(a) {
  if (a > 4) {
    a = 0
    target = 0
  }
  for (let i = 0; i < elem.length; i++) {
    elem[i].style.display = 'none'
  }
  elem[a].style.display = 'block'
}


