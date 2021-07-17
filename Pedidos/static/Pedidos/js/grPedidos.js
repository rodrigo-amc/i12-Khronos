//<!-- Script para agregar fila a la tabla de NUEVO (id="pedido")-->

/*Funciona, pero hay que mejorar el código ya que hay muchas variables que se repiten y funcionalidades
que deberían estar en funciones para reutilizar */

/**
 * En este array se guardan los valores de la tabla, que luego se pasan por ajax
 * al backend en la función "guardar" */
var lista = [];

//Funcionalidad para el boton "Nuevo Item"
$('#btnNuevoItem').click(function(){

    //Guardo el valor de la ultima fila (tr), el primer campo (input)
    var valNom = $('#tblPedido tr:last input:first').val();

    //Guardo el valor de la ultima fila (tr), el ultimo campo (input)
    var valCan = $('#tblPedido tr:last input:last').val();

    //Acá se valida que los campos estén completos antes de agregar una nueva fila
    if ( (valNom == '') ) {
        alert('Tipo De Cerveza Vacío');
        $('#tblPedido tr:last input:first').focus();
        
    }else{
        if( ((valNom != '') & (valCan == '')) ){
        alert('Cantidad Vacío');
        $('#tblPedido tr:last input:last').focus();
        
        /*Si ninguno de los campos está vacío, entonces agrega una nueva fila y
        le da el foco al primer campo de la nueva fila*/
        }else {
            $('#tblPedido tbody:last').append(
                '<tr>'+
                    '<td class="text-center">'+
                        '<a href="#" data-toggle="modal">'+
                            '<i class="material-icons text-danger btnBorrar" data-toggle="tooltip" title="Borrar">'+
                                '&#xE872;'+
                            '</i>'+
                        '</a>'+
                    '</td>'+
                    
                    '<td class="valores">'+
                        '<input type="text" id="prod" placeholder="Tipo De Cerveza">'+
                    '</td>'+

                    '<td class="valores">'+
                        '<input type="text" id="cant" placeholder="Cantidad">'+
                    '</td>'+
                '</tr>'
            );

            //$('#tabla tr:last input:first').css("background-color", "red");
            $('#tblPedido tr:last input:first').focus();
        }
    }

});

//Funcionalidad para Botón "guardar"
//$('#asd').click(function(){
function guardar(){
    //Guardo el valor de la ultima fila (tr), el primer campo (input)
    var valNom = $('#tblPedido tr:last input:first').val();

    //Guardo el valor de la ultima fila (tr), el ultimo campo (input)
    var valCan = $('#tblPedido tr:last input:last').val();

    //Guardo la cantidad de filas que tiene la tabla
    var tablaLength = $('#tblPedido tr').length;

    /*Inicialmente la tabla tiene dos filas. La de encabezados y una para completar
    La primera fila para completar no puede estar vacía para guardar el pedido.
    Para validarlo llamo a la función que valida que es la del botón "Nuevo Item"*/
    if(tablaLength < 3){
        $('#btnNuevoItem').click();
        
    }else{
        /*Si hay mas de dos filas y la última tiene los dos campos vacíos entonces permite guardar*/
        if( ((valNom == '') & (valCan == '')) | ((valNom !='')&(valCan!='')) ){
            //alert('CRT + G = Guardar');
            
            //Esta función caarga los valores de la tabla en el array "lista" 
            enviar();
            
        }else{
            //Sino vuelve a validar con la función del boton "Nuevo Item"
            $('#btnNuevoItem').click();
        }
    }
};


//Funcionalidad Para botón "Borrar"
$('tbody').on('click', '.btnBorrar', function(){

    //Guardo la cantidad de filas que tiene la tabla
    var tablaLength = $('#tblPedido tr').length;

    if (tablaLength <3) {
        // cambiar esto. parent parent parent parent parent**n
        $(this).parent().parent().parent().remove();
        $('#tblPedido tbody:last').append(
            '<tr>'+
                '<td class="text-center">'+
                    '<a href="#" data-toggle="modal">'+
                        '<i class="material-icons text-danger btnBorrar" data-toggle="tooltip" title="Borrar">'+
                            '&#xE872;'+
                        '</i>'+
                    '</a>'+
                '</td>'+
                
                '<td>'+
                    '<input type="text" placeholder="Tipo De Cerveza">'+
                '</td>'+

                '<td>'+
                    '<input type="text" placeholder="Cantidad">'+
                '</td>'+
            '</tr>'
        );
        //$('#tabla tr:last input:first').css("background-color", "red");
        $('#tblPedido tr:last input:first').focus();

    }else{
        $(this).parent().parent().parent().remove();
    }
    
});


//--------------------------- Atajos De Teclado ---------------------------

//Cuando se pulsa la tecla "Enter" se llama a la función del botón "Nuevo Item"
$(document).keypress(function(event){
    var keyCode = (event.keyCode ? event.keyCode : event.which);
    if(keyCode == '13'){
        $('#btnNuevoItem').click();
    }
});


//Cuando se pulsa "CRTL+G" llama al botón "guardar"
$(document).keydown(function(event) {
    if (event.ctrlKey && event.which === 71) {
        $('#btnGuardar').click();   
        event.preventDefault();
    }
});

/**
 * ******************************************************************************************
 *          GUARDO LOS VALORES DE LA TABLA EN UN ARRAY PARA PASARLOS AL BACKEND
 * ******************************************************************************************
 */

function enviar() {
    $('#tblPedido tbody tr').each(function() {
        var prod = $(this).find(".valores #prod").val();
        var cant = $(this).find('.valores #cant').val();

        lista.push(prod);
        lista.push(cant);
        
    });
    console.log(lista);
};