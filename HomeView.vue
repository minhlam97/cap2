<template>
  <div class="flex flex-col min-h-screen px-5 py-5 max-w-screen w-full gap-5">
    <div class="flex flex-col w-full gap-3">
      <div class="flex gap-1 text-bold items-center text-gray-200">
        <h1>Xin chào</h1>
        <h1 class="text-sky-600">{{ counter.Data_User.username }}</h1>
        <h1>, danh sách phát gần đây</h1>
      </div>
      <div id="cjss1" class="flex w-full items-center overflow-x-auto">
        <div
          v-for="(i, index) in counter.Get_late_song"
          :class="{ 'ml-[200px]': index > 0 }"
          class="flex text-gray-100 py-3 items-center"
        >
          <div
            v-on:click="
              Play_all();
              Get_data_song_1(i);
            "
            class="flex flex-col items-center gap-3 cursor-pointer"
          >
            <img :src="i.poster" class="min-w-[50px] h-[50px] rounded" />
            <h1 class="text-[16px]">{{ i.name }}</h1>
          </div>
        </div>
      </div>
    </div>
    <div class="flex min-h-full grow gap-5 overflow-auto">
      <div class="flex flex-col w-2/3">
        <div id="cjss" class="flex flex-col overflow-auto text-gray-200">
          <h1 class="text-[18px]">Bài hát dựa trên tâm trạng của bạn</h1>
          <div class="flex items-center gap-2 min-h-[50px]">
            <h1 class="text-[16px]">Danh sách bài hát</h1>
            <h1 class="text-blue-600 text-[18px] font-bold">
              {{ counter.Data_Feeling["Data"] }}
            </h1>
          </div>
          <div class="text-white h-full w-full flex flex-col">
            <div
              class="grid grid-cols-3 border-b-[1px] border-zinc-600 py-5 items-center font-bold"
            >
              <h1 class="flex w-[250px] ml-[50px]"></h1>
              <h1 class="flex w-[250px] ml-[50px]">Tên bài hát</h1>
              <h1>Nghệ sĩ</h1>
            </div>
            <div
              v-for="(i, index) in counter.Data_Feeling['List_Song']"
              v-on:click="
                Play_all();
                Get_data_song(i);
              "
              class="grid grid-cols-3 text-gray-300 border-b-[1px] border-zinc-600 items-center font-normal py-1 cursor-pointer"
            >
              <div class="flex gap-5 items-center">
                <h1>{{ index + 1 }}</h1>
                <img
                  :src="counter.domain_Backend + i.poster"
                  class="w-[50px] h-[50px] rounded"
                />
              </div>
              <h1 class="flex w-[250px] ml-[50px]">{{ i.name }}</h1>
              <h1>{{ i.artist }}</h1>
            </div>
          </div>
        </div>
      </div>
      <div
        class="w-1/3 flex flex-col items-center gap-5 h-full grow shrink-0 mt-[30px]"
      >
        <div class="flex relative">
          <video
            id="video"
            width="320"
            height="240"
            autoplay
            class="bg-red-600 absolute"
          ></video>
          <canvas id="canvas" width="320" height="240" class=""></canvas>
        </div>
        <button
          id="snap"
          v-on:click="
            Capture();
            counter.F_Search_Feeling();
          "
          class="bg-zinc-600 py-2 rounded w-[150px]"
        >
          Scan
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { useCounterStore } from "@/stores/counter";
import axios from "axios";
import VueCookies from "vue-cookies";
import { PhotoCapture, VideoCapture } from "vue-media-recorder";

export default {
  data() {
    return {
      canvas: null,
      context: null,
      video: null,
    };
  },

  methods: {},
  setup() {
    const counter = useCounterStore();
    return { counter };
  },
  mounted: function () {
    this.Play_Video();
    this.counter.get_song_play_list();
    this.counter.get_late_song();
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
      this.counter.Play_nhac.URL = this.counter.domain_Backend + i.mp3_file;
      this.counter.Play_nhac.Name_song = i.name;
      this.counter.Play_nhac.Name_artist = i.artist;
      this.counter.Play_nhac.Photo = this.counter.domain_Backend + i.poster;
      this.counter.Pause_Start = true;
    },
    Get_data_song_1(i) {
      this.counter.Play_nhac.URL = i.mp3_file;
      this.counter.Play_nhac.Name_song = i.name;
      this.counter.Play_nhac.Name_artist = i.artist;
      this.counter.Play_nhac.Photo = i.poster;
      this.counter.Pause_Start = true;
    },
    Play_Video() {
      var video = document.getElementById("video");

      // Get access to the camera!
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        // Not adding `{ audio: true }` since we only want video now
        navigator.mediaDevices
          .getUserMedia({ video: true })
          .then(function (stream) {
            //video.src = window.URL.createObjectURL(stream);
            video.srcObject = stream;
            video.play();
          });
      }
    },
    Capture() {
      this.canvas = document.getElementById("canvas");
      this.context = canvas.getContext("2d");
      this.video = document.getElementById("video");

      // Trigger photo take

      this.context.drawImage(this.video, 0, 0, 320, 240);
      this.counter.Image_Base64 = this.canvas.toDataURL();
      this.counter.Image_Base64 = this.counter.Image_Base64.split(
        "data:image/png;base64,"
      )[1];
    },
    async Filter_Feeling() {
      await Capture();
      this.counter.F_Search_Feeling();
    },
  },
  components: {
    PhotoCapture,
    VideoCapture,
  },
};
</script>

<style>
#cjss::-webkit-scrollbar {
  width: 5px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss::-webkit-scrollbar-track {
  background: #393636; /* Màu nền ngoài của thanh scrollbar */
}
#cjss::-webkit-scrollbar-thumb {
  background-color: #595857; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss::-webkit-scrollbar-thumb:hover {
  background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}

#cjss1::-webkit-scrollbar {
  width: 5px;
  height: 8px; /* Chiều rộng vùng chứa scrollbar */
}
#cjss1::-webkit-scrollbar-track {
  background: #393636; /* Màu nền ngoài của thanh scrollbar */
}
#cjss1::-webkit-scrollbar-thumb {
  background-color: #595857; /* Màu của thanh cuộn (scroll thumb) */
  border-radius: 5px; /* Bo góc scroll thumb */
  /* border: 2px solid #ccc;  Không hỗ trợ padding, margin, transition nên dùng viền cùng màu nên để padding scroll thumb */
}
#cjss1::-webkit-scrollbar-thumb:hover {
  background-color: #655f58; /* Hiệu ứng di chuột đổi màu*/
}

#video {
  transform: rotateY(180deg);
  -webkit-transform: rotateY(180deg); /* Safari and Chrome */
  -moz-transform: rotateY(180deg); /* Firefox */
}
</style>
