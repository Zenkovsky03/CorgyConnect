console.log("dziala");


let dogsUrl = "http://127.0.0.1:8000/api/dogs/"
let getDogs = () =>{
    fetch(dogsUrl)
        .then(response => response.json())
        .then(data => {
            // console.log(data)
            displayDogs(data)
        })
}

let displayDogs = (dogsJson) =>{
    let dogsWrapper = document.getElementById('dogs-wrapper')
    for (let i = 0; i < dogsJson.length; i++){
        let dog = dogsJson[i];
        let dogCard = `
            <div>
                <p>${dog.name}</p>
            </div>
        `
        dogsWrapper.innerHTML += dogCard
    }

}

getDogs()