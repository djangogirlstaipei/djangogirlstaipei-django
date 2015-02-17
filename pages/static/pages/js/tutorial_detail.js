(function ($, katex, defaultOS) {

$('span.math').each(function () {
  katex.render(this.textContent, this);
});

var switchOS = function (name) {
  // Show only text code blocks for current OS.
  $('.os').hide().filter('.' + name).show();

  // Show fallback in code block collections without variant for current OS.
  $('pre.os.default').each(function () {
    $(this)[$(this).siblings('pre.os.' + name).size() ? 'hide' : 'show']();
  });
};

switchOS(defaultOS);

$('#id_os').change(function (e) {

  var name = $(this).val();
  switchOS(name);

  // Set OS selection via AJAX.
  var form = $(this).closest('form');
  $.post(form.attr('action'), form.serialize());
});

})(jQuery, katex, DEFAULT_OS);
