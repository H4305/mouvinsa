/* jQuery parce que je suis pressé */
var questionForm = $('#question-form');
questionForm.submit(function(e) {
  e.preventDefault();

  var value = $("#select-value").val();
  console.log(value);
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