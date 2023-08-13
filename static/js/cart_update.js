$(document).on('click', '#add-button', function(e){
    e.preventDefault();
    console.log($('#select option:selected').text())
    $.ajax({
        type: 'POST',
        url: '{% url "cart:cart_add" %}',
        data: {
            productid: $('#add-button').val(),
            productqty: $('#select').val(),
            crsfmiddlewaretoken: "{{csrf_token}}",
            action: 'post'
        },
        success: function (json) {},
        error: function (xhr, errmsg, err) {}
    });
});