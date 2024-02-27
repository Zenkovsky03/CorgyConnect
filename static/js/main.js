let searchForm = document.getElementById('searchForm')
let pageLinks = document.getElementsByClassName('page-link')

if(searchForm){
    for(let i= 0; pageLinks.length > i; i++){
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            console.log('clicked')
            let page = this.dataset.page
            console.log(page)
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`
            searchForm.submit()
        })
    }
}
//to dziala tak ze preventDefault nie przeladowywuje strony i my przez klikniecie przekazujemy page czyli numer strony i wteyd na danej stronie dalej mamy search wynik ktory chcemy
//sztuczne przeladowanie storny