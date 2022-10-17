const addMoreBtn = document.getElementById("add-more");
const totalNewForms = document.getElementById("id_form-INITIAL_FORMS");
const currentImagesForms = document.getElementsByClassName("images-form")
addMoreBtn.addEventListener('click',add_new_form);
function add_new_form(event) {
    if(event){
        event.preventDefault();
    }
    const curImagesCount = currentImagesForms.length
    const formCopyTarget = document.getElementById("images-form-list");
    const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
    copyEmptyFormEl.setAttribute('class','images-form');
    copyEmptyFormEl.setAttribute('id',`form-${curImagesCount}`);
    const regex = new RegExp('__prefix__','g');
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex,curImagesCount)
    formCopyTarget.append(copyEmptyFormEl);



}