$("#logout").click(function(){
    localStorage.removeItem('token');
    window.location.href = "http://127.0.0.1:8000/";
});

$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/user/header_load/",
        type: 'GET',
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'Token '+localStorage.getItem('token'));},
        success: function (response) {
            // $('#username').html("<a href='#' class='text-white'>"+myArr[1]+"</a>");
            // $('#usernamefield').val(response);
            const myArr = response.split(",");
            $('#usernamefield1').html(myArr[0]+"&nbsp&nbsp&nbsp<img style='border-radius: 50%;width:30px;height:30px;'src='"+myArr[1] +"' alt='SDGDSA'>");
            //sessionStorage.setItem("token", response['token'])
        },
        error: function (jqXHR) {
            if (jqXHR.status == 404) { 
                
                $('#emailwarning').html(responseText['non_field_errors']);
            } else {
            }
        }
    }); 




});