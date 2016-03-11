var i=0;
var imgArr=["url(2.jpg) no-repeat center center fixed",
			"url(3.jpg) no-repeat center center fixed",
			"url(4.jpg) no-repeat center center fixed",
			"url(1.jpg) no-repeat center center fixed"];

function bgcf(){
	setInterval(function(){
		console.log("use img: " + i);
		jQuery('html').css('background',imgArr[i]);
		jQuery('html').css('background-size','cover');
		i++;
		if(i==(imgArr.length)) i=0;
	}, 3000);
}

bgcf();
