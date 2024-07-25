
$(document).ready(function () {
    CargaFunciones();

});

function CargaFunciones() {

    if ($("title").text().trim() == "Inicio") {
        Modal();
    }

    if ($("title").text().trim() == "Envios") {

        const selectElement = document.querySelector("#envio");
        const result = document.querySelector("#costoDespacho");
    
        selectElement.addEventListener("change", (event) => {
            //result.textContent = `You like ${event.target.value}`;
            document.getElementById("costoDespacho").innerHTML = "";   
            CalculaEnvios();
            
        });        
    }
}

function Modal() {
    var fecha = new Date()
    var diaHoy = fecha.getDate()


    if (diaHoy == 24) {
        $('#exampleModal').modal('toggle');
    }
}


function CalculaEnvios() {

    if ($("#envio").val() == 'Conchalí') {

        var despacho = 3000 + 1000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');


    }
    if ($("#envio").val() == 'Huechuraba') {
        var despacho = 3000 + 2000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');

    }
    if ($("#envio").val() == 'Independencia') {
        var despacho = 3000 + 3000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');

    }
    if ($("#envio").val()== 'Recoleta') {
        var despacho = 3000 + 4000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');

    }
    if ($("#envio").val()== 'Quilicura') {

        var despacho = 3000 + 5000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');

    }
    if ($("#envio").val() == 'Renca') {
        var despacho = 3000 + 6000
        $("#costoDespacho").append('<div class="valorDespacho">Costo de envio: ' + despacho + '</div>');


    }


}

