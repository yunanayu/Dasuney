<template>
  <b-container style="height: 100vh">
    <h1 class="dasney">Dasney+ </h1>
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
    <section class="device center">
      <h2>즐겨 사용하는 기기에서 시청 가능</h2>
      <p class="text-medium">TV, 컴퓨터, 스마트폰 & 태블릿, 게임 콘솔</p>
      <div class="grid-list four-column mobile-two-column">
        <div>  
        <img src="@/assets/tvicon.png" />
          <h3>TV</h3>
        </div>
        <div>
          <img src="@/assets/comicon.png" />
          <h3>컴퓨터</h3>
        </div>
        <div>
          <img src="@/assets/phoneicon.png" />
          <h3>스마트폰 & 태블릿</h3>
        </div>
        <div>
          <img src="@/assets/gameicon.png" />
          <h3>게임 콘솔</h3>
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
.grid-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 100px;
  grid-gap: 15px;
  padding: 15px;
}
img {
  width: 200px;
  height: 200px;
  filter: invert(100%) sepia(0%) saturate(7430%) hue-rotate(148deg) brightness(98%) contrast(101%);
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
