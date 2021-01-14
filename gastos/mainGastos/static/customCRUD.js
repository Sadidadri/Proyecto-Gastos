$(function() {

    //Añade la parte de editar y eliminar a la tabla
    let $trhead = $(".table>thead>tr");
    $trhead.append("<th>Editar</th>")
    $trhead.append("<th>Eliminar</th>")

    let $trbody = $(".table>tbody>tr")

    let URL = $(location).attr("href");

    //Limpiar URL
    let re = /[?]\w*/
    if (re.exec(URL)){
        let pos = URL.lastIndexOf("?");
        URL = URL.substring(0,pos);
    }

    $trbody.each(function(index){
        //Obtiene id y añade el boton de editar
        let id = $(this).children().first().text()
        $(this).append("<td><a href="+URL+"/edita/"+id+" class='btn btn-primary'>Editar</a></td>")
        //Añade el boton de eliminar
        $(this).append("<td><a href="+URL+"/elimina/"+id+" class='btn btn-danger'>Eliminar</a></td>")

    });
 

    //Añade estilos a los botones
    $('.btn-default').removeClass('.btn-default').addClass('btn-primary');
    $('.pagination li.active').addClass('btn-primary');

    //Elimina el id de cada elemento (no nos interesa mostrarlos)
    $('table>thead>tr>th').first().remove()
    
    let $filas = $('table>tbody>tr')
    for (let i = 0; i < $filas.length; i++) {
        $filas[i].removeChild($filas[i].getElementsByTagName('td')[0]);
    }
});

