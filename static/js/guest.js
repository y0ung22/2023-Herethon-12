const diaryList = document.getElementById("diary-list");
const DIARY_KEY = "diary"; // 키 설정

// 목록 하나하나 출력
function paintDiaries(newdiary) {
  const liDiv = document.createElement("div"); // div로 수정
  liDiv.id = newdiary.id; // 구별 아이디값 저장
  liDiv.className = "box";
  const div = document.createElement("div");
  div.id = "content"; // css 맞춰서 지정해주기
  const div2 = document.createElement("div");
  div2.id = "wdate";
  const hr = document.createElement("hr");
  hr.id = "line";
  div.innerText = newdiary.text; // 보여줘야하니까 입력받은 텍스트 값!!
  div2.innerText = newdiary.date; // 보여줘야하니까 입력받은 텍스트 값!!

  liDiv.appendChild(div2); // 날짜엘리먼트추가
  liDiv.appendChild(hr);
  liDiv.appendChild(div); // 내용
  diaryList.appendChild(liDiv);

  // 엘리먼트 클릭 시 업데이트 창으로 이동
  liDiv.addEventListener("click", function () {
    window.location.href = `./pages/update.html?keyId=${liDiv.id}`; // id 넘기기
  });
}

// 로컬 스토리지에서 얻어온 투두들
const savedDiaries = localStorage.getItem(DIARY_KEY);

if (savedDiaries !== null) {
  // 데이터가 있으면
  const parsedDiaries = JSON.parse(savedDiaries); // 배열로 변환
  //toDos = parsedDiaries; // 투두 db에 배열로 변환된 것 넣어줌. (데이터 넣어줌!!)
  parsedDiaries.forEach(paintDiaries); // 각각의 아이템을 paintDiaries의 매개변수로 줌
  // 그럼 각각이 출력됨!! (전체~)
}
