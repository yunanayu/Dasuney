<template>
  <main :class="color">
    <div class="bg"></div>
    <div class="wrapper">
      <h1 class="font1">
        <span @click="goIntro">Dasuney+</span>
        <h2 class="font2">made by @Sinwoong @Yuna</h2>
      </h1>
    </div>
  </main>
</template>

<script>
export default {
  
  data() {
    return {
      color: 'your-initial-class',
      inputText: '',
      user: {
        name: 'WEBS',
      },
    };
  },
  mounted() {
    const colors = ['blue'];
    this.changeColor(colors[Math.floor(Math.random() * colors.length)]);
  },
  methods: {
    changeColor(newColor) {
      this.color = newColor;
    },
  },
};
</script>
<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
const goIntro = function () {
  router.push({name:'intro'})
}
</script>
<style lang="scss" scoped>
/* 필요한 스타일을 여기에 추가 */

.wrapper {
  position: absolute;
  width: auto;
  height: 150px;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  text-align: center;
}

.wrapper h1 {
  font-size: 200px;
  margin: 0;
  font-weight: normal;
}

.wrapper h2 {
  font-size: 40px;
  margin-top: 60px;
  font-weight: normal;
  line-height: 10px;
}

.font1 { 
  font-family: disney;
}
.font2 { font-family: disney; }

@mixin content($color, $id) {
  
  animation: bgNeon-#{$id} 3s infinite;
  
  $colorNeon: $color;
  $colorLightNeon: lighten($colorNeon, 30%);
  $shadowColor: adjust-hue($colorNeon, -30);
  $bgNeon: adjust-color($shadowColor, $lightness: -40%);
  
  .input-text {
    color: $colorNeon;
  }
  
  .wrapper h1 {
    animation: neon2-#{$id} 3s infinite;
  }
  
  .wrapper h2 {
    text-shadow: 0 0 10px $colorNeon, 0 0 30px $shadowColor;
    color: $colorNeon;
  }
  
  @keyframes neon2-#{$id} {
    0% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
    80% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
    81% {
      color: #222;
      text-shadow: 0 0 10px #000, 1px 1px rgb(99, 74, 82), -2px 0px 4px #29121A;
    }
    94% {
      color: #222;
      text-shadow: 0 0 10px #000, 1px 1px rgb(99, 74, 82), -2px 0px 4px #29121A;
    }
    95% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
    96% {
      color: #222;
      text-shadow: 0 0 10px #000, 1px 1px rgb(99, 74, 82), -2px 0px 4px #29121A;
    }
    97% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
    98% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
    99% {
      color: #222;
      text-shadow: 0 0 10px #000, 1px 1px rgb(99, 74, 82), -2px 0px 4px #29121A;
    }
    100% {
      color: $colorNeon;
      text-shadow: 0 0 10px $colorNeon, 1px 1px $colorLightNeon, 0 0 280px $shadowColor;
    }
  }
  
  @keyframes bgNeon-#{$id} {
    0% { background-color: $bgNeon; }
    80% { background-color: $bgNeon; }
    81% { background-color: #111; }
    94% { background-color: #111; }
    95% { background-color: $bgNeon; }
    96% { background-color: #111; }
    97% { background-color: $bgNeon; }
    98% { background-color: $bgNeon; }
    99% { background-color: #111; }
    100% { background-color: $bgNeon; }
  }
  
}
main.blue { @include content(#03A9F4, 4); }
</style>
