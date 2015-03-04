/* jQuery parce que je suis pressé */
var questionForm = $('#question-form');
questionForm.submit(function(e) {
  e.preventDefault();

  var value = $("#input-value").val();
  if (value != "") {
    $.ajax({
      type: "POST",
      url: "/questionsante",
      data: questionForm.serializeArray(),
      success: function(ret) {
        console.log(ret);
        $(".overlay").hide();
        $(".modal").hide();
      },
      dataType: "json"
    });
  }
});