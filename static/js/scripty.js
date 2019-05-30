
    $(document).ready(function () {
        console.log("loaded");

        if (typeof $.material !== 'undefined') {
            $.material.init();
        }

        $(document).on("submit", "#register-form", function (e) {
            e.preventDefault();
            console.log("form submitted");

            let form = $('#register-form').serialize(); //get the form data

            //send an ajax request over to the route /postregisteration
            $.ajax({
                url: '/postregistration',
                type: 'POST',
                data: form,
                success: function (response) {
                    console.log(response);
                }
            });
        });
    });
