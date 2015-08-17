(function ($) {

    $(function () {
        $('.button-collapse').sideNav();
        $('.sticky').Stickyfill();
        console.log("document ready.");
    }); // end of document ready

    // automatic fade in/out of navbar logo on
    // landing page when scrolled
    if (SITE_AREA === "landing") {

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
        });
    } else {
        // navbar logo auto fade in/out: OFF
    }

})(jQuery); // end of jQuery name space
