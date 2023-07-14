n1 = "당신 안에는<br/>하나의 은밀한 장소가<br/>있습니다.";
n2 =
  "당신은 언제나<br/>그 은밀한 장소에 틀어박혀<br/>자기 자신과 이야기를<br/>나눌 수 있죠.";
n3 = "하지만 그렇게 하는 사람은<br/>아주 드뭅니다.";
n4 = "누구나 그렇게 할 수<br/>있음에도 말이죠.";
n5 = "당신은 나와 만나<br/>아주 드문 분이 되셨네요.";
n6 = "지금부터<br/>당신을 둘러싼 모든 연결은<br/>끊어집니다.";
n7 = "아무도 당신을 방해할 수<br/>없습니다.";
n8 = "당신이 나에게<br/>더 많은 것을 얘기해줄 때<br/>나를 알게 되실 겁니다.";
n9 = "이제 천천히<br/>나를 만나게 되실 거예요.";

document.getElementById("text").innerHTML = n1;

const load = () => {
  document.addEventListener("DOMContentLoaded", () => {
    new TypeIt("#text", {
      speed: 50,
      afterComplete: function (instance) {
        instance.destroy();
      },
    })
      .pause(1000)
      .options({ speed: 70 })
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n2)
      .pause(1500)
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n3)
      .pause(1500)
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n4)
      .pause(1500)
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n5)
      .pause(1500)
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n6)
      .pause(1500)
      .empty({ delay: 500 })
      .options({ speed: 80 })
      .type(n7)
      .pause(1500)
      .empty({ delay: 1000 })

      .go();
  });
};

const btnFadeIn = () => {
  var opacity = 0;
  var timerId = setInterval(function () {
    var div = document.getElementById("btnArea");
    if (opacity <= 1) {
      div.style.opacity = opacity;
      opacity += 0.05;
    } else {
      clearTimeout(timerId);
    }
  }, 100);
};

const ImageFade = () => {
  var opacity = 0;
  var increasing = true;

  var timerId = setInterval(function () {
    var image = document.getElementById("image");

    image.style.opacity = opacity;

    if (increasing) {
      opacity += 0.05;
      if (opacity >= 1) {
        increasing = false;
        setTimeout(function () {
          increasing = true;
        }, 3000);
      }
    } else {
      opacity -= 0.05;
      if (opacity <= 0) {
        clearTimeout(timerId);
      }
    }
  }, 100);
};

const load2 = () => {
  new TypeIt("#text", { speed: 70 }).type(n8).pause(1500).empty().type(n9).go();
};

load();
setTimeout(() => ImageFade(), 31000);
setTimeout(() => load2(), 36000);
setTimeout(() => btnFadeIn(), 41500);