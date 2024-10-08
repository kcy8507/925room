// function scrollDisable() {
//   $("body")
//     .addClass("scrollDisable")
//     .on("scroll touchmove mousewheel", function (e) {
//       e.preventDefault();
//     });
// }
// function scrollAble() {
//   $("body").removeClass("scrollDisable").off("scroll touchmove mousewheel");
// }

$(".nav__toggle").click(function () {
  $("#popup__nav").toggle();
  $("body").addClass("overflow");
});
$(".cancel")
  .unbind("click")
  .bind("click", function () {
    $("#popup__nav").toggle();
    $("body").removeClass("overflow");
  });

// 스크롤 시 nav fade-in

// $(function () {
//   $(document).on("scroll", function () {
//     if ($(window).scrollTop() > 100) {
//       $("#nav").removeClass("deactive");
//       $("#nav").addClass("active");
//     } else {
//       $("#nav").removeClass("active");
//       $("#nav").addClass("deactive");
//     }
//   });
// });
