




const image_list = document.getElementsByClassName("images")
console.log(image_list[0])


for(const image in image_list) {
    image_list[0].addEventListener("click", () => {
        console.log("eventLister")
    })

}
image_list[0].style.objectFit=cover;
image_list[1].style.objectFit=cover;