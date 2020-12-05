
class AlertModal {

    constructor(element){
        this.element = element
        this.cancelable = false
        this.scream = document.getElementById('scream')
    }

    show(){

        //Deshabilita el scroll
        var x = window.scrollX;
        var y = window.scrollY;
        window.onscroll = function(){ window.scrollTo(x, y) };

        this.scream.addEventListener('click' , (e) => {
            if(this.cancelable) {
                console.log('close dialog')
                this.element.style.display = 'none'
                window.onscroll = null
            }
        })
        this.element.style.display = 'block'
    }

}

var buttonShow = document.getElementById('show-dialog')
var element = document.getElementById('dialog-container')
var dialog = new AlertModal(element)
dialog.cancelable = true

buttonShow.addEventListener('click' , (e) => {
    dialog.show()
})







