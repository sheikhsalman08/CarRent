$(function(){
	$('.DSubmitSearch').click(function(e) {
		e.preventDefault();
		$.ajax({
			type:"POST",
			url:'/search/',
			data:{
				'location': $('.geoposition-address').text(),
				'model': $('.form-control').val(),
				'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
				},
			success: successSearch
		});
	});
});
		
function successSearch(data, textStatus, jqXHR){
	i = $('.geoposition-address').text()
	j = $('.form-control').val()
	console.log(i)
	console.log(j)
	$('#search-result').html(data)
}