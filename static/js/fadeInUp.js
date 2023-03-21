window.onscroll = function() {myFunction1()};
var header, sticky, mainNews, mainNewsImg, samacharAntarbarta, filmyApis, multimediaTippadi, sampadakiyaCelebrity,a, a1, a2, a3, a4, a4;
var celebrityNextRelease, videoOther, a6;
header = document.getElementById("myNavbar");
sticky = header.offsetTop;

celebrityNextRelease = document.getElementsByClassName("celebrity-next-release")[0];
a = celebrityNextRelease.offsetTop;

mainNews = document.getElementsByClassName("section-main-news")[0];
mainNewsImg = document.getElementsByClassName("main-news-image")[0];
a1 = mainNewsImg.offsetTop;

samacharAntarbarta = document.getElementsByClassName("samachar-antarbarta")[0];
a2 = samacharAntarbarta.offsetTop;

filmyApis = document.getElementsByClassName("filmy-apis")[0];
a3 = filmyApis.offsetTop;

multimediaTippadi = document.getElementsByClassName("multimedia-tippadi")[0];
a4= multimediaTippadi.offsetTop;

sampadakiyaCelebrity = document.getElementsByClassName("sampadakiya-celebrity")[0];
a5= sampadakiyaCelebrity.offsetTop;

videoOther=document.getElementsByClassName("video-and-other")[0];
a6=videoOther.offsetTop;

function myFunction1() {
	if (window.pageYOffset > sticky) {
	    	header.classList.add("sticky");
	  	} 
	else {
	    	header.classList.remove("sticky");
  	}


  	if (window.pageYOffset > sticky) {
    	// mainNews.classList.add("animated");
    	// mainNews.classList.add("fadeIn");
    	celebrityNextRelease.classList.add("yes-display");
  	} 

    if (window.pageYOffset > a) {
      // mainNews.classList.add("animated");
      // mainNews.classList.add("fadeIn");
      mainNews.classList.add("yes-display");
    }

  	if (window.pageYOffset > a1 ) {
    	// samacharAntarbarta.classList.add("animated");
    	// samacharAntarbarta.classList.add("fadeInUp");
    	samacharAntarbarta.classList.add("yes-display");
  	} 
  	// else{
  	// 	samacharAntarbarta.classList.remove("animated");
   //  	samacharAntarbarta.classList.remove("fadeInUp");
  	// }


  	if (window.pageYOffset > a2) {
    	// filmyApis.classList.add("animated");
    	// filmyApis.classList.add("bounceInRight");
    	filmyApis.classList.add("yes-display");
  	} 


  	if (window.pageYOffset > a3) {
    	// multimediaTippadi.classList.add("animated");
    	// multimediaTippadi.classList.add("bounceInRight");
    	multimediaTippadi.classList.add("yes-display");
  	} 


  	if (window.pageYOffset > a4) {
    	// sampadakiyaCelebrity.classList.add("animated");
    	// sampadakiyaCelebrity.classList.add("bounceInUp");
    	sampadakiyaCelebrity.classList.add("yes-display");
  	} 


    if (window.pageYOffset > a5) {
      // sampadakiyaCelebrity.classList.add("animated");
      // sampadakiyaCelebrity.classList.add("bounceInUp");
      videoOther.classList.add("yes-display");
    } 
};