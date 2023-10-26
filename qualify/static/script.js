
let timeboxes = document.querySelectorAll(".input-time")

timeboxes.forEach(function(box) {
  box.addEventListener("click", function() {
    document.querySelector(".time").style.display = "none"
    document.querySelector(".service").style.display = "flex"
    document.querySelector(".progress").value = "25"
    })
})

let serviceboxes = document.querySelectorAll('.input-service')

serviceboxes.forEach(function(service) {
  service.addEventListener('click', function() {
    document.querySelector('.service').style.display = 'none'
    document.querySelector('.attention').style.display = 'flex'
    document.querySelector(".progress").value = "50"
    document.querySelector(".field-atten").style.width = "50px"
  })
})

let attentionboxes = document.querySelectorAll('.input-attention')

attentionboxes.forEach(function(aten) {
  aten.addEventListener('click', function() {
    document.querySelector('.attention').style.display = 'none'
    document.querySelector('.recomment').style.display = 'flex'
    document.querySelector(".progress").value = "75"
    document.querySelector(".field-rec").style.width = "80px"
  })
})

let recommentboxes = document.querySelectorAll('.input-recomment')

recommentboxes.forEach(function(reco) {
  reco.addEventListener('click', function() {
    document.querySelector('.recomment').style.display = 'none'
    document.querySelector(".progress").value = "100"
    document.querySelector(".button").style.display = "block"
  })
})