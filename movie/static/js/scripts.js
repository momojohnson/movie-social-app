$(document).ready(function() {
	$('.trailer').magnificPopup({
		
		type: 'iframe',
		
	});
	$('.trailer').on('click', function(){
		$('.popup-content').append($('div.mfp-bg').html())
	})
});