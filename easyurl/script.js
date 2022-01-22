function sleep(milliseconds) {
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}

var cursor = true;
var speed = 500;
var list = ["h", "t", "t", "p", "s", ":", "/", "/", "w", "w", "w", ".", "g", "o", "o", "g", "l", "e", ".", "d", "e"];
var i = 0;
var size = 25;

async function linkShow() {
    $("#preview p").html("https://www.easyurl.de/fuYVdue");
    for (var x = 361; x > -1; x--) {
        $("#preview").css("transform", "rotate(" + x +"deg)");
        if(size < 26) {
          size += 0.1;
          $("#preview").css("font-size", size + "px");
        }
        await sleep(0.1);
    }
    return
}

async function linkDissapear() {
    for (var x = 0; x < 361; x++) {
        $("#preview").css("transform", "rotate(" + x +"deg)");
        if(size > 1) {
          size -= 0.1;
          $("#preview").css("font-size", size + "px");
        }
        await sleep(0.1);
    }
    $("#preview p").html("");
    return
}

setInterval(() => {
  if(cursor) {
    document.getElementById('cursor').style.opacity = 0;
    cursor = false;
  }else {
    document.getElementById('cursor').style.opacity = 1;
    cursor = true;
  }
}, speed);

setInterval(async () => {
    if(i > list.length + 5) {
        i = 0;
        //$("#preview p").html("https://www.easyurl.de/fuYVdue");
        $("#preview p").html("");
        //await linkDissapear();
        //await linkShow();
    }
    $("#preview p").append(list[i])
    i++;
}, 200);

$(document).ready(function() {
    $("#url").on("input", function() {
        var val = $("#url").val();
        var button = $("#submit");
        if(val.length > 0 && val.search("https://") == 0 || val.search("http://") == 0) {
            button.css("background-color", "green");
            button.css("border", "3px solid white");
            button.css("color", "white");
        } else {
            $("#submit").css("background-color", "rgba(0, 0, 0, 0)");
            button.css("border", "3px solid grey");
            button.css("color", "grey");
        }
    });
    $("#submit").click(async function() {
        var val = $("#url").val();
        if(val.length > 0 && val.search("https://") == 0 || val.search("http://") == 0) {
            var data = val.split(".");
            if(data.length != 1) {
                console.log(data)
            } else {
                var button = $("#submit");
                $("#url").val("");
                $("#submit").css("background-color", "rgba(0, 0, 0, 0)");
                button.css("border", "3px solid grey");
                button.css("color", "grey");
                $("#alert").append("<p>Please enter a valid link!</p>")
                for (var i = 0; i < 100; i++) {
                    $("#alert").css("opacity", i + "%");
                    await sleep(3)
                }
                await sleep(4000)
                for (var i = 100; i > 0; i--) {
                    $("#alert").css("opacity", i + "%");
                    await sleep(3)
                }
                $("#alert p").remove();
            }
        }
    })
    
});