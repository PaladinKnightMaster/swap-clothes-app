// Initialize Materialize components using jQuery
$(document).ready(function(){
	$('.sidenav').sidenav();
	$('.tooltipped').tooltip();
	$('select').formSelect();
	// scrolling effect for items on My Profile page
	$('.carousel').carousel({
		dist: -30,
		shift: -20,
	});
	$('.register input#username, .register input#password').characterCounter();
});

$('.item-creator-container').on('click', function() {
	$(this).next().toggleClass('visible')
})