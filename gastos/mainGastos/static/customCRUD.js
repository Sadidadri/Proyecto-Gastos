$(function() {

    //Add edit and delete titles to the table
    let $trhead = $(".table>thead>tr");
    $trhead.append("<th>Edit</th>")
    $trhead.append("<th>Delete</th>")

    let $trbody = $(".table>tbody>tr")

    let URL = $(location).attr("href");

    //This function is dedicated for clean the URL if the user uses the filters of the table
    let re = /[?]\w*/
    if (re.exec(URL)){
        let pos = URL.lastIndexOf("?");
        URL = URL.substring(0,pos);
    }

    $trbody.each(function(index){
        //Obtain id and add button edit
        let id = $(this).children().first().text()
        $(this).append("<td><a href="+URL+"/edit/"+id+" class='btn btn-primary'>Edit</a></td>")
        //add button delete
        $(this).append("<td><a href="+URL+"/delete/"+id+" class='btn btn-danger'>Delete</a></td>")

    });
 

    //Add styles to buttons and pagination
    $('.btn-default').removeClass('.btn-default').addClass('btn-primary');
    $('.pagination li.active').addClass('btn-primary');

    
});

