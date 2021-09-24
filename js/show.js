function show(name)
{
	if ($('#for_set_text')) //初始化
	{
		if (false) {
			$('#for_set_text').remove();
			return;
		} else{
			$('#for_set_text').remove();
		};
		
	}

	$('#' + name).after('<div id="for_set_text" class="container"></div>');
	$('#for_set_text').append('<object data="text/' + name + '.html" class="sch_text"></object>');
};