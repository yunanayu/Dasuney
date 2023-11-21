<template>
  <b-container style="height: 100vh">
      <div class="banner">
        <div class="bannerposition">
            <h1 class="dasney">Dasney+ </h1><br>
            <h1>취향에 따라 골라보는 다양한<br>컨텐츠가 모두 한자리에</h1><br>
            <h5 style="color: gray;">지금 바로 회원이 되어보세요</h5>
          <div class="accounts">
            <router-link :to="{ name: 'login' }">
              <div class="email-container">
                <form class="email-form">
                  <div><button>로그인</button></div>
                </form>
              </div>
            </router-link>
            <router-link :to="{ name: 'signup' }">
              <div class="email-container">
                <form class="email-form">
                  <div><button>회원가입</button></div>
                </form>
              </div>
            </router-link>
          </div>
        </div>
      </div>
      <div>
        <h2 style="margin-top: 20px; text-align: center;">즐겨 사용하는 기기에서 사용하세요</h2>
        <div class="grid-list four-column mobile-two-column">
          <div class="icon-container">
            <div class="icon-item">
              <img src="@/assets/tvicon.png" alt="TV" class="icon"/>
              <h3>TV</h3>
            </div>
            <div class="icon-item">
              <img src="@/assets/comicon.png" alt="컴퓨터" class="icon"/>
              <h3>PC</h3>
            </div>
            <div class="icon-item">
              <img src="@/assets/phoneicon.png" alt="스마트폰 & 태블릿" class="icon"/>
              <h3>Mobile</h3>
            </div>
            <div class="icon-item">
              <img src="@/assets/gameicon.png" alt="게임 콘솔" class="icon"/>
              <h3>Game Console</h3>
            </div>
          </div>
        </div>
      </div>
  </b-container>
</template>

<script>
// import { onMounted } from 'vue';
// import { useRouter } from 'vue-router';

// const router = useRouter()

// onMounted(() => {
//   setTimeout(() => {
//     router.push({name:'home'}
//     , 3000)
//   })
// })
// import { ref, onMounted } from 'vue'

// export default {
//   setup() {
//     // ref를 사용하여 타이머 상태를 저장
//     const timerFinished = ref(false)

//     // onMounted 훅에서 타이머 설정
//     onMounted(() => {
//       setTimeout(() => {
//         // 타이머가 끝나면 timerFinished 값을 true로 변경하고 라우터 이동
//         timerFinished.value = true
//       }, 3000)
//     })

//     return {
//       timerFinished
//     }
//   },

//   // watch를 사용하여 timerFinished 값이 변경될 때마다 라우터 이동
//   watch: {
//     timerFinished(value) {
//       if (value) {
//         this.$router.push('/home')
//       }
//     }
//   }
// }
</script>

<style scoped>
.banner {
  position: relative;
  background-image: linear-gradient(to right, rgba(0, 0, 0, 1.0), rgba(0, 0, 0, 0)), url("@/assets/lala.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  height: 900px;
  position: relative;
}
img {
  filter: invert(100%) sepia(0%) saturate(7430%) hue-rotate(148deg) brightness(98%) contrast(101%);
}

.banner > div {
  position: relative;
  z-index: 2;
  white-space: nowrap;
}
.bannerposition {
  position: absolute ;
  /* left: 100px; */
  top: 250px;
  margin-left: 100px;
}
.bannertext {
  margin-bottom: 20px;
}
.icon-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.icon-item {
  text-align: center;

}
.grid-list {
  display: grid;
  /* grid-template-columns: repeat(2, 1fr); */
  grid-auto-rows: 300px;
  grid-gap: 100px;
  padding: 30px;
}
.icon {
  width: 200px;
  height: 200px;
  margin-bottom: 20px;
}
.accounts {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 100px;
  grid-gap: 15px;
  padding: 15px;
}
.dasney {
  font-family: 'disney';
  font-size: 70px;
}
.email-container {
  width: 100%;
  margin-bottom: 24px;
}

.email-form {
  display: flex;
  flex-direction: column;
}

.email-form button {
  margin-top: 10px;
  border-radius: 4px;
  padding: 0 44px;
  height: 50px;
  max-width: 500px;
  background: #0063e5;
  border: none;
  color: #f9f9f9;
  text-decoration: none;
  width: 100%;
  cursor: pointer;
  transition: all 0.2s ease 0s;
  font-weight: 400;
  letter-spacing: 1px;
  font-size: 18px;
  line-height: 18px;
  box-sizing: border-box;
  border-radius: 4px 4px 4px 4px;
  margin: 10px;
}

.email-form button:hover {
  background: #016cf9;
}

h3 {
  color: white;
}

@media (min-width: 769px) {
  /* 데스크탑 전용 스타일을 추가할 수 있습니다. */
}

@media (min-width: 577px) and (max-width: 768px) {
  /* 태블릿 전용 스타일을 추가할 수 있습니다. */
  .bannerposition {
    left: 50px; /* 태블릿용 왼쪽 위치 조정 */
    top: 150px; /* 태블릿용 상단 위치 조정 */
  }

  .grid-list {
    grid-gap: 50px; /* 태블릿용 그리드 간격 조정 */
  }

  .icon {
    width: 150px;
    height: 150px;
    margin-bottom: 15px;
  }

  .email-form button {
    padding: 0 30px;
    height: 40px;
    font-size: 16px;
  }

  /* 태블릿용 이미지 크기 조정 */
  .banner {
    height: 600px; /* 이미지 높이 조정 */
  }

  .icon {
    width: 120px; /* 이미지 너비 조정 */
    height: 120px; /* 이미지 높이 조정 */
    margin-bottom: 10px;
  }
}

@media (max-width: 576px) {
  /* 모바일 전용 스타일 추가 */
  .bannerposition {
    left: 20px; /* 모바일용 왼쪽 위치 조정 */
    top: 100px; /* 모바일용 상단 위치 조정 */
  }

  .grid-list {
    grid-gap: 30px; /* 모바일용 그리드 간격 조정 */
  }

  .icon {
    width: 100px; /* 이미지 너비 조정 */
    height: 100px; /* 이미지 높이 조정 */
    margin-bottom: 10px;
  }

  .email-form button {
    padding: 0 20px;
    height: 30px;
    font-size: 14px;
  }

  /* 모바일용 이미지 크기 조정 */
  .banner {
    height: 400px; /* 이미지 높이 조정 */
  }
}
</style>
