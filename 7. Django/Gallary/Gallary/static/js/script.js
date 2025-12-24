const button = document.getElementById('btn')
const image = document.getElementById('image')

button.addEventListener("click", function(){
    if (image.style.display == "none"){
        image.style.display = "block";
    }
    else{
        image.style.display = 'none';
    }
})