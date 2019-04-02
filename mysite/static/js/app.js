// mechanism to change page display mode (day/night) day as the default
var sun = $(".fas.fa-sun");
var moon = $(".fas.fa-moon");
var head = $("head");
var dmode = $("<link rel='stylesheet' href='/static/css/dmode.css'>")
var nmode = $("<link rel='stylesheet' href='/static/css/nmode.css'>")

var links = $("link")
var proper_links = [];
links.each(function () {
    if ($(this).attr("rel") === "stylesheet") {
        proper_links.push($(this));
    }
});



var main_css = links.eq(-3);
var link = links.eq(-2)
var highlight = links.eq(-1);



console.log(link)
sun.on("click", function () {
    if (!$(this).hasClass("active")) {
        $(this).addClass("active");
        moon.removeClass("active");
        link.attr('href', '/static/css/dmode.css');
        highlight.attr("href", "//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/atom-one-light.min.css")

    }
})


moon.on("click", function () {
    if (!$(this).hasClass("active")) {
        $(this).addClass("active");
        sun.removeClass("active");
        link.attr('href', '/static/css/nmode.css')
        highlight.attr("href", "//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/atom-one-dark.min.css")
    }
})