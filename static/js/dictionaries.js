

function activDict(index) {
    var list = document.getElementById('words-list-' + index);
    var table = document.getElementById('table-container-' + index); // Исправлено здесь

    if (list.style.display === "none" || list.style.display === "") {
        list.style.display = "block";
        table.style.height = "400px";
    } else {
        list.style.display = "none";
        table.style.height = ""; // Сброс высоты при скрытии
    }
}
