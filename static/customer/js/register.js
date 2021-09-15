$(document).ready(function () {

    $("#signUpBtn").click(function (event) {
        console.log('Clicked')

        //Stop submit the form, we will post it manually.
        event.preventDefault();

        // Get form
        const form = $('#form-post')[0];

        // Create an FormData object
        const data = new FormData(form);


        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "/api-auth/customer/register/",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 600000,
            success: function () {
                console.log("SUCCESS :");
                alert('SUCCESS :')
            },
            error: function (e) {
                console.log("ERROR : ", e);
                alert("ERROR : ")
            }
        });

    });

});