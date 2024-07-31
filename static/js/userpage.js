

function activDictonaries(){
    window.location.href = '/dictionaries'
}

function checkTextAppended(){
    let textarea = document.getElementById('inputText')
    // Проверяем, добавился ли текст (предполагаем, что пустой текст не должен вызывать реакцию)
    if (textarea.value !== "") {
        textarea.style.border = "1px solid #66ff00"; // Или любой другой нужный вам стиль рамки
        textarea.style.boxShadow = "0px 0px 10px #66ff00"; 
    
        // Убираем стили через 1 секунду (1000 миллисекунд)
        setTimeout(function() {
          textarea.style.border = "";
          textarea.style.boxShadow = ""; 
        }, 330);
      }

}

function textError(){
    let textarea = document.getElementById('inputText')
    textarea.style.border = "1px solid #f50029"; // Или любой другой нужный вам стиль рамки
    textarea.style.boxShadow = "0px 0px 10px #f50029"; 
    
        // Убираем стили через 1 секунду (1000 миллисекунд)
    setTimeout(function() {
        textarea.style.border = "";
        textarea.style.boxShadow = ""; 
    }, 700);
}

async function sendData(value){

    try {
        const request = await fetch('/sendData', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'Value': value})
        });

        if (request.ok) {
            checkTextAppended()
            location.reload();
        } else {
            throw new Error(`Send error, ${request.statusText}`);
        }
    } catch (error) {
        
    }
}

function add_word(){
    let formInput = document.getElementById('FormInput')
    let textarea = formInput.getElementsByTagName('textarea')
    let values = []
    
    
    for(var i = 0; i < textarea.length; i++){
        if (textarea[i].value.length > 0){
            values.push(textarea[i].value)
        }
        else{
            break;
        }
    }
    if (values.length >= 1){
        sendData(values)
        console.log(values)
    }
    else{
        textError()
    }
}

