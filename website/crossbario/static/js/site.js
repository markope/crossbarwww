(function ($) {

    $(function () {
        $('.button-collapse').sideNav();
        $('.sticky').Stickyfill();
        console.log("document ready.");
    }); // end of document ready

    var logo_state = true;

    $(window).scroll(function () {
        var pos = $(document).scrollTop();

        if (pos > 50) {
            $("nav").removeClass("nav-scroll-top");
            $("nav").addClass("nav-scroll-nontop");

            $("#biglogo").removeClass("logo-on");
            $("#biglogo").addClass("logo-off");
        } else {
            $("nav").removeClass("nav-scroll-nontop");
            $("nav").addClass("nav-scroll-top");

            $("#biglogo").removeClass("logo-off");
            $("#biglogo").addClass("logo-on");
        }


/*
        logo_state = $("#biglogo").attr('class') == "logo-on";
        if (logo_state) {
            if (pos < 50) {
                $("#biglogo").removeClass("logo-off");
                $("#biglogo").addClass("logo-on");
            } else {
                $("#biglogo").removeClass("logo-on");
                $("#biglogo").addClass("logo-off");
            }

        } else {
            if (pos > 0) {
                $("#biglogo").removeClass("logo-off");
                $("#biglogo").addClass("logo-on");
            } else {
                $("#biglogo").removeClass("logo-on");
                $("#biglogo").addClass("logo-off");
            }
        }
*/
    });

})(jQuery); // end of jQuery name space
