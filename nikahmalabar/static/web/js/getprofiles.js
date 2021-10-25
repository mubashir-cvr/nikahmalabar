
$(document).ready(function () {
    $.ajax({
        url: "http://127.0.0.1:8000/api/user/collectproperties/",
        type: 'GET',
        beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'Token '+localStorage.getItem('token'));},
        success: function (response) {
            // $('#username').html("<a href='#' class='text-white'>"+myArr[1]+"</a>");
            const obj = JSON.parse(JSON.stringify(response));
            for(let i = 0; i < obj.length; i++){
                $('#membersList').append("<div class='col-lg-4  col-md-6 col-sm-12 col-12 p-2 '>\
                <div class='pager-coll gext'><div class='row'>\
                <div class='col-lg-6 col-md-6 col-sm-12 pr-0'>\
                <img src='"+obj[i].image+"' alt=''>\
                <div class='d-flex mobi'><p class='sta'>\
                <i class='icofont-ui-text-chat'></i>\
                </p><p class='sta'><i class='icofont-star'></i>\
                </p></div></div><div class='col-lg-6 col-md-6 col-sm-12 pro-detail pr-0'>\
                <a href='#' class='like mobii'><i class='icofont-ui-love'></i>Like</a>\
                <h4>"+obj[i]['profile'].name+"</h4><p>Age  <span class='sp1 ml-4'>"+obj[i]['profile'].dateOfBirth+"</span> \
                </p> <p>Status  <span class='sp2'>"+obj[i]['profile'].martialStatus+"</span></p>\
                <p ><span><i class='icofont-users-alt-3 mr-2'></span></i>\
                "+obj[i]['profile'].relegion+"</p><p><span><i class='icofont-web mr-2'></span></i>\
                "+obj[i]['education'].highestEducation+"</p><p><span><i class='icofont-bag mr-2'></span></i>\
                "+obj[i]['education'].profession+"</p><p><span><i class='icofont-location-pin mr-2'></span></i>"+ obj[i]['education'].nativeCity+"</p>\
                </div></div><div class='d-none three justify-content-center'><p class='sta'>\
                <i class='icofont-ui-text-chat'></i></p><p class='sta'><i class='icofont-star'>\
                </i></p><p class='sta'><i class='icofont-heart'></i></p></div></div></div>");
                console.log("Id :"+obj[i].id);
                  console.log("Quantity :" + obj[i].image);
                  console.log("Name :" + obj[i]['profile'].dateOfBirth);
                  console.log("Education :" + obj[i]['education'].nativeCity);
                }
           
            // $('#usernamefield1').html(myArr[1]+"&nbsp&nbsp&nbsp<img style='border-radius: 50%;width:30px;height:30px;'src='"+myArr[0] +"' alt='SDGDSA'>");
            //sessionStorage.setItem("token", response['token'])
        },
        error: function (jqXHR) {
            if (jqXHR.status == 404) { 
                var responseText = jQuery.parseJSON(jqXHR.responseText);
            } else {
                alert("Hisd")
                $('#username').html("<a href='http://127.0.0.1:8000/signup/' class='get-started-btnn'>Sign Up</a>");
            }
        }
    }); 




});