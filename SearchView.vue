<template>
  <div class="text-white h-full w-full flex flex-col">
    <div id="cjss" class="h-[300px] w-full flex flex-col overflow-auto">
      <div
        v-for="(i, index) in counter.Data_Search_Song.Data"
        class="flex text-gray-100 border-b-[1px] border-gray-800 py-3 items-center"
      >
        <h1 class="w-[15%]">{{ index + 1 }}</h1>
        <div
          v-on:click="
            Play_all();
            Get_data_song(i);
            counter.add_late_song(
              i.name,
              i.artist,
              i.duration,
              i.poster,
              i.mp3_file,
              i.id,
              counter.Data_User.username
            );
          "
          class="flex w-[35%] gap-3 cursor-pointer"
        >
          <img :src="i.poster" class="w-[50px] h-[50px] rounded" />
          <div class="flex flex-col gap-2 h-[50px]">
            <h1 class="text-[16px]">{{ i.name }}</h1>
            <h1 class="text-[13px] text-gray-400">{{ i.artist }}</h1>
          </div>
        </div>
        <h1 class="w-[20%]"></h1>
        <div class="w-[10%] cursor-pointer">
          <svg
            v-show="i.love == 'love'"
            v-on:click="
              counter.add_song_love(
                i.name,
                i.artist,
                i.duration,
                i.poster,
                i.mp3_file,
                i.id,
                counter.Data_User.username
              );
              i.love = 1;
            "
            role="img"
            height="16"
            width="16"
            aria-hidden="true"
            viewBox="0 0 16 16"
            data-encore-id="icon"
            class="Svg-sc-ytk21e-0 gQUQL fill-gray-200"
          >
            <path
              d="M1.69 2A4.582 4.582 0 0 1 8 2.023 4.583 4.583 0 0 1 11.88.817h.002a4.618 4.618 0 0 1 3.782 3.65v.003a4.543 4.543 0 0 1-1.011 3.84L9.35 14.629a1.765 1.765 0 0 1-2.093.464 1.762 1.762 0 0 1-.605-.463L1.348 8.309A4.582 4.582 0 0 1 1.689 2zm3.158.252A3.082 3.082 0 0 0 2.49 7.337l.005.005L7.8 13.664a.264.264 0 0 0 .311.069.262.262 0 0 0 .09-.069l5.312-6.33a3.043 3.043 0 0 0 .68-2.573 3.118 3.118 0 0 0-2.551-2.463 3.079 3.079 0 0 0-2.612.816l-.007.007a1.501 1.501 0 0 1-2.045 0l-.009-.008a3.082 3.082 0 0 0-2.121-.861z"
            ></path>
          </svg>
          <svg
            v-show="i.love == 1"
            v-on:click="counter.delete_song_love(i.name)"
            role="img"
            height="16"
            width="16"
            aria-hidden="true"
            viewBox="0 0 16 16"
            data-encore-id="icon"
            class="Svg-sc-ytk21e-0 gQUQL absolute fill-green-500"
          >
            <path
              d="M15.724 4.22A4.313 4.313 0 0 0 12.192.814a4.269 4.269 0 0 0-3.622 1.13.837.837 0 0 1-1.14 0 4.272 4.272 0 0 0-6.21 5.855l5.916 7.05a1.128 1.128 0 0 0 1.727 0l5.916-7.05a4.228 4.228 0 0 0 .945-3.577z"
            ></path>
          </svg>
        </div>
        <h1 class="w-[10%]">{{ i.duration }}</h1>
        <div class="w-[10%] cursor-pointer relative">
          <font-awesome-icon icon="fa-solid fa-ellipsis" />
        </div>
      </div>
    </div>

    <h1
      v-show="counter.Search_Song == ''"
      class="text-[20px] text-gray-200 font-bold my-5"
    >
      Duyệt tất cả
    </h1>
    <div
      v-show="counter.Search_Song == ''"
      class="grid sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4"
    >
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-rose-600 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Podcasts
        </h1>
        <img
          src="@/assets/1.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-lime-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Live Events
        </h1>
        <img
          src="@/assets/2.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-violet-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Fresh Finds
        </h1>
        <img
          src="@/assets/3.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-blue-900 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Made For You
        </h1>
        <img
          src="@/assets/4.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-green-900 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Pop
        </h1>
        <img
          src="@/assets/5.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-sky-400 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          GLOW
        </h1>
        <img
          src="@/assets/6.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-orange-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Hip-Hop
        </h1>
        <img
          src="@/assets/7.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-violet-300 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Charts
        </h1>
        <img
          src="@/assets/8.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-stone-300 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Workout
        </h1>
        <img
          src="@/assets/9.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-orange-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Summer
        </h1>
        <img
          src="@/assets/10.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-lime-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Travel
        </h1>
        <img
          src="@/assets/11.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-violet-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Gaming
        </h1>
        <img
          src="@/assets/12.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-stone-600 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Jazz
        </h1>
        <img
          src="@/assets/13.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-red-300 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Soul
        </h1>
        <img
          src="@/assets/14.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-red-600 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Love
        </h1>
        <img
          src="@/assets/15.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-cyan-700 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Party
        </h1>
        <img
          src="@/assets/16.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-pink-900 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          R&B
        </h1>
        <img
          src="@/assets/17.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-yellow-700 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Chill
        </h1>
        <img
          src="@/assets/18.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-violet-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Anime
        </h1>
        <img
          src="@/assets/19.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-cyan-400 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Instrumental
        </h1>
        <img
          src="@/assets/20.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
      <a
        class="flex justify-end items-end min-w-[173px] min-h-[173px] aspect-square rounded bg-fuchsia-500 overflow-hidden relative"
      >
        <h1
          class="absolute z-30 top-0 left-3 text-[22px] text-gray-200 font-bold my-5"
        >
          Sleep
        </h1>
        <img
          src="@/assets/21.jpg"
          class="w-[100px] h-[100px] lg:w-[120px] lg:h-[120px] rotate-12"
        />
      </a>
    </div>

    <!-- <h1 class="text-gray-200">{{ counter.Data_Search_Song.Data }}</h1> -->
  </div>
</template>
<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";
// import 'package:just_audio/just_audio.dart';

export default {
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {
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
  },
  components: {},
};
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 8px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #393636; /* M ủa thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #595857; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
  background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}
</style>
