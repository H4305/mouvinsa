/**
 * Created by vcaen on 16/12/2014.
 */
$(document).ready(function() {
    var end = Date.parse("5 Jan 2015 8:00:00 +0100");
    var now = Date.now();
    var remainingSeconds = (end - now) / 1000;
    var clock = $('.your-clock').FlipClock(remainingSeconds, {
        // ... your options here
        countdown: true,
        clockFace: 'DailyCounter'
    });
});