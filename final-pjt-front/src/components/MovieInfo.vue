<template>
  <div>
    <img :src="(`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`)" alt="">
    <p>제목 : {{ movieInfo.title }}</p>
    <p>개봉일 : {{ movieInfo.release_date }}</p>
    <p>러닝타임 :{{ movieInfo.runtime }} 분</p>
    <p>TMDB 평점 : {{ movieInfo.vote_average }}</p>
    <h4>장르</h4>
    <p v-for="genre in movieInfo.genres">{{ genre.name }}</p>
    <h3>줄거리</h3>
    <p>{{ movieInfo.overview }}</p>
    <button @click.prevent="hopeMovie(movieInfo.title)">{{ isLiked ? '안볼래영' : '보고싶어여!!!!!!!!!!!!!!!!'}}</button>
    <hr>
    <div>
      <h3>평점 주기</h3>
      <button @click="reRateScore(0)" :style="{ color: scoreColor(0) }">0점</button>
      <fieldset class="rate">
        <input type="radio" @click="reRateScore(10)" id="rating10" name="rating" value="10"><label for="rating10" title="5점"></label>
        <input type="radio" @click="reRateScore(9)" id="rating9" name="rating" value="9"><label class="half" for="rating9" title="4.5점"></label>
        <input type="radio" @click="reRateScore(8)" id="rating8" name="rating" value="8"><label for="rating8" title="4점"></label>
        <input type="radio" @click="reRateScore(7)" id="rating7" name="rating" value="7"><label class="half" for="rating7" title="3.5점"></label>
        <input type="radio" @click="reRateScore(6)" id="rating6" name="rating" value="6"><label for="rating6" title="3점"></label>
        <input type="radio" @click="reRateScore(5)" id="rating5" name="rating" value="5"><label class="half" for="rating5" title="2.5점"></label>
        <input type="radio" @click="reRateScore(4)" id="rating4" name="rating" value="4"><label for="rating4" title="2점"></label>
        <input type="radio" @click="reRateScore(3)" id="rating3" name="rating" value="3"><label class="half" for="rating3" title="1.5점"></label>
        <input type="radio" @click="reRateScore(2)" id="rating2" name="rating" value="2"><label for="rating2" title="1점"></label>
        <input type="radio" @click="reRateScore(1)" id="rating1" name="rating" value="1"><label class="half" for="rating1" title="0.5점"></label>
        
      </fieldset>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref,onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
const store = useCounterStore()
const props = defineProps({
  movieInfo : Object
})
const isLiked = ref(false)
// 영화 좋아요
const hopeMovie = function (movietitle) {
  const movie = store.movies.find((movie) => movie.title === movietitle)
  axios({
    method : 'post',
    url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    // console.log(res.data.is_liked)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
}


const reRateScore = function (score) {
  // 만약 선택된 점수가 0이면, 평가가 없음을 나타내기 위해 -1로 설정합니다
  selectedScore.value = score === 0 ? -1 : score;

  // 만약 점수가 -1(평가 없음)이면 요청을 보내지 않습니다
  if (selectedScore.value === -1) {
    console.log("0점으로 평가되지 않습니다.");
    return;
  }

  const movie = store.movies.find((movie) => movie.title == props.movieInfo.title);
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/movies/${movie.id}/score/`,
    headers: {
      Authorization: `Token ${store.Token}`,
    },
    data: {
      score: selectedScore.value,
    },
  })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => console.log(err));
};

onMounted(() => {
  const movie = store.movies.find((movie) => movie.title == props.movieInfo.title)
  axios({
    method : 'get',
    url : `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
    headers : {
      Authorization:`Token ${store.Token}`
    }
  })
  .then((res) => {
    // console.log(res.data.is_liked)
    isLiked.value = res.data.is_liked
  })
  .catch(err => console.log(err))
})

const scoreColor = (index) => {
  const filledScore = Math.floor(selectedScore.value);

  if (index <= filledScore) {
    return 'gold';
  } else if (index === filledScore + 1 && selectedScore.value % 1 !== 0) {
    // 반개 별을 위한 부분적으로 채워진 별
    const gradient = (selectedScore.value % 1) * 100;
    return `linear-gradient(90deg, gold ${gradient}%, white ${gradient}%)`;
  } else {
    return 'white';
  }
};

let selectedScore = ref(-1);


</script>

<style scoped>
@import url(//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css);
.rate { display: inline-block;border: 0;margin-right: 15px;}
.rate > input {display: none;}
.rate > label {float: right;color: #ddd}
.rate > label:before {
  display: inline-block;
  font-size: 50px; /* 별의 크기를 100px로 조절 */
  padding: .3rem .2rem;
  margin: 0;
  cursor: pointer;
  font-family: FontAwesome;
  content: "\f005 ";
}
.rate .half:before {content: "\f089 "; position: absolute;padding-right: 0;}
.rate input:checked ~ label, 
.rate label:hover,.rate label:hover ~ label { color: #f3f308 !important;  } 
.rate input:checked + .rate label:hover,
.rate input input:checked ~ label:hover,
.rate input:checked ~ .rate label:hover ~ label,  
.rate label:hover ~ input:checked ~ label { color: #f3f308 !important;  } 
</style>

