$(document).ready(function(){

  new WOW().init();

  $("#side-menu-singup").click(function(){
    $("#side-menu").animate({
  height: "toggle",
  opacity: "toggle",
});
    $("#side-menu-singup").hide();
    $("#side-menu-singup1").css({"display": "initial", });

  });

  $("#side-menu-singup1").click(function(){
         $("#side-menu").animate({
       height: "toggle",
       opacity: "toggle"
     });
         $("#side-menu-singup1").hide();
         $("#side-menu-singup").css({"display": "initial", });
       })


  $('.form_datetime').datetimepicker({
      //language:  'fr',
      weekStart: 1,
      todayBtn:  1,
  autoclose: 1,
  todayHighlight: 1,
  startView: 2,
  forceParse: 0,
      showMeridian: 1
  });
$('.form_date').datetimepicker({
      language:  'fr',
      weekStart: 1,
      todayBtn:  1,
  autoclose: 1,
  todayHighlight: 1,
  startView: 2,
  minView: 2,
  forceParse: 0
  });
$('.form_time').datetimepicker({
      language:  'fr',
      weekStart: 1,
      todayBtn:  1,
  autoclose: 1,
  todayHighlight: 1,
  startView: 1,
  minView: 0,
  maxView: 1,
  forceParse: 0
  });

  $("#see-more-car").click(function(){
    $(".car-part-hidden").toggle();

  });

  $("#see-more-car1").click(function(){
    $(".car-part-hidden1").toggle();

  });

  $("#see-more-car2").click(function(){
    $(".car-part-hidden2").toggle();

  });

   $("#see-more-delar").click(function(){
     $(".delar-hide").toggle();

   });

   $("#full-button").click(function(){
     $("#car-part-search").toggle();

   });

   $("#full-button1").click(function(){
     $("#car-part-search").toggle();

   });

   $("#cancle-more-car").click(function(){
     $("#car-part-search").hide();

   });



         $(window).scroll(function() {
               var height = $(window).scrollTop();
             if(height > 50  )  {
                 $("#second-menu-bar").css({"display": "none", });
             }else if(($(window).width() > 1400 )){
               $("#second-menu-bar").css({"display": "none", });
             }
             else{
               $("#second-menu-bar").css({"display": "initial",  });
             }
         });


});
