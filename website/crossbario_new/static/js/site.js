(function ($) {

    $(function () {
        console.log("document ready.");
        $('.button-collapse').sideNav();
    }); // end of document ready

    $(window).scroll(function () {
        if ($(document).scrollTop() > 0) {
            $("nav").addClass("nav-scroll-nontop");
            $("nav").removeClass("nav-scroll-top");
            //$('body').scrollTo('#main');
        } else {
            $("nav").addClass("nav-scroll-top");
            $("nav").removeClass("nav-scroll-nontop");
        }
    });

})(jQuery); // end of jQuery name space
