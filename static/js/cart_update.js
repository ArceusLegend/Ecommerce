// Delete Item
$(document).on("click", ".delete-button", function (e) {
  e.preventDefault();
  var prodid = $(this).data("index");
  var url = $(this).data("url");
  $.ajax({
    type: "POST",
    url: url,
    data: {
      productid: $(this).data("index"),
      csrfmiddlewaretoken: "{{csrf_token}}",
      action: "post",
    },
    success: function (json) {
      $('.product-item[data-index="' + prodid + '"]').remove();
      document.getElementById("subtotal").innerHTML = json.subtotal;
      document.getElementById("cart-qty").innerHTML = json.qty;
    },
    error: function (xhr, errmsg, err) {},
  });
});

// Update Item
$(document).on("click", ".update-button", function (e) {
  e.preventDefault();
  var prodid = $(this).data("index");
  var url = $(this).data("url");
  $.ajax({
    type: "POST",
    url: url,
    data: {
      productid: $(this).data("index"),
      productqty: $("#select" + prodid + " option:selected").text(),
      csrfmiddlewaretoken: "{{csrf_token}}",
      action: "post",
    },
    success: function (json) {
      document.getElementById("cart-qty").innerHTML = json.qty;
      document.getElementById("subtotal").innerHTML = json.subtotal;
    },
    error: function (xhr, errmsg, err) {},
  });
});
