var main_card = document.querySelector('.card-img-overlay')
var cards = document.querySelectorAll(".card-main")


// redirect to another page on click
main_card.addEventListener("click", function () {
    var link = this.children[0].children[1].href;
    window.location = link;
})

// redirect to another page on click imgae 
for (var i = 0; i < cards.length; i++) {
    cards[i].children[0].addEventListener("click", function () {
        var link = this.nextElementSibling.children[0].href;
        window.location = link

    })
}