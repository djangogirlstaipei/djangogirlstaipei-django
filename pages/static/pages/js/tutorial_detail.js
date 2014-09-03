(function ($, defaultOS) {

$('.language-toggles a').click(function (e) {
  e.preventDefault();

  $(this).addClass('active');
  $(this).parent().siblings().children('a').removeClass('active');

  var name = $(this).data('name');
  History.replaceState(null, $(document).find('title').text(), '?os=' + name);
  $('pre.os').hide().filter('.' + name).show();   // Show only current OS.

  // Show fallback is a block does not contain current OS.
  $('pre.os.default').each(function () {
    $(this)[$(this).siblings('pre.os.' + name).size() ? 'hide' : 'show']();
  });
});

$('.language-toggles .' + defaultOS).click();

})(jQuery, DEFAULT_OS);
