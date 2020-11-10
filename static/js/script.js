// Initialize Materialize components using jQuery
$(document).ready(function(){
	$('.sidenav').sidenav();
	$('.tooltipped').tooltip();
	$('select').formSelect();
	// Dropdown for user socials
	$('.dropdown-trigger').dropdown({
		container: '.item-footer',
	});
	// scrolling effect for items on My Profile page
	$('.carousel').carousel({
		dist: -30
	});
});

  