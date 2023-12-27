import { defineStore } from "pinia";

import axios from "axios";
import VueCookies from "vue-cookies";
import { fa0 } from "@fortawesome/free-solid-svg-icons";

import { useRoute } from "vue-router";
const Route = useRoute();

export const useCounterStore = defineStore("counter", {
  state: () => {
    return {
      domain_Backend: "http://127.0.0.1:8000",
      domain_Frontend: "",
      Path_Route: useRoute(),

      Show_Table_Login: 0,
      Login_SignUp: 1,
      Login: { username: "", password: "" },
      Search_Song: "",
      Data_Search_Song: {
        Data: "",
        Notification: "",
        Number: "",
        Tk_Search: "",
      },
      Image_Base64: "",
      Data_Feeling: "",
      Play_nhac: { URL: "", Name_song: "", Name_artist: "", Photo: "", Tim: 0 },
      show_Nhac: 0,
      show_Ten_nhac: "",
      Data_User: "",
      username: "",
      password: "",
      Set_User: "",
      username_dk: "",
      password_dk: "",
      email_dk: "",
      Set_song_love: "",
      Get_song_love: "",
      Get_song_play_list: "",
      Show_delete: 0,
      Delete_play_list: "",
      name_delete_play_list: "",
      show_tim: 0,
      show_bang_DSP: "",
      Add_song_play_list: "",
      show_bang_DSPN: "",
      name_show_bang_DSPN: "",
      Get_late_song: [{ poster: "", name: "" }],
      Add_late_song: "",
      Show_deletete: "",
      Delete_song_play_list: "",
      pk: "",
      duration_mp3: "",
      current_mp3: "",
      isPublished: true,
      isPaused: true,
      isMuted: false,
      //   url: "https://dkihjuum4jcjr.cloudfront.net/ES_ITUNES/Shake%20It%20Up/ES_Shake%20It%20Up.mp3",
      audioo: null,
      progress: 0,
      current: "0:00",
      length: "",
      volume: 100,
      message: "Welcome to Vue!",
      am_luong: "",
      do_dai: "",
      loop_ms: false,
      dao_ms: false,
      Show_bang_DKTC: { tb: 0, tc: 0 },
      Show_bang_DNTC: 1,
      name_PLL: "MOODIFY",
      Show_bang_DT: 1,
      st: 0,
      hhhh: 100,
    };
  },

  getters: {
    // cookievalue: (state) => state.openthongtincanhan.token + "(Theta)" + state.openthongtincanhan.id,
  },

  actions: {
    //  {
    //   this.audioo = new Audio(this.counter.Play_nhac.URL);
    //   this.audioo.addEventListener("loadeddata", () => {
    //     this.length = this.getTimeCodeFromNum(this.audioo.duration);
    //     this.audioo.volume = 1;
    //   },
    //     false
    //   );
    // }
    // ,
    async Play() {
      var audio = document.getElementById("nhac");
      audio.load();
      audio.play();
      // this.duration_mp3 = audio.duration;
    },
    async get_song_love() {
      this.Get_song_love = await axios({
        method: "get",
        url: this.domain_Backend + "/get_song_love",
      });
      this.Get_song_love = await this.Get_song_love.data.data;
    },
    async delete_song_love(i) {
      this.Delete_song_love = await axios({
        method: "post",
        data: { name: i },
        url: this.domain_Backend + "/delete_song_love",
      });
      this.Delete_song_love = await this.Delete_song_love.data;
      this.get_song_love();
    },
    async set_play_list() {
      this.Set_play_list = await axios({
        method: "post",
        data: { name: this.name_PLL, name_user: this.Data_User.username },
        url: this.domain_Backend + "/set_play_list",
      });
      this.Set_play_list = await this.Set_play_list.data;
    },
    async delete_play_list() {
      this.Delete_play_list = await axios({
        method: "post",
        data: {
          name: this.name_delete_play_list,
          name_user: this.Data_User.username,
        },
        url: this.domain_Backend + "/delete_play_list",
      });
      this.Delete_play_list = await this.Delete_play_list.data;
    },
    async get_song_play_list() {
      this.Get_song_play_list = await axios({
        method: "post",
        data: { name_user: this.Data_User.username },
        url: this.domain_Backend + "/get_song_play_list",
      });
      this.Get_song_play_list = await this.Get_song_play_list.data;
    },
    async add_song_play_list(
      name,
      artist,
      duration,
      poster,
      mp3_file,
      id_Song,
      Play_list_Link
    ) {
      this.Add_song_play_list = await axios({
        method: "post",
        data: {
          name: name,
          artist: artist,
          duration: duration,
          poster: poster,
          mp3_file: mp3_file,
          id_Song: id_Song,
          Play_list_Link: Play_list_Link,
        },
        url: this.domain_Backend + "/add_song_play_list",
      });
      this.Add_song_play_list = await this.Add_song_play_list.data;
      this.get_song_play_list();
    },
    async delete_song_play_list() {
      this.Delete_song_play_list = await axios({
        method: "post",
        data: { pk: this.pk },
        url: this.domain_Backend + "/delete_song_play_list",
      });
      this.Delete_song_play_list = await this.Delete_song_play_list.data;
    },
    async get_late_song() {
      this.Get_late_song = await axios({
        method: "get",
        url: this.domain_Backend + "/get_late_song",
      });
      this.Get_late_song = await this.Get_late_song.data.data;
    },
    async add_late_song(
      name,
      artist,
      duration,
      poster,
      mp3_file,
      id_Song,
      User_Link
    ) {
      this.Add_late_song = await axios({
        method: "post",
        data: {
          name: name,
          artist: artist,
          duration: duration,
          poster: poster,
          mp3_file: mp3_file,
          id_Song: id_Song,
          User_Link: User_Link,
        },
        url: this.domain_Backend + "/add_late_song",
      });
      this.Add_late_song = await this.Add_late_song.data;
    },
    async F_Search_Song() {
      this.Data_Search_Song.Data = await axios({
        method: "get",
        params: { search: this.Search_Song },
        url: this.domain_Backend + "/api/search_song",
      });
      this.Data_Search_Song.Data = this.Data_Search_Song.Data.data;
      await this.get_song_love();
      for (let i = 0; i < this.Get_song_love.length; i++) {
        let user = this.Data_Search_Song.Data.findIndex(
          (item) => item.id == this.Get_song_love[i].id_Song
        );
        this.Data_Search_Song.Data[user].love = 1;
      }
      if (this.Data_Search_Song.Data.length > 0 && this.Search_Song != "") {
        this.Data_Search_Song.Notification =
          "Danh sách bài hát được tìm kiếm với từ khóa";
        this.Data_Search_Song.Number = 2;
        this.Data_Search_Song.Tk_Search = this.Search_Song;
      } else {
        this.Data_Search_Song.Notification =
          "Không có bài hát nào được tìm kiếm với từ khóa";
        this.Data_Search_Song.Number = 1;
        this.Data_Search_Song.Tk_Search = this.Search_Song;
      }
    },
    async F_Search_Feeling() {
      this.Data_Feeling = await axios({
        method: "post",
        data: { Image_Base64: this.Image_Base64 },
        url: this.domain_Backend + "/Scan_Feeling",
      });
      this.Data_Feeling = await this.Data_Feeling.data;
    },
    async Get_Data_User() {
      try {
        this.Data_User = await axios({
          method: "post",
          data: { username: this.username, password: this.password },
          url: this.domain_Backend + "/login_api",
        });
        this.Data_User = await this.Data_User.data;

        this.Show_Table_Login = 1;

        this.username = "";
        this.password = "";
      } catch (error) {
        this.Show_bang_DNTC = 2;
      }
    },
    async Set_Data_User() {
      try {
        this.Set_User = await axios({
          method: "post",
          data: {
            username_dk: this.username_dk,
            password_dk: this.password_dk,
            email_dk: this.email_dk,
          },
          url: this.domain_Backend + "/sign_api",
        });
        this.Set_User = await this.Set_User.data;

        this.username_dk = "";
        this.password_dk = "";
        this.email_dk = "";

        // if (this.Set_User['Signup information'] == 'Signup in successfully !') {
        this.Show_bang_DKTC.tc = 1;
        // }
      } catch (error) {
        this.Show_bang_DKTC.tc = 2;
      }
    },
    async add_song_love(
      name,
      artist,
      duration,
      poster,
      mp3_file,
      id_Song,
      User_Link
    ) {
      this.Set_song_love = await axios({
        method: "post",
        data: {
          name: name,
          artist: artist,
          duration: duration,
          poster: poster,
          mp3_file: mp3_file,
          id_Song: id_Song,
          User_Link: User_Link,
        },
        url: this.domain_Backend + "/add_song_love",
      });
      this.Set_song_love = await this.Set_song_love.data;
    },
  },
});
