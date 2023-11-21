<template>
  
  <b-container style="height: 100vh">
    <h1 class="dasney">Dasney+ </h1>
    <img src="@/assets/lala.jpg" alt="">
    <div class="banner">
      
      <div>
        <figure class="text-start">
          <blockquote class="blockquote text-white">
            <h1>
              취향에 따라 골라보는 다양한<br />
              컨텐츠가 모두 한자리에
              
            </h1>
          </blockquote>
          <figcaption class="blockquote-footer text-white">
            <h3>지금 바로 회원이 되어보세요</h3>
          </figcaption>
        </figure>
      </div>
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
    <section class="device center">
      <h2>즐겨 사용하는 기기에서 사용하세요</h2>
      <div class="grid-list four-column mobile-two-column">
        <div class="icon-container">
          <div class="icon-item">
            <img src="@/assets/tvicon.png" alt="TV" class="icon"/>
            <h3>TV</h3>
          </div>
          <div class="icon-item">
            <img src="@/assets/comicon.png" alt="컴퓨터" class="icon"/>
            <h3>컴퓨터</h3>
          </div>
          <div class="icon-item">
            <img src="@/assets/phoneicon.png" alt="스마트폰 & 태블릿" class="icon"/>
            <h3>스마트폰 & 태블릿</h3>
          </div>
          <div class="icon-item">
            <img src="@/assets/gameicon.png" alt="게임 콘솔" class="icon"/>
            <h3>게임 콘솔</h3>
          </div>
        </div>
      </div>
    </section>
  </b-container>
</template>

<script>
export default {
  name: "home",
  components: {},
};
</script>

<style scoped>
/* .banner {
  position: relative;
  background-image: url("@/assets/lala.jpg");
  background-size: cover;
} */


/* .banner::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 50%;
  width: 50%;
  background: linear-gradient(to left, rgba(0, 0, 0, 0.6), transparent);
  z-index: 1;
}
.banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 200px;
  background: #000;
  z-index: 1;
  
}

.banner > div {
  position: relative;
  z-index: 2;
  white-space: nowrap;
} */
.icon-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.icon-item {
  text-align: center;
  filter: invert(100%) sepia(0%) saturate(7430%) hue-rotate(148deg) brightness(98%) contrast(101%);
  
}
.grid-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-auto-rows: 100px;
  grid-gap: 15px;
  padding: 15px;
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

</style>
