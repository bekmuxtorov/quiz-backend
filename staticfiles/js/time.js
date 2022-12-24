function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = parseInt(minutes / 60) + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    let meTime = document.getElementById("meTime").innerHTML;

    let t = Number(meTime);
    // t = 3;
    var fiveMinutes = 60 * t,
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};



function stopTime() {
    let stopT = document.getElementById("time").innerText;
    let get_timer = stopT.split(":");
    let min = get_timer[0];
    let sec = get_timer[1]
    let min_int = parseInt(min);
    let sec_int = parseInt(sec);
    let timeOut = min_int * 60 + sec_int;
    console.log(timeOut);

    return timeOut;
}


let res = stopTime();
document.getElementById("result").innerHTML = res;
console.log(res);