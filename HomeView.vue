<template>
  <div class="flex flex-col text-white h-full w-full gap-5">
    <div class="flex flex-col h-full w-full gap-3">
      <div class="flex gap-1 text-bold items-center">
        <h1>Xin chào</h1>
        <h1 class="text-sky-600">Lam97</h1>
        <h1>, nghe nhạc</h1>
      </div>
      <div class="flex fill-gray-300 justify-between h-full w-full">
        <svg
          role="img"
          height="16"
          width="16"
          aria-hidden="true"
          class="Svg-sc-ytk21e-0 kcBZLg IYDlXmBmmUKHveMzIPCF"
          viewBox="0 0 16 16"
          data-encore-id="icon"
        >
          <path
            d="M11.03.47a.75.75 0 0 1 0 1.06L4.56 8l6.47 6.47a.75.75 0 1 1-1.06 1.06L2.44 8 9.97.47a.75.75 0 0 1 1.06 0z"
          ></path>
        </svg>
        <h1>{{ counter.show_Ten_nhac }}</h1>
        <svg
          role="img"
          height="16"
          width="16"
          aria-hidden="true"
          class="Svg-sc-ytk21e-0 kcBZLg IYDlXmBmmUKHveMzIPCF"
          viewBox="0 0 16 16"
          data-encore-id="icon"
        >
          <path
            d="M4.97.47a.75.75 0 0 0 0 1.06L11.44 8l-6.47 6.47a.75.75 0 1 0 1.06 1.06L13.56 8 6.03.47a.75.75 0 0 0-1.06 0z"
          ></path>
        </svg>
      </div>
    </div>
    <div class="flex h-[500px] grow gap-5">
      <div id="cjss" class="w-2/3 flex flex-col overflow-auto">
        <h1 class="text-[18px]">Bài hát dựa trên tâm trạng của bạn</h1>
        <div class="flex items-center gap-2">
          <h1 class="text-[16px]">Danh sách bài hát</h1>
          <h1 class="text-blue-600 text-[18px] font-bold">
            {{ counter.Data_Feeling["Data"] }}
          </h1>
        </div>
        <div class="text-white h-full w-full flex flex-col">
          <div
            class="grid grid-cols-3 border-b-[1px] border-zinc-600 py-5 items-center font-bold"
          >
            <h1 class="flex w-[250px] ml-[50px]">STT</h1>
            <h1 class="flex w-[250px] ml-[50px]">Tên bài hát</h1>
            <h1>Nghệ sĩ</h1>
          </div>
          <div
            v-for="i in counter.Data_Feeling['List_Song']"
            v-on:click="
              counter.Play();
              Get_data_song(i);
            "
            class="grid grid-cols-3 text-gray-300 border-b-[1px] border-zinc-600 items-center font-normal py-1 cursor-pointer"
          >
            <img
              :src="counter.domain_Backend + i.poster"
              class="w-[100px] rounded"
            />
            <h1 class="flex w-[250px] ml-[50px]">{{ i.name }}</h1>
            <h1>{{ i.artist }}</h1>
          </div>
        </div>
      </div>
      <div
        class="w-1/3 flex flex-col items-center gap-5 h-full grow shrink-0 mt-[80px]"
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
  },
  methods: {
    Get_data_song(i) {
      this.counter.Play_nhac.URL = this.counter.domain_Backend + i.mp3_file;
      this.counter.Play_nhac.Name_song = i.name;
      this.counter.Play_nhac.Name_artist = i.artist;
      this.counter.Play_nhac.Photo = this.counter.domain_Backend + i.poster;
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
  width: 10px; /* Chiều rộng vùng chứa scrollbar */
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
</style>
