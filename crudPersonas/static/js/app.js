(function (){
    const btnDelete = document.querySelectorAll(".btnDelete")
    btnDelete.forEach(btn =>{
        btn.addEventListener("click",(e) =>{
            const confirma = confirm("Are you sure you want to delete?")
            if(!confirma){
                e.preventDefault()
            }
        })
    })
})()