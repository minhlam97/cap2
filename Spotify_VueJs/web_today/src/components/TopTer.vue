<template>
  <div
    :class="{
      'justify-between': counter.Path_Route.path == '/Search',
      'justify-end bg-[#5038A0]': counter.Path_Route.path == '/Love-Song',
      'justify-end bg-sky-500': counter.Path_Route.path == '/Play-list',
    }"
    class="flex bg-[#121212] w-full h-[64px] text-white justify-end items-center pl-[260px] pr-5"
  >
    <div
      v-show="counter.Path_Route.path == '/Search'"
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
        placeholder="Bạn muốn nghe gì ?"
        @keyup.enter="counter.F_Search_Song()"
        class="w-full outline-none text-gray-600"
        v-model="counter.Search_Song"
      />
    </div>
    <body class="antialiased">
      <div class="bg-back rounded-full group inline-block relative">
        <!-- bg-black rounded-full flex pl-1 pr-3 py-1 gap-1 -->
        <button class="py-2 px-4 rounded inline-flex items-center">
          <img
            class="flex items-center justify-center w-[28px] h-[28px] rounded-full bg-[#535353]"
            src="@/assets/vn.png"
          />
          <h1 class="text-white pl-1">VI</h1>
          <!-- <h1 class="text-white">VI</h1> -->

          <svg
            class="fill-current h-4 w-4"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
          ></svg>
        </button>
        <ul class="absolute hidden text-gray-700 pt-1 group-hover:block">
          <li class="">
            <a
              class="rounded-t bg-gray-200 hover:bg-gray-400 py-2 px-4 block whitespace-no-wrap"
              href="#"
              >VI</a
            >
          </li>
          <li class="">
            <a
              class="bg-gray-200 hover:bg-gray-400 py-2 px-4 block whitespace-no-wrap"
              href="#"
              >EN</a
            >
          </li>
        </ul>
      </div>
    </body>

    <div class="bg-black rounded-full flex pl-1 pr-3 py-1 gap-1">
      <div
        class="flex items-center justify-center w-[28px] h-[28px] rounded-full bg-[#535353]"
      >
        <svg
          role="img"
          height="16"
          width="16"
          aria-hidden="true"
          viewBox="0 0 16 16"
          data-encore-id="icon"
          class="fill-gray-300 Svg-sc-ytk21e-0 uPxdw"
        >
          <path
            d="M6.233.371a4.388 4.388 0 0 1 5.002 1.052c.421.459.713.992.904 1.554.143.421.263 1.173.22 1.894-.078 1.322-.638 2.408-1.399 3.316l-.127.152a.75.75 0 0 0 .201 1.13l2.209 1.275a4.75 4.75 0 0 1 2.375 4.114V16H.382v-1.143a4.75 4.75 0 0 1 2.375-4.113l2.209-1.275a.75.75 0 0 0 .201-1.13l-.126-.152c-.761-.908-1.322-1.994-1.4-3.316-.043-.721.077-1.473.22-1.894a4.346 4.346 0 0 1 .904-1.554c.411-.448.91-.807 1.468-1.052zM8 1.5a2.888 2.888 0 0 0-2.13.937 2.85 2.85 0 0 0-.588 1.022c-.077.226-.175.783-.143 1.323.054.921.44 1.712 1.051 2.442l.002.001.127.153a2.25 2.25 0 0 1-.603 3.39l-2.209 1.275A3.25 3.25 0 0 0 1.902 14.5h12.196a3.25 3.25 0 0 0-1.605-2.457l-2.209-1.275a2.25 2.25 0 0 1-.603-3.39l.127-.153.002-.001c.612-.73.997-1.52 1.052-2.442.032-.54-.067-1.097-.144-1.323a2.85 2.85 0 0 0-.588-1.022A2.888 2.888 0 0 0 8 1.5z"
          ></path>
        </svg>
      </div>

      <h1 class="text-white">{{ counter.Data_User.username }}</h1>
      <router-link
        to="/"
        v-on:click="counter.Show_Table_Login = 0"
        class="flex items-center justify-center px-2 ml-2 border-l-[1px] border-zinc-700 cursor-pointer"
        ><font-awesome-icon
          icon="fa-solid fa-right-to-bracket"
          class="text-white"
      /></router-link>
    </div>

    <!-- <h1>{{ counter.Show_Table_Login }}</h1> -->
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
    // src="https://cse.google.com/cse.js?cx=55c97eef5881f4231"
  },
};
</script>
