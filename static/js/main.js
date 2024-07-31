


async function authorization(value){
    let user_login = value [0]
    let user_password = value[1]
    

    try {
        const request = await fetch('/authorization', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'Value': [user_login,user_password]})
        });

        if (request.ok) {
            
            window.location.href = '/userPage';
        } else {
            throw new Error(`Send error, ${request.statusText}`);
        }
    } catch (error) {
        console.error('Error', error);
        alert('Неверный логин или пароль')
    }
}

async function registration(value){
    let user_login = value [0]
    let user_password = value[1]

    try {
        const request = await fetch('/registration', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'Value': [user_login,user_password]})
        });

        if (request.ok) {
            alert('Регистрация успешна')
            
        } else {
            throw new Error(`Send error, ${request.statusText}`);
        }
    } catch (error) {
        alert('Имя пользователя занято!')
    }
}


function CheckPasswordMatch(arr){
    if (arr[1] == arr[2]){
        return true;
    }
    else{
        alert('Пароли не совпадают')
        return;
    }
}

function extractValues(FormId){
    var form = document.getElementById(FormId);
    var inputs = form.getElementsByTagName('input');
    var values = [];

    for (var i = 0; i < inputs.length; i++) {
        console.log(inputs[i].value)
        if (inputs[i].value.length >= 3){
            values.push(inputs[i].value);
        }
        else{
            alert('Ошибка!\nЗаполните все поля!')
            return
        }
    }
    
    console.log(values)
    if (values.length === 3 && CheckPasswordMatch(values)){
        registration(values,form.id)
    }
    if (values.length === 2 ){
        authorization(values)
    }
}

function ActivatingForm(A_FormID, B_FormID, A_btnId, B_btnId) {
    // Получаем элементы
    var ActivButton = document.getElementById(A_btnId);
    var BlockButton = document.getElementById(B_btnId);
    var ActivFormID = document.getElementById(A_FormID);
    var BlocFormID = document.getElementById(B_FormID);

    // Проверяем наличие всех элементов
    if (ActivFormID.style.display === 'flex') {
        extractValues(ActivFormID.id);
    }

    // Скрываем блокирующую форму
    if (BlocFormID.style.display === 'flex') {
        BlocFormID.style.display = 'none';
        BlockButton.style.backgroundColor = '#121214';
        BlockButton.style.color = 'white';
    }

    // Переключаем отображение активной формы
    if (ActivFormID.style.display === 'none' || ActivFormID.style.display === '') {
        ActivFormID.style.display = 'flex'; // Показываем активную форму
        ActivButton.style.backgroundColor = '#00ffff';
        ActivButton.style.color = 'black';
    } else {
        ActivFormID.style.display = 'none'; // Скрываем активную форму
        ActivButton.style.backgroundColor = ''; // Сбрасываем цвет кнопки
        ActivButton.style.color = ''; // Сбрасываем цвет текста кнопки
    }

}