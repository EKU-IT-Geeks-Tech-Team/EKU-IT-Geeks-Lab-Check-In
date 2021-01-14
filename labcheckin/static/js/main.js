// automatically adjusts image map coordinates when window resizes
var callback = function () {
  // Handler when the DOM is fully loaded
  imageMapResize()
}

// calls callback() function when page is loaded
if (
  document.readyState === 'complete' ||
  (document.readyState !== 'loading' && !document.documentElement.doScroll)
) {
  callback()
} else {
  document.addEventListener('DOMContentLoaded', callback)
}

// add event listener to each image map area
document.querySelectorAll('area').forEach((area) => {
  if (area.dataset.status !== 'Open') {
    area.addEventListener('click', (e) => alert(area.title))
    // call a python function that sets status to "Open"
  }
})

let isCardInput = false
let card_input = ''

document.addEventListener('keydown', (e) => {
  if (isDigit(e.key)) {
    if (e.key === ';') {
      isCardInput = true
    }

    if (isCardInput) {
      card_input += e.key
    }

    if (e.key === '?') {
      isCardInput = false
      fetch(`/validate_card/${card_input}`)
        .then((response) => response.json())
        .then((data) => {
          /*const swipe_number = data.swipe_number
                    document.getElementById("test").innerHTML = swipe_number ? swipe_number : "Invalid Card"*/
          if (data.swipe_number) {
            console.log(current_swipe_numbers.indexOf(data.swipe_number) !== -1)
            populateModal(data.seatTypes)
            document
              .getElementById('swipe_number')
              .setAttribute('value', data.swipe_number)
            if (current_swipe_numbers.indexOf(data.swipe_number) === -1) {
              $('#exampleModal').modal('show')
            } else {
              document.getElementById('seatTypeSelectButton').click()
            }
          }
        })
      card_input = ''
    }
  }
})

function isDigit(str) {
  return str.length === 1 && str.match(/[\d;?=]/i)
}

function populateModal(seatTypes) {
  buttons = document.getElementById('buttons')

  removeAllChildNodes(buttons)

  console.log(seatTypes)

  seatTypes.forEach((seatType) => {
    const lbl = document.createElement('label')
    lbl.setAttribute('class', 'btn btn-info btn-lg btn-block')
    const btn = document.createElement('input')
    btn.setAttribute('type', 'radio')
    btn.setAttribute('name', 'options')
    btn.setAttribute('id', seatType)
    btn.setAttribute('data-label', seatType)
    btn.setAttribute('value', seatType)
    btn.setAttribute('autocomplete', 'off')
    const txt = document.createTextNode(seatType)
    lbl.appendChild(btn)
    lbl.appendChild(txt)
    buttons.appendChild(lbl)
  })
}

function removeAllChildNodes(parent) {
  while (parent.firstChild) {
    parent.removeChild(parent.firstChild)
  }
}
