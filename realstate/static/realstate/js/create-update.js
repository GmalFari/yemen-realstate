const addMoreBtn = document.getElementById("add-more");
document.addEventListener('click',function(event){
    if (event.target.id=="add-more"){
        add_new_form(event)
    }
    
})
function add_new_form(event) {
    if(event){
        event.preventDefault();
    }
    const currentImagesForms = document.getElementsByClassName("images-form")
    const totalNewForms = document.getElementById("id_form-INITIAL_FORMS");
    const curImagesCount = currentImagesForms.length
    const formCopyTarget = document.getElementById("images-form-list");
    const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
    copyEmptyFormEl.setAttribute('class','images-form');
    copyEmptyFormEl.setAttribute('id',`form-${curImagesCount}`);
    const regex = new RegExp('__prefix__','g');
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex,curImagesCount)
    formCopyTarget.append(copyEmptyFormEl);



}