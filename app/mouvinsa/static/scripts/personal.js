var maxSteps = 10000; //TO-DO: mettre le vrai max de l'utilisateur

var actToolTip = document.querySelector('.activity-data > .tooltip');

var days = document.querySelectorAll('.calendar > li');

var datePicker = document.getElementById('date-picker');
var dateView = document.getElementById('date-view');

var today = document.getElementById('today');
if(today) {
  today = today.value;
}

for(var d = 0; d < days.length; d++) {
  var dayIterate = days[d];
  var steps = dayIterate.dataset.step;
  if(steps) {
    steps = parseInt(steps, 10);
    dayIterate.style.background = stepToHSL(steps);
    if(dayIterate.id == "date-" + today) {
      dayIterate.classList.add("calendar-today");
    }

    dayIterate.addEventListener('mouseenter', function(e) {
      actToolTip.innerHTML = "";
      actToolTip.appendChild(document.createTextNode(e.target.dataset.date));
      actToolTip.appendChild(document.createElement("br"));
      actToolTip.appendChild(document.createTextNode(e.target.dataset.step));
      actToolTip.style.display = "block";
    });
    dayIterate.addEventListener('mousemove', function(e) {
      actToolTip.style.left = (e.offsetX || e.layerX) - 50 + "px";
      actToolTip.style.top  = (e.offsetY || e.layerY) - 68 + "px";
    });
    dayIterate.addEventListener('mouseleave', function(e) {
      actToolTip.style.display = "none";
    });
  }
}

var datePickerOpen = false;

if(dateView) {
  dateView.addEventListener('click', function(e) {
    if(datePickerOpen) {
      datePickerOpen = false;
      datePicker.style.display = "none";
    } else {
      datePickerOpen = true;
      datePicker.style.display = "block";
    }
  });
}

if(datePicker) {
  datePicker.addEventListener('click', function(e) {
    if(e.target.tagName == "LI") {
      document.getElementById('date').value = e.target.id.substr(2);
      dateView.firstChild.textContent = e.target.innerHTML + " ";
      datePickerOpen = false;
      datePicker.style.display = "none";
      var d = new Date(today);
      d.setDate(d.getDate()-1);
      document.getElementById('date-'+ d).classList.add('calendar-today');
      dayIterate.classList.add("calendar-today");
    }
  });
}

setTimeout(function() {
  var circle = document.getElementsByClassName('bar');
  for(var i = 0; i < circle.length; i++)  {
    var el = circle[i];
    var val = el.parentElement.nextElementSibling.firstChild.textContent;
    if (isNaN(val)) {
      val = 100;
    }
    else{
      var r = el.r.baseVal.value;
      var c = Math.PI*(r*2);

      if (val < 0) { val = 0;}
      if (val > 100) { val = 100;}

      var pct = ((100-val)/100)*c;

      console.log(r);
      el.style.strokeDashoffset = pct;
    }
  };
}, 500);

/* jQuery parce que je suis pressé */
var activityForm = $('#activity-form');
activityForm.submit(function(e) {
  e.preventDefault();
  $.ajax({
    type: "POST",
    url: activityForm.attr('action'),
    data: activityForm.serializeArray(),
    success: function(ret) {
      console.log(ret);
      var calendarEntry = document.getElementById('date-'+ret.date);
      calendarEntry.dataset.step = ret.stepj;
    },
    dataType: "json"
  });
});

function stepToHSL(steps) {
  if(steps == 0)
    return "hsl(123, 70%, 100%)";
  var l = steps * 50 / maxSteps;
  return "hsl(123,70%," + (80 - l) + "%)";
}

// Our labels and three data series
var data = {
  labels: ['Week1', 'Week2', 'Week3', 'Week4', 'Week5', 'Week6', 'Week7', 'Week8'],
  series: [
    [5000, 12000, 8000, 7000, 9000, 10000, 1000, 10000],
    [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000 ]
  ]
};

// We are setting a few options for our chart and override the defaults
var options = {
  // Disable line smoothing
  lineSmooth: false,
  // X-Axis specific configuration
  axisX: {
    // We can disable the grid for this axis
    showGrid: false,
    // and also don't show the label
    showLabel: false
  },
  // Y-Axis specific configuration
  axisY: {
    // Lets offset the chart a bit from the labels
    offset: 60
  }
};

var $chart = $('.ct-chart');

var $toolTip = $chart
.append('<div class="tooltip"></div>')
.find('.tooltip')
.hide();

$chart.on('mouseenter', '.ct-point', function() {
  var $point = $(this),
    value = $point.attr('ct:value'),
    seriesName = $point.parent().attr('ct:series-name');
  $toolTip.html(value + " Pas").show();
});

$chart.on('mouseleave', '.ct-point', function() {
  $toolTip.hide();
});

$chart.on('mousemove', function(event) {
  $toolTip.css({
    left: (event.offsetX || event.originalEvent.layerX) - $toolTip.width() / 2 - 10,
    top: (event.offsetY || event.originalEvent.layerY) - $toolTip.height() - 40
  });
});

// All you need to do is pass your configuration as third parameter to the chart function
new Chartist.Line('.ct-chart', data, options);