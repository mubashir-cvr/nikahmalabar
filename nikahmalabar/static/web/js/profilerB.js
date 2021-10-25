

$(document).ready(function () {
    $("form[name='profilerB']").validate({ // initialize the plugin
        rules: {
            highestEducation: {
                required: true,                
            },
            profession: {
                required: true,
            },
            professionType: {
                required: true,
            },
            nativeCountry: {
                required: true,
            },
            nativeState: {
                required: true,
            },
            nativeCity: {
                required: true,
            },
            primaryNumber: {
                required: true,
            },
            secondaryNumber: {
                required: true,
            },
            preferedContact: {
                required: true,
            },
            relation: {
                required: true,
            },
            describe: {
                required: true,
            },
          
           
        },
        messages:{
            
            profession:"This field is required.",
            highestEducation:"This field is required.",
            professionType:"This field is required.",
            nativeCountry:"This field is required.",
            nativeState:"This field is required.",
            nativeCity:"This field is required.",
            primaryNumber:"This field is required.",
            secondaryNumber:"This field is required.",
            relation:"This field is required.",
            describe:"This field is required.",

        },
            
    
        submitHandler:function(){
            event.preventDefault();
            var csrf_token1 = $('[name="csrfmiddlewaretoken"]').val();
            var highestEducation = $('#highestEducation').val();
            var profession = $('#profession').val();
            var professionType = $('#professionType').val();
            var nativeCountry = $('#nativeCountry').val();
            var nativeState = $('#nativeState').val();
            var nativeCity = $('#nativeCity').val();
            var primaryNumber = $('#primaryNumber').val();
            var secondaryNumber = $('#secondaryNumber').val();
            var preferedContact = $('#preferedContact').val();
            var relation = $('#relation').val();
            var describe = $('#describe').val();
            data = {
                "highestEducation": highestEducation,
                "profession": profession,
                "professionType": professionType,
                "nativeCountry": nativeCountry,
                "nativeState": nativeState,
                "nativeCity": nativeCity,
                "primaryNumber": primaryNumber,
                "secondaryNumber": secondaryNumber,
                "preferedContact": preferedContact,
                "relation": relation,
                "describe": describe,
            }
            $.ajax({
                url: "http://127.0.0.1:8000/api/user/Bproperties/",
                type: 'POST',
                dataType: "JSON",
                data: data,
                            
                beforeSend: function(xhr){xhr.setRequestHeader('Authorization', 'Token '+localStorage.getItem('token'));},
                success: function (response) {
                    // var responseText = jQuery.parseJSON(response);   
                    //sessionStorage.setItem("token", response['token'])
                    window.location.href = "http://127.0.0.1:8000/imageupload/"
                },
                error: function (jqXHR) {
                    if (jqXHR.status == 400) { 
                        var responseText = jQuery.parseJSON(jqXHR.responseText);
                        $('#emailwarning').html(responseText['non_field_errors']);
                    } else {
                        $('#emailwarning').html("Unnexpected Error Occured ");
                    }
                }
            }); 
        }
    });

});





