$(window).scroll(function(event) {
    if($(this).scrollTop() > -1) {
    	$('.header_top-block').addClass('fixed');
    	return true;
	}
	else {
    	$('.header_top-block').removeClass('fixed');
 	}
});