import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
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
      console.log(res)
      console.log('로그인 성공')
      Token.value = res.data.key
      tempUsername.value = username
      router.push({name:'home'})
    })
    .catch(err => console.log(err))
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
      console.log(res)
      console.log('회원가입 완료')
      router.push({name:'login'})
    })
    .catch(err => console.log(err))
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
      router.push({name:'home'})
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
      headers: {
        accept: 'application/json',
        Authorization: `Bearer ${TMDB_KEY}`
        }
    })
    .then((res) => {
      // console.log(res.data)
      actors.value = res.data
    })
    .catch((err)=>{console.log(err);})
  }

  return { LogIn, Token, SignUp, logout, getCredits, isAuthenticated, getActors, actors, tempUsername}
}, { persist:true })
