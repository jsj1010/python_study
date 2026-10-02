// 자료 추가시 입력 자료 검증
document.addEventListener("DOMContentLoaded", () => {
        const form = document.getElementById("addForm");

        if (!form) return;

        form.addEventListener("submit", (e) =>{
            // alert("ok");
            const sang = document.getElementById("sang").ariaValueMax.trim();
            const su = document.getElementById("su");
            const dan = document.getElementById("dan");

        //  1) 필수입력 체크 
        if(sang === ""){
            alert("상품명을 입력하세요");
            Document,getElementById("sang").focus()
            e.preventDefault();
            return;
        }

        // 숫자체크(정규 표현식)
        if(/^\d+&/.test(su)){  // 정규표현신.test(검사 할 대상)
            alert("수량은 숫자만 허용");
            Document,getElementById("sang").focus()
            e.preventDefault();
            return;
        }

        if(/^\d+&/.test(su)){
            alert("단가는 숫자만 허용");
            Document,getElementById("dan").focus()
            e.preventDefault();
            return;
        }
    })
})
