
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
	$('.register input#username, .register input#password, input#item_name, textarea#short_desc, textarea#long_desc').characterCounter();

	// Code used from Code Institute task manager mini project, classes changed to fit formating for this project
	validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border": "2px solid #26b38f", "box-shadow": "none" };
        let classInvalid = { "border": "2px solid #f44336", "box-shadow": "none" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border") != "2px solid rgb(38, 179, 143)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});


$('.item-creator-container').on('click', function() {
	$(this).next().toggleClass('visible')
})

// Sweetalert delete confirmation pop-up
// Sweetalert code used from sweetalert documentation on https://sweetalert2.github.io/
function deleteConfirm(link) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
          )
        // Go to link in href attribute of the delete button clicked
        // This code was taken from a tutorial on https://www.seblod.com/resources/tutorials/sebold-and-sweetalert2-replace-the-default-delete-confirm-box
          window.location.href = link;
        }
    })
}

// Prevent delete until it's confirmed in sweetaert pop-up
// This code was taken from a tutorial on  https://www.seblod.com/resources/tutorials/sebold-and-sweetalert2-replace-the-default-delete-confirm-box
$('.delete-confirm').click(function(event) {
    // Prevent opening link in href attribute before sweetalert modal runs
    event.preventDefault();
    // Get link in the href attribute of delete button
    let link = $(this).attr("href");
    // Run Sweetalert function
    deleteConfirm(link)
})


