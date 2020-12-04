
var getText = document.getElementsByClassName('contend')


function cutText(text) {
    if (text.length > 85) {
        var newText = text.slice(1 , 140)
        return newText + ' ...'
    } else {
        return text
    }
}

for(var x=0; x<getText.length;x++) {
    var text = cutText(getText[x].textContent)
    getText[x].innerText = text
}







