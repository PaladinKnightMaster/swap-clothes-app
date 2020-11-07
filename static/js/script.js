// Initialize Materialize components using jQuery
$(document).ready(function(){
	$('.sidenav').sidenav();
	$('.tooltipped').tooltip();
	$('select').formSelect();
});

// Implement like button toggle
$('.like-button').on( 'click', function() {
    $(this).toggleClass('far fas') 
});
