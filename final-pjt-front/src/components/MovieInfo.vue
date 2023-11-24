<template>
  <div class="container">
    <div class="movie-detail">
      <h1>{{ movieInfo.title }} 상세 정보</h1>
      <div class="header">
        <img :src="`https://image.tmdb.org/t/p/w500/${movieInfo.poster_path}`" alt="영화 포스터">
        <div class="movie-info">
          <button class="like-button" @click.prevent="hopeMovie">
            <span v-if="isLiked">🚫</span> <!-- 여기에 보고 싶어요 취소 아이콘을 넣어도 좋습니다 -->
            <span v-else>🎬</span> <!-- 여기에 보고 싶어요 아이콘을 넣어도 좋습니다 -->
            {{ isLiked ? '보고 싶어요 취소' : '보고 싶어요!' }}
          </button>
          <h1>{{ movieInfo.title }}</h1>
          <p class="release-date">{{ movieInfo.release_date }}</p>
          <p class="runtime">{{ movieInfo.runtime }} 분</p>
          <p class="tmdb-rating">TMDB 평점: {{ movieInfo.vote_average }}</p>
          <div class="genres">
            <h4>장르</h4>
            <p v-for="genre in movieInfo.genres" :key="genre.id">{{ genre.name }}</p>
          </div>
        </div>
      </div>
      <div class="rating-section" style="position: relative;">
        <h2>이 영화 평가하기</h2>
        <div class="rate" v-if="!moviescore">
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
        </div>
        <div v-else>
          <div class="user-rating">
          <h2>내 평점 : {{ moviescore.score }} 점 </h2>
          <!-- <span v-for="i in moviescore.score / 2" :key="i" class="active">★</span>
          <span v-for="i in (10 - moviescore.score) / 2" :key="i" class="inactive">☆</span> -->
        </div>
      </div>
      <button v-if="moviescore" @click="cancelRating" class="score-button">❌ 평가 취소</button>
    </div>

    <div class="plot-summary">
      <h2>줄거리</h2>
      <p>{{ movieInfo.overview }}</p>
    </div>
    <hr>
  </div>
  </div>
</template>
  
  <script setup>

  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import { useCounterStore } from '../stores/counter';
  import { useRouter } from 'vue-router';
  const store = useCounterStore();
  // const props = defineProps(['movieInfo']);
  const props = defineProps({
    movieInfo : Object
  });
  const router = useRouter()
  const isLiked = ref(false);
  const selectedScore = ref(-1);
  
  const moviescore = ref(null)
  
  const hopeMovie = function () {
    const movie = store.movies.find((m) => m.title === props.movieInfo.title);
  
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
      headers: {
        Authorization: `Token ${store.Token}`
      }
    })
    .then((res) => {
      isLiked.value = res.data.is_liked;
    })
    .catch(err => console.log(err));
  };
  
  const reRateScore = function (score) {
    if (selectedScore.value === 0) {
      selectedScore.value = -1;
    } else {
      selectedScore.value = score === 0 ? -1 : score;
    }
  
    if (selectedScore.value === -1) {
      console.log("0점으로 평가되지 않습니다.");
      return;
    }
  
    const movie = store.movies.find((m) => m.title === props.movieInfo.title);
  
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/movies/${movie.id}/score/`,
      headers: {
        Authorization: `Token ${store.Token}`
      },
      data: {
        score: selectedScore.value
      }
    })
    .then((res) => {
      // console.log(res.data);
      moviescore.value = res.data
      window.alert('평가완료되었습니다.!')
      // console.log(score)
      console.log(moviescore.value);
    })
    .catch((err) => {
      console.log(err)
      window.alert('이미 평가하셨습니다.')
    });
  };
  
  const cancelRating = function () {
    if (!moviescore.value) {
      console.error('취소할 평점이 없습니다.')
      window.alert('취소할 평점이 없습니다.')
      return 
    } else {
      // 평가 취소 버튼을 눌렀을 때 선택된 별 초기화
      selectedScore.value = -1;
    
      // 선택된 별이 없다면 초기화하는 로직을 추가할 수 있습니다.
      const stars = document.querySelectorAll('input[name="rating"]');
      stars.forEach((star, index) => {
        star.checked = false;
      });
    
      axios({
        method :'delete',
        url : `http://127.0.0.1:8000/movies/${moviescore.value.movie}/score/${moviescore.value.id}/`,
        headers: {
          Authorization: `Token ${store.Token}`
        },
      })
      .then ((res) => {
        console.log("평가가 취소되었습니다.");
        moviescore.value = null
        window.alert("평가가 취소되었습니다.");
        console.log(moviescore.value);
      })
    }
  }
  

  
  onMounted(() => {
    store.getMovieList()
    const movie = store.movies.find((m) => m.title === props.movieInfo.title);
    console.log(movie);
    if (movie.score_set.length > 0) {
      moviescore.value = movie.score_set[0]
      console.log(moviescore.value)
    } else {
      moviescore.value = null
    }
    // console.log(moviescore.value)
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/movies/${movie.id}/movielike/`,
      headers: {
        Authorization: `Token ${store.Token}`
      }
    })
    .then((res) => {
      isLiked.value = res.data.is_liked;
    })
    .catch(err => console.log(err));
  });
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
  .movie-detail {
    font-family: 'Arial', sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .header {
    display: flex;
    align-items: center;
    margin-top: 30px;
  }
  
  .header img {
    max-width: 200px;
    margin-right: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  .movie-info {
    color: white
  }
  
  .movie-info h1 {
    font-size: 1.5em;
    margin: 0;
  }
  
  .release-date, .runtime, .tmdb-rating {
    margin: 5px 0;
  }
  
  .genres {
    margin-top: 15px;
  }

  .genres h4 {
    margin-bottom: 5px;
  }
  
  .rating-section {
    margin-top: 20px;
  }
  
  .rating-section h2 {
    font-size: 1.2em;
    margin-bottom: 10px;
  }
  
  
  .like-button {
    background-color: #3498db;
    color: #fff;
    padding: 10px 15px;
    font-size: 1em;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-bottom: 15px;
  }
.like-button:hover {
  background-color: #2980b9;
}
  .score-button {
    background-color: #f01b14;
    color: #fff;
    padding: 10px 15px;
    font-size: 1em;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  .score-button:hover {
  background-color: #ee8d0f;
}
  .like-button:hover {
    background-color: #2980b9;
  }
  
  .plot-summary {
    margin-top: 20px;
  }
  
  .plot-summary h2 {
    font-size: 1.2em;
    margin-bottom: 10px;
  }
  
  .plot-summary p {
    line-height: 1.5;
  }
  
  @media (max-width: 600px) {
    .header {
      flex-direction: column;
      text-align: center;
    }
  
    .header img {
      margin-bottom: 10px;
    }
  }
    /* 스타일링을 위한 CSS를 여기에 추가하세요 */
  .user-rating {
    color: gold; /* 별의 색상을 조절하세요 */
    font-size: 50px; /* 별의 크기를 100px로 조절 */
  }

  .user-rating span {
    margin-right: 5px; /* 별 사이의 간격을 조절하세요 */
  }

  .user-rating .inactive {
    color: lightgray; /* 선택되지 않은 별의 색상을 조절하세요 */
  }
  </style>
  