<template>
  <div class="flex gap-1 text-white px-5 py-5 font-bold items-center">
    <h1>Danh sách phát</h1>
  </div>
  <div
    class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 px-5 py-5"
  >
    <div
      class="flex justify-end items-end h-60 w-72 aspect-square rounded bg-gradient-to-b from-sky-500 to-violet-600 overflow-hidden relative"
    >
      <h1
        class="absolute z-30 top-0 left-3 text-[25px] text-gray-200 font-bold my-5"
      >
        Bài hát yêu thích
      </h1>
      <div
        class="absolute z-30 top-9 left-3 text-[15px] text-gray-200 font-bold my-5 hover:ml-2"
      >
        <router-link
          to="/Love-Song"
          class="flex items-center gap-2 hover:text-yellow-500 cursor-pointer duration-100 pb-5"
          v-bind:class="{}"
        >
          <h3
            :class="{ 'text-white': counter.Path_Route.path == '/Love-Song' }"
          >
            {{ counter.Get_song_love.length }} bài hát
          </h3>
          <img src="@/assets/play.png" class="lg:w-[50px] lg:h-[50 px]" />
        </router-link>
      </div>
    </div>
    <!-- class="h-60 w-72 aspect-square rounded bg-gradient-to-b from-sky-500 to-yellow-200 overflow-hidden relative left-40" -->
  </div>
</template>

<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";

export default {
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {
    this.counter.get_song_love();
  },
  methods: {
    async Play_all() {
      await this.counter.Play();

      this.counter.duration_mp3 = document.getElementById(
        "nhac"
      ).onloadedmetadata = () => {
        this.counter.duration_mp3 = document.getElementById("nhac").duration;
        this.counter.duration_mp3 = Math.floor(this.counter.duration_mp3);
        if (this.counter.duration_mp3 % 60 >= 10) {
          this.counter.length =
            Math.floor(this.counter.duration_mp3 / 60) +
            ":" +
            (this.counter.duration_mp3 % 60);
        } else {
          this.counter.length =
            Math.floor(this.counter.duration_mp3 / 60) +
            ":0" +
            (this.counter.duration_mp3 % 60);
        }
      };
    },
    Get_data_song(i) {
      this.counter.Play_nhac.URL = i.mp3_file;
      this.counter.Play_nhac.Name_song = i.name;
      this.counter.Play_nhac.Name_artist = i.artist;
      this.counter.Play_nhac.Photo = i.poster;
      this.counter.Play_nhac.Tim = 1;
      this.counter.Pause_Start = true;
    },
  },
  components: {},
};
</script>
