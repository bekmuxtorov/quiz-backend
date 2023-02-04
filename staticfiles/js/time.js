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
    let meTime = document.getElementById("meTime").innerText;

    let t = Number(meTime);
    // t = 3;
    var fiveMinutes = 60 * t,
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};


let time_result = document.getElementById("time_result").value;
time_result.innerText.value= 4324;
console.log('result', time_result);


console.log('hey');
function stopTime() {
    let stopT = document.getElementById("time").innerText;
    console.log('stopT: ',stopT);
    let get_timer = stopT.split(":");
    console.log('get_timer >>> '+get_timer)
    let min = get_timer[0];
    let sec = get_timer[1]
    let min_int = parseInt(min);
    let sec_int = parseInt(sec);
    let timeOut = (min_int * 60) + sec_int;
    console.log('bu time out', timeOut)
    return timeOut;
}
let res = stopTime();

console.log('salooooooooooooo')


let timetest = document.getElementById('timetest');
timetest.value='jkhkhk';
timetest.innerHTML.value = 'jinni';

console.log('hey2')
console.log('this is stop time: ', res)
console.log('time_result:', time_result)
time_result.innerHTML = 'salom';





function myFunction() {
    document.getElementById("myDIV").style.backgroundColor = "#5846f9";
    document.getElementById("myDIV").style.color = "#fff";
}