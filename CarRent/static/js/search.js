$(function(){
	$('.DSubmitSearch').click(function(e) {
		e.preventDefault();

		var car_model = $('.DCarModel').val()

		if (car_model.length === 0 ){				// if mobile version is on than search form part change
				var car_model = $('.DCarModel2').val()
		}

		$.ajax({
			type:"POST",
			url:'/search/',
			data:{
				'location': $('.geoposition-address').text(),
				'model': car_model,
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
				},
			success: successSearch
		});
	});
});
		
function successSearch(data, textStatus, jqXHR){

	$('.DSearchResult').html(data)

}