import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const navshow = true
  const tempUsername = ref('')
  const Token = ref('')
  const actors = ref([])
  const isAuthenticated = computed(()=>{
    if (Token.value === '') {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()
  const TMDB_KEY = import.meta.env.VITE_TMDB_API_KEY
  const YOUTUBE_KEY = import.meta.env.YOUR_YOUTUBE_API_KEY
  const LogIn = function (payload) {
    const { username, password } = payload
    
    axios({
      method : 'post',
      url : 'http://127.0.0.1:8000/accounts/login/',
      data : {
        username,
        password
      }
    })
    .then((res) => {
      // console.log(res)
      window.alert('로그인 성공')
      Token.value = res.data.key
      tempUsername.value = username
      router.push({name:'home'})
    })
    .catch((err) => {
      console.log(err)
      window.alert('존재하지않는 회원입니다.')
    })
  }

  const SignUp = function (payload) {
    const { username, password1, password2 } = payload
    axios({
      method : 'post',
      url : 'http://127.0.0.1:8000/accounts/signup/',
      data : {
        username,
        password1,
        password2
      }
    })
    .then((res) => {
      // console.log(res)
      window.alert('회원가입 완료')
      router.push({name:'login'})
    })
    .catch((err) => {
      console.log(err)
      if (password1 != password2) {
        window.alert('비밀번호가 다릅니다.')
      }
    })
  }

  const logout = function () {
    axios({
      method:'post',
      url:'http://127.0.0.1:8000/accounts/logout/'
    })
    .then((res)=>{
      console.log(res.data);
      window.alert('로그아웃 완료');
      Token.value = ''
      tempUsername.value = ''
      router.push({name:'intro'})
    })
    .catch(err=>console.log(err))
  }
  const movies = ref([])

  const getMovieList = function () {
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/movies/',
      headers : {
        Authorization:`Token ${Token.value}`
      }
      })
      .then((res) => {
        movies.value = res.data
      })
      .catch(err=>console.log(err))
    
  }
  const getCredits = function(movieId) {
    axios({
      method:'get',
      url : `https://api.themoviedb.org/3/movie/${movieId}/credits`,
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_KEY}`
        }
    })
    .then((res)=>{
      console.log(res.data);
    })
    .catch(err=>console.log(err))
  }

  const getActors = function () {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/actors/',
      headers : {
        Authorization:`Token ${Token.value}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      actors.value = res.data
    })
    .catch((err)=>{console.log(err);})
  }
  
  const directors = ref([])

  const getDirectors = function () {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/movies/directors/',
      headers : {
        Authorization:`Token ${Token.value}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      directors.value = res.data
    })
    .catch((err)=>{console.log(err);})
  }

  return {navshow,directors,getDirectors ,TMDB_KEY, YOUTUBE_KEY, LogIn, Token, SignUp, logout, getCredits, isAuthenticated, getActors, actors, tempUsername, getMovieList, movies}
}, { persist:true })
