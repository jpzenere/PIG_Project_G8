const d = new Date();
const dias = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"];
const meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Augosto","Septiembre","Octubre","Noviembre","Deciembre"];

function fechaActual() {
    let dia = dias[d.getDay()];
    let mes = meses[d.getMonth()];
    let ano = d.getFullYear();
    let fecha = d.getDate();
    let hora = d.getHours();
    if (hora == "0" || hora == "1" || hora == "2" || hora == "3" || hora == "4" || hora == "5" ||hora == "6" || hora == "7" || hora == "8" || hora == "9"){
        var horas = "0" + hora
        } else { 
        horas = hora        
        }    
    let min = d.getMinutes();
    if (min == "0" || min == "1" || min == "2" || min == "3" || min == "4" || min == "5" || min == "6" || min == "7" || min == "8" || min == "9"){
        var mins = "0" + min
        } else { 
        mins = min         
        }  

    return dia+" "+fecha+" de "+mes+" de "+ano+" - "+horas+":"+mins
}
document.getElementById("fechaHora").innerHTML = fechaActual();
setInterval('fechaActual()',1000);
