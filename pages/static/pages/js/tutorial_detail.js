(function ($, defaultOS) {

$('.language-toggles a').click(function (e) {
  e.preventDefault();

  $(this).addClass('active');
  $(this).parent().siblings().children('a').removeClass('active');

  var name = $(this).data('name');
  $('pre.os').hide().filter('.' + name).show();   // Show only current OS.

  // Show fallback is a block does not contain current OS.
  $('pre.os.default').each(function () {
    $(this)[$(this).siblings('pre.os.' + name).size() ? 'hide' : 'show']();
  });

  // Set OS selection via AJAX.
  var form = $('.language-toggles > form');
  $('input[name="os"]', form).val(name);
  $.post(form.attr('action'), form.serialize());
});

$('.language-toggles .' + defaultOS).click();

})(jQuery, DEFAULT_OS);
