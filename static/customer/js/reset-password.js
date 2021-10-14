$(document).ready(function () {
    // change customer info
    $("#change-password-form").submit(function (e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.

        let form = $(this)
        let url = form.attr('action');
                $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: url,
            data: form.serialize(),

            success: function (data) {
                console.log(data)
                alert('SUCCESS :')
                window.location.replace('http://127.0.0.1:8000/customer/login/')
            },
            error: function (e) {
                console.log("ERROR : ", e);
                alert("ERROR :  ")
            }

        });




});})