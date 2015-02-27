
    /*
 jQuery animateNumber plugin v0.0.10
 (c) 2013, Alexandr Borisov.
 https://github.com/aishek/jquery-animateNumber
*/
(function(d){var p=function(b){return b.split("").reverse().join("")},l={numberStep:function(b,a){var e=Math.floor(b);d(a.elem).text(e)}},h=function(b){var a=b.elem;a.nodeType&&a.parentNode&&(a=a._animateNumberSetter,a||(a=l.numberStep),a(b.now,b))};d.Tween&&d.Tween.propHooks?d.Tween.propHooks.number={set:h}:d.fx.step.number=h;d.animateNumber={numberStepFactories:{append:function(b){return function(a,e){var k=Math.floor(a);d(e.elem).prop("number",a).text(k+b)}},separator:function(b,a){b=b||" ";a=
a||3;return function(e,k){var c=Math.floor(e).toString(),s=d(k.elem);if(c.length>a){for(var f=c,g=a,l=f.split("").reverse(),c=[],m,q,n,r=0,h=Math.ceil(f.length/g);r<h;r++){m="";for(n=0;n<g;n++){q=r*g+n;if(q===f.length)break;m+=l[q]}c.push(m)}f=c.length-1;g=p(c[f]);c[f]=p(parseInt(g,10).toString());c=c.join(b);c=p(c)}s.prop("number",e).text(c)}}}};d.fn.animateNumber=function(){for(var b=arguments[0],a=d.extend({},l,b),e=d(this),k=[a],c=1,h=arguments.length;c<h;c++)k.push(arguments[c]);if(b.numberStep){var f=
this.each(function(){this._animateNumberSetter=b.numberStep}),g=a.complete;a.complete=function(){f.each(function(){delete this._animateNumberSetter});g&&g.apply(this,arguments)}}return e.animate.apply(e,k)}})(jQuery);

    $(document).ready(function () {
        bar = $("#distance-value-bar");
        bar.css("marginRight", "70%");
        bar.animate(
                { marginRight: "0%"},
                {
                    duration: 2000
                });

        var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',');
        km = $("#distance-value-number").html().replace(',', '.');
        var decimal_places = 2;
        var decimal_factor = decimal_places === 0 ? 1 : decimal_places * 10;
        $("#distance-value-number").animateNumber(
                {
                    number: parseFloat(km) * decimal_factor,

                    numberStep: function(now, tween) {
                        var floored_number = Math.floor(now) / decimal_factor,
                                target = $(tween.elem);

                        if (decimal_places > 0) {
                            // force decimal places even if they are 0
                            floored_number = floored_number.toFixed(decimal_places);

                            // replace '.' separator with ','
                            floored_number = floored_number.toString().replace('.', ',');
                        }

                        target.text(floored_number);
                    }
                },
    2000
  );

///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////

$("#distance-bar-rect").animate(
  {width: 1500},
  {
    duration: 1500,
    step: function (now) {
      $(this).attr("width", now);
    }
  });
});


var maxSteps = 10000; //TO-DO: mettre le vrai max de l'utilisateur

var actToolTip = document.querySelector('.activity-data > .tooltip');

var days = document.querySelectorAll('.calendar > li');

var datePicker = document.getElementById('date-picker');
var dateView = document.getElementById('date-view');

var date = document.getElementById('date');

var today = document.getElementById('today');
if(today) {
  today = today.value;
}

if(date) {
  date.value = 0;
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
      actToolTip.appendChild(document.createTextNode(e.target.dataset.step + " Pas"));
      actToolTip.style.display = "block";
    });
    dayIterate.addEventListener('mousemove', function(e) {
      actToolTip.style.left = e.layerX - 50 + "px";
      actToolTip.style.top  = e.layerY - 68 + "px";
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
      date.value = e.target.id.substr(2);
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
        $("#distance-value-number").text(ret.distanceTot);
        $("#dialog-container").show();
        if (ret.hasOwnProperty('errorM')) {
            //window.alert(ret.errorM);
            $("#title-dialog").text("ERROR");
            $("#message-dialog").text(ret.errorM);
        }
        document.getElementById('date-'+ret.date).setAttribute("data-step", "20");
      console.log(ret);
      var calendarEntry = document.getElementById('date-'+ret.date);
      calendarEntry.dataset.step = ret.stepj;
      calendarEntry.style.background = stepToHSL(ret.stepj);
      calendarEntry.classList.add("pulse");
      setTimeout(function() {
        calendarEntry.classList.remove("pulse");
      },2000);

      document.getElementById("distance-value-number").innerHTML = ret.distanceTot;

      document.getElementById("streak").innerHTML = ret.streak + " Jours";
      document.getElementById("best-streak").innerHTML = ret.bestStreak + " Jours";

      if(ret.cityChanged != 'no') {
          $("#title-dialog").text("Nouvelle ville!");
            //window.alert("Vos données ont bien été enregistrées!\n "+ ret.cityChanged);
          $("#message-dialog").text(ret.cityChanged + "\n Date:" + ret.date + "-15    Pas:" + ret.stepj);
      }else{
          $("#title-dialog").text("Confirmation");
          //window.alert("Vos données ont bien été enregistrées!");
          $("#message-dialog").text("Vos données ont bien été enregistrées!\n Date:" + ret.date + "-15    Pas:" + ret.stepj);
      }


      /*data.labels.push(ret.date);
      data.series[0].push(ret.stepj);
      data.series[1].push(objPerso);

      new Chartist.Line('.ct-chart', data, options);*/
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

///////////////////////////////////////////////////////////

var options = {
  lineSmooth: false,
  axisX: {
    showGrid: false,
    showLabel: false
  },
  axisY: {
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

new Chartist.Line('.ct-chart', data, options);

    jQuery(document).ready(function($) {
    $('#button-continue').on('click', function () {
        $("#dialog-container").hide();
    });
});