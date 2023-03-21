
/*$(document).ready(function () {

    var navListItems = $('div.setup-panel div a'),
        allWells = $('.setup-content'),
        allNextBtn = $('.nextBtn');

    allWells.hide();

    navListItems.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr('href')),
            $item = $(this);

        if (!$item.hasClass('disabled')) {
            navListItems.removeClass('btn-success').addClass('btn-default');
            $item.addClass('btn-success');
            allWells.hide();
            $target.show();
            $target.find('input:eq(0)').focus();
        }
    });

    allNextBtn.click(function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
            curInputs = curStep.find("input[type='text'],input[type='url']"),
            isValid = true;

        $(".form-group").removeClass("has-error");
        for (var i = 0; i < curInputs.length; i++) {
            if (!curInputs[i].validity.valid) {
                isValid = false;
                $(curInputs[i]).closest(".form-group").addClass("has-error");
            }
        }

        if (isValid) nextStepWizard.removeAttr('disabled').trigger('click');
    });

    $('div.setup-panel div a.btn-success').trigger('click');
});*/


//MENU DROPDOWN
     $(document).ready(function () {
$('.navbar .dropdown').hover(function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown(150);
    }, function () {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp(105)
    });
});


//BACK TO TOP
      $(document).ready(function(){

$(function(){
 
    $(document).on( 'scroll', function(){
 
      if ($(window).scrollTop() > 100) {
      $('.scroll-top-wrapper').addClass('show');
    } else {
      $('.scroll-top-wrapper').removeClass('show');
    }
  });
 
  $('.scroll-top-wrapper').on('click', scrollToTop);
});
 
function scrollToTop() {
  verticalOffset = typeof(verticalOffset) != 'undefined' ? verticalOffset : 0;
  element = $('body');
  offset = element.offset();
  offsetTop = offset.top;
  $('html, body').animate({scrollTop: offsetTop}, 500, 'linear');
}

});




//MOBILE MENU

function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}



//HISTORY

(function($){
    $('.history-item').owlCarousel({
      items: 1,
      loop:true,
      margin:10,        
      nav: true,
      dots: true,        
      navText: ['<span class="fa fa-angle-left"></span>','<span class="fa fa-angle-right"></span>'],        
      responsiveClass:true,
      responsive:{
          0:{
              items:1
          },
  
          600:{
              items:3
          },

          1000:{
              items:5
          }
      }
    });

})(jQuery);


//ACCORDIAN
 $(".set > a").on("click", function() {
      if ($(this).hasClass("active")) {
        $(this).removeClass("active");
        $(this)
          .siblings(".set .content")
          .slideUp(200);
        $(".set > a i")
          .removeClass("fa-minus")
          .addClass("fa-plus");
      } else {
        $(".set > a i")
          .removeClass("fa-minus")
          .addClass("fa-plus");
        $(this)
          .find("i")
          .removeClass("fa-plus")
          .addClass("fa-minus");
        $(".set > a").removeClass("active");
        $(this).addClass("active");
        $(".set .content").slideUp(200);
        $(this)
          .siblings(".set .content")
          .slideDown(200);
      }
    });



//SIDEBAR MENU

/*function sticky_relocate() {
    var window_top = $(window).scrollTop() ;
    var footer_top = $(".footer").offset().top - 30;
    var div_top = $('#sticky-anchor').offset().top;
    var div_height = $(".sidebar").height();
    var leftHeight = $('.left-container').height(); 

    if (window_top + div_height > footer_top){
        $('.sidebar').removeClass('stick');
      $('.sidebar').addClass('abs');
       $('.right-conatainer').css('min-height', leftHeight + 'px');
      }
    else if (window_top > div_top) {
        $('.sidebar').addClass('stick');
        $('.sidebar').removeClass('abs');
    } else {
        $('.sidebar').removeClass('stick');
        $('.sidebar').removeClass('abs');
    }
}

$(function () {
    $(window).scroll(sticky_relocate);
    sticky_relocate();
});
*/


//TAb

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

//sscroll

$(document).scroll(function () {
    var y = $(this).scrollTop();
    if (y > 700) {
        $('.bottomMenu').fadeIn();
    } else {
        $('.bottomMenu').fadeOut();
    }

});

$(document).scroll(function () {
    var y = $(this).scrollTop();
    if (y > 700) {
        $('.bottomMenu1').fadeOut();
    } else {
        $('.bottomMenu1').fadeIn();
    }

});









//homepage tab

// $(function() {
//   var $tabButtonItem = $('#tab-button li'),
//       $tabSelect = $('#tab-select'),
//       $tabContents = $('.tab-contents'),
//       activeClass = 'is-active';

//   $tabButtonItem.first().addClass(activeClass);
//   $tabContents.not(':first').hide();

//   $tabButtonItem.find('a').on('hover', function(e) {
//     var target = $(this).attr('href');

//     $tabButtonItem.removeClass(activeClass);
//     $(this).parent().addClass(activeClass);
//     $tabSelect.val(target);
//     $tabContents.hide();
//     $(target).show();
//     e.preventDefault();
//   });

//   $tabSelect.on('change', function() {
//     var target = $(this).val(),
//         targetSelectNum = $(this).prop('selectedIndex');

//     $tabButtonItem.removeClass(activeClass);
//     $tabButtonItem.eq(targetSelectNum).addClass(activeClass);
//     $tabContents.hide();
//     $(target).show();
//   });
// });



//TRIP SECTION

(function($){
    $('.trip-item').owlCarousel({
      items: 1,
      loop:true,
      margin:10,        
      nav: true,
      dots: true,        
      autoplay:true,
      autoplayTimeout:5000,
      navText: ['<span class="fa fa-angle-left"></span>','<span class="fa fa-angle-right"></span>'],        
      responsiveClass:true,
      responsive:{
          0:{
              items:1
          },
  
          600:{
              items:1
          },

          1000:{
              items:1
          }
      }
    });

})(jQuery);

/**********everest accordian**********/

//TESTIMONIALS

(function($){
    $('.testi-item').owlCarousel({
      items: 1,
      loop:true,
      margin:10,        
      nav: true,
      dots: true,        
      autoplay:true,
      autoplayTimeout:3000,
      navText: ['<span class="fa fa-angle-left"></span>','<span class="fa fa-angle-right"></span>'],        
      responsiveClass:true,
      responsive:{
          0:{
              items:1
          },
  
          600:{
              items:2
          },

          1000:{
              items:3
          }
      }
    });

})(jQuery);

//GALLERY POPUP 

    $('.portfolio-item').isotope({
    itemSelector: '.item',
    layoutMode: 'fitRows'
   });
   $('.portfolio-menu ul li').click(function(){
    $('.portfolio-menu ul li').removeClass('active');
    $(this).addClass('active');
    
    var selector = $(this).attr('data-filter');
    $('.portfolio-item').isotope({
      filter:selector
    });
    return  false;
   });
   $(document).ready(function() {
   var popup_btn = $('.popup-btn');
   popup_btn.magnificPopup({
   type : 'image',
   gallery : {
    enabled : true
   }
 });
});


//new page js



