$(function () {
	$.ajax({
		type: 'GET',
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr'
		success: function (data) {
			$('#sf_wind_speed').text(data['query']['results']['channel']['wind']['speed']);
		},
		dataType: 'json'
	});
});
