(function ($, defaultOS) {

var switchOS = function (name) {
  $('.os').hide().filter('.' + name).show();   // Show only current OS.

  // Show fallback is a block does not contain current OS.
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

})(jQuery, DEFAULT_OS);
