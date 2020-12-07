$(document).ready(function()
{

	// search filter for name
	$("#searchByName").on("keyup", function() 
	{
		var value = $(this).val().toLowerCase();
		$(".wt-name").filter(function()
		{
			$(this).parent().toggle($(this).text().toLowerCase().indexOf(value) != -1);
		});
	});

	// search filter for location
	$("#searchByLocation").on("keyup", function() 
	{
		var value = $(this).val().toLowerCase();
		$(".wt-location").filter(function()
		{
			$(this).parent().toggle($(this).text().toLowerCase().indexOf(value) != -1);
		});
	});

	// search filter for type
	$("#searchByType").on("keyup", function() 
	{
		var value = $(this).val().toLowerCase();
		$(".wt-type").filter(function()
		{
			$(this).parent().toggle($(this).text().toLowerCase().indexOf(value) != -1);
		});
	});

	// onclick of div mainblock
	$('.wt-mainblock').click(function()
	{
		var name = $(this).children('h2').text() + '.html';
		window.location.href = name;
	});

	$("#rate-sub-btn").hide();

	$('.wt-big-star').click(function()
	{
		$('#rate-sub-btn').fadeIn();
	});

	$('#rate-1').click(function()
	{
		$('#rate-1').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-2').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-3').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-4').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-5').removeClass("fas fa-star").addClass("far fa-star");
	});

	$('#rate-2').click(function()
	{
		$('#rate-1').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-2').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-3').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-4').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-5').removeClass("fas fa-star").addClass("far fa-star");
	});

	$('#rate-3').click(function()
	{
		$('#rate-1').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-2').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-3').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-4').removeClass("fas fa-star").addClass("far fa-star");
		$('#rate-5').removeClass("fas fa-star").addClass("far fa-star");
	});

	$('#rate-4').click(function()
	{
		$('#rate-1').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-2').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-3').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-4').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-5').removeClass("fas fa-star").addClass("far fa-star");
	});

	$('#rate-5').click(function()
	{
		$('#rate-1').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-2').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-3').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-4').removeClass("far fa-star").addClass("fas fa-star");
		$('#rate-5').removeClass("far fa-star").addClass("fas fa-star");
	});

});


function rate(num)
{
	var part;
	switch(num)
	{
		case 0: part = 	'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;
		case 0.5: part ='<span class="fas fa-star-half-alt wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;
		case 1: part = 	'<span class="fas fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;
		case 1.5: part ='<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star-half-alt wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;
		case 2: part = 	'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;

		case 2.5: part ='<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star-half-alt wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;

		case 3: part = 	'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;

		case 3.5: part ='<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star-half-alt wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;

		case 4: part = 	'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="far fa-star wt-star"></span>';
				break;

		case 4.5: part ='<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star-half-alt wt-star"></span>';
				break;

		case 5: part = 	'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>'+
						'<span class="fas fa-star wt-star"></span>';
				break;

	}

	return part;
}