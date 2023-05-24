<template>
  <div class="h-full grow">
    <div class="flex bg-[#5038A0] gap-5 px-5 py-6 items-end">
      <img
        src="@/assets/timm.png"
        class="w-[192px] h-[192px] shadow-lg shadow-gray-900"
      />
      <div class="flex flex-col text-white font-semibold">
        <h1>Danh sách phát</h1>
        <h1 class="text-[65px]">Bài hát yêu thích</h1>
        <div class="flex text-[14px] gap-1">
          <h1>{{ counter.Data_User.username }}</h1>
          <h1>/</h1>
          <h1>{{ counter.Get_song_love.length }} song</h1>
        </div>
      </div>
    </div>
    <div class="h-14 grid grid-cols-3 gap-4 content-start ...">
      <button>
        <img src="@/assets/play.png" class="lg:w-[50px] lg:h-[50 px]" />
        <!-- flex bg-[#5038A0] gap-5 px-5 py-6 items-end -->
        <!-- lg:w-[50px] lg:h-[50 px] -->
      </button>
      <button class="absolute right-0 h-16 w-20">
        <img
          src="@/assets/kinh.png"
          v-b-tooltip.hover
          title="Tìm trong danh sách phát"
          class="lg:w-[40px] lg:h-[40 px]"
        />
      </button>
    </div>
    <div
      class="flex flex-col grow shrink-0 bg-gradient-to-t from-black to-[#21183e] h-full px-5 py-5 text-[14px]"
    >
      <div class="flex text-gray-400 border-b-[1px] border-gray-800 py-2">
        <h1 class="w-[15%]">#</h1>
        <h1 class="w-[45%]">Tiêu đề</h1>
        <h1 class="w-[20%]">Nghệ sĩ</h1>
        <h1 class="w-[10%]"></h1>
        <h1 class="w-[10%]">Thời gian</h1>
      </div>
      <div
        v-for="(i, index) in counter.Get_song_love"
        class="flex text-gray-100 border-b-[1px] border-gray-800 py-3 items-center"
      >
        <h1 class="w-[15%]">{{ index + 1 }}</h1>
        <div
          v-on:click="
            Play_all();
            Get_data_song(i);
          "
          class="flex w-[45%] gap-3 cursor-pointer"
        >
          <img :src="i.poster" class="w-[50px] h-[50px] rounded" />
          <div class="flex flex-col gap-2 h-[50px]">
            <h1 class="text-[16px]">{{ i.name }}</h1>
            <h1 class="text-[13px] text-gray-400">{{ i.artist }}</h1>
          </div>
        </div>
        <h1 class="w-[20%]">{{ i.artist }}</h1>
        <div
          v-on:click="counter.delete_song_love(i.name)"
          class="w-[10%] flex justify-end items-center pr-5"
        >
          <svg
            class="Svg-sc-ytk21e-0 gQUQL absolute fill-green-500 cursor-pointer"
            role="img"
            height="16"
            width="16"
            aria-hidden="true"
            viewBox="0 0 16 16"
            data-encore-id="icon"
          >
            <path
              d="M15.724 4.22A4.313 4.313 0 0 0 12.192.814a4.269 4.269 0 0 0-3.622 1.13.837.837 0 0 1-1.14 0 4.272 4.272 0 0 0-6.21 5.855l5.916 7.05a1.128 1.128 0 0 0 1.727 0l5.916-7.05a4.228 4.228 0 0 0 .945-3.577z"
            ></path>
          </svg>
        </div>
        <h1 class="w-[10%]">{{ i.duration }}</h1>
      </div>
    </div>
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
