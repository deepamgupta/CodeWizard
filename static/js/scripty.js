
$(document).ready(function () {
    console.log("loaded");

    if (typeof $.material !== 'undefined') {
        $.material.init();
    }


    //For Registeration
    $(document).on("submit", "#register-form", function (e) { //'e' means any event
        e.preventDefault();
        // console.log("form submitted");

        let form = $(this).serialize(); //get the form data

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




    //For Log In
    $(document).on("submit", "#login-form", function (e) {
        e.preventDefault();

        let form = $(this).serialize(); // this means #login-form

        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function (res) {
                if(res === "error"){
                    alert("Could not log in.");
                }else {
                    console.log("logged in as ", res);
                    window.location.href="/"; //This will redirect to the homepage after we have logged in
                }
            }
        })
    });


    //For Logout
    $(document).on("click", "#logout-link", function (e) {
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET', //If we use GET method, we do not have to send any data.
            success: function (res) {
                if(res === "success"){
                    window.location.href='/login';
                }
                else {
                    alert("Something went wrong!!")
                }
            }
        })
    })

    //For Posts
    $(document).on("submit", "#post-activity", function (e) {
        e.preventDefault();

        let form = $(this).serialize()

        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function (res) {
                console.log(res)
            }
        });
    });
});
