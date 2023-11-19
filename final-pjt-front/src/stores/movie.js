import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import {useCounterStore} from '@/stores/counter'

export const useMovieStore = defineStore('counter', () => {
  const store = useCounterStore()
  const movies = ref([])
  const getMovieList = function () {
    axios({
      method : 'get',
      url : 'http://127.0.0.1:8000/movies/',
      headers : {
        Authorization:`Token ${store.Token}`
      }
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch(err=>console.log(err))
  }

  return { getMovieList}
}, { persist:true })
