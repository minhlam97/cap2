<template>
    <div class="text-white h-full w-full flex flex-col ">
        <div  class="grid grid-cols-3 border-b-[1px] border-zinc-600 py-5 items-center font-bold">
            <h1 class="flex w-[250px] ml-[50px]">STT</h1>
            <h1 class="flex w-[250px] ml-[50px]">Tên bài hát</h1>
            <h1>Nghệ sĩ</h1>
        </div>
        <div v-for="i in counter.Data_Search_Song.Data" v-on:click=" counter.Play(); Get_data_song(i);" class="grid grid-cols-3 text-gray-300 border-b-[1px] border-zinc-600  items-center font-normal py-2 cursor-pointer">
            <img :src="i.poster" class="w-[100px] rounded" />
            <h1 class="flex w-[250px] ml-[50px]">{{ i.name }}</h1>
            <h1>{{ i.artist }}</h1>
        </div>
    </div>
</template>
<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'
import { AtomSpinner, FulfillingSquareSpinner, HalfCircleSpinner, TrinityRingsSpinner, HollowDotsSpinner } from 'epic-spinners'


export default {

    setup() {
        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.counter.F_Search_Song();
    },
    methods:{
        Get_data_song(i){
            this.counter.Play_nhac.URL = i.mp3_file;
            this.counter.Play_nhac.Name_song = i.name;
            this.counter.Play_nhac.Name_artist = i.artist;
            this.counter.Play_nhac.Photo = i.poster;
            this.counter.Pause_Start=true;
        }
    },
    components: {
        AtomSpinner, FulfillingSquareSpinner, HalfCircleSpinner, TrinityRingsSpinner, HollowDotsSpinner
    }
}
</script>