<template>
  <div class="flex flex-col grow h-full">
    <div
      class="flex flex-col min-h-[340px] w-full bg-gradient-to-b from-sky-500 to-violet-600 px-5 py-5 gap-3"
    >
      <div class="flex items-center gap-5">
        <div
          class="flex justify-center items-center w-[192px] h-[192px] bg-blue-400 shadow-lg shadow-gray-900"
        >
          <svg
            role="img"
            height="50"
            width="50"
            aria-hidden="true"
            data-testid="playlist"
            viewBox="0 0 30 30"
            data-encore-id="icon"
            class="fill-gray-100 Svg-sc-ytk21e-0 gQUQL"
          >
            <path
              d="M6 3h15v15.167a3.5 3.5 0 1 1-3.5-3.5H19V5H8v13.167a3.5 3.5 0 1 1-3.5-3.5H6V3zm0 13.667H4.5a1.5 1.5 0 1 0 1.5 1.5v-1.5zm13 0h-1.5a1.5 1.5 0 1 0 1.5 1.5v-1.5z"
            ></path>
          </svg>
        </div>
        <h1
          v-for="k in counter.Get_song_play_list.data"
          v-show="counter.show_bang_DSP == k.id"
          class="text-gray-200 text-[55px] font-bold"
        >
          Danh sách Phát #{{ k.name }}
        </h1>
      </div>
      <div class="flex flex-col w-full grow py-5 text-[14px]">
        <div class="flex text-gray-200 border-b-[1px] border-gray-200 py-2">
          <h1 class="w-[15%]">#</h1>
          <h1 class="w-[45%]">Tiêu đề</h1>
          <h1 class="w-[20%]">Nghệ sĩ</h1>
          <h1 class="w-[10%]">Thời gian</h1>
          <h1 class="w-[10%]"></h1>
        </div>
        <div
          class="flex flex-col"
          v-show="counter.show_bang_DSPN == index"
          v-for="(j, index) in counter.Get_song_play_list.data"
        >
          <div
            v-for="(i, index) in j.Play_list_Link"
            class="flex text-gray-100 border-b-[1px] border-gray-200 py-3 items-center"
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
            <h1 class="w-[10%]">{{ i.duration }}</h1>
            <div class="w-[10%] flex gap-2 items-center">
              <font-awesome-icon
                icon="fa-solid fa-ellipsis"
                v-on:click="
                  counter.Show_deletete = i.id + counter.show_bang_DSPN;
                  counter.pk = i.id;
                "
                class="text-gray-300 text-[25px] cursor-pointer"
              />
              <div
                v-show="counter.Show_deletete == i.id + counter.show_bang_DSPN"
                v-on:click="delete_song_PL()"
                class="bg-sky-400 rounded px-3 py-1 w-[100px] h-[30px] text-gray-100 text-[13px] cursor-pointer"
              >
                Xóa
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="flex flex-col bg-gradient-to-t from-black to-[#21183e] w-full grow px-5 py-5"
    >
      <div
        class="flex bg-white h-[40px] gap-3 items-center w-[364px] rounded-full px-3"
      >
        <button>
          <svg
            v-on:click="counter.F_Search_Song()"
            role="img"
            height="24"
            width="24"
            aria-hidden="true"
            class="fill-gray-900 Svg-sc-ytk21e-0 uPxdw mOLTJ2mxkzHJj6Y9_na cursor-pointer_"
            viewBox="0 0 24 24"
            data-encore-id="icon"
          >
            <path
              d="M10.533 1.279c-5.18 0-9.407 4.14-9.407 9.279s4.226 9.279 9.407 9.279c2.234 0 4.29-.77 5.907-2.058l4.353 4.353a1 1 0 1 0 1.414-1.414l-4.344-4.344a9.157 9.157 0 0 0 2.077-5.816c0-5.14-4.226-9.28-9.407-9.28zm-7.407 9.279c0-4.006 3.302-7.28 7.407-7.28s7.407 3.274 7.407 7.28-3.302 7.279-7.407 7.279-7.407-3.273-7.407-7.28z"
            ></path>
          </svg>
        </button>
        <input
          placeholder="Hãy tìm bài hát"
          @keyup.enter="counter.F_Search_Song()"
          class="w-full outline-none text-gray-600"
          v-model="counter.Search_Song"
        />
      </div>
      <h1 class="text-gray-200 text-[22px] font-bold mb-3 mt-3">
        Hãy thêm nội dung vào Danh sách Phát của bạn
      </h1>
      <div
        v-for="(i, index) in counter.Data_Search_Song.Data"
        class="flex text-gray-100 border-b-[1px] border-gray-700 py-3 items-center"
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
          v-on:click="
            counter.add_song_play_list(
              i.name,
              i.artist,
              i.duration,
              i.poster,
              i.mp3_file,
              i.id,
              counter.show_bang_DSP
            )
          "
          clclass="w-[20%]"
        >
          <button
            class="px-3 py-1 rounded-full font-bold border-[1px] border-gray-200"
          >
            Add
          </button>
        </div>
      </div>
    </div>
    <!-- bang nhap ten -->
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
    this.counter.get_song_play_list();
    this.counter.F_Search_Song();
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
      this.counter.Pause_Start = true;
    },
    async delete_song_PL() {
      await this.counter.delete_song_play_list();
      this.counter.get_song_play_list();
    },
  },
  components: {},
};
</script>
