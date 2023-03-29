   // A $( document ).ready() block.
$(document).ready(function() {
    document.getElementById("nacionalidad").addEventListener("change", function() {
        var paisValue = document.getElementById("nacionalidad").value;
        alert(paisValue);
        if (paisValue != null) {
            alert(paisValue);
            $.ajax({
                url: "{% url 'appCrud:ajax_campo' %}",
                type: "GET",
                data: {
                  'nacionalidad': paisValue,
                  'csrfmiddlewaretoken': '{{ csrf_token }}'  // Agrega esta línea si estás usando CSRF protection
                },
                dataType: 'json',
                success: function(data) {
                  document.getElementById("nac").value = data.nacionalidad;
                }
              });
        }
     
      });
});
