var fields = document.getElementsByClassName('dialogue-field');
for (var i = 0; i < fields.length; i++) {
  fields[i].addEventListener('click', function() {
    var form = document.createElement('form');
    form.method = 'POST';
    form.action = '/submit';
    var field = document.createElement('input');
    field.type = 'hidden';
    field.name = 'value';
    field.value = this.value;
    form.appendChild(field);
    document.body.appendChild(form);
    form.submit();
  });
}
