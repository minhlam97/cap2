<template>
    <div>
        <div class="flex relative">
            <video id="video" width="320" height="240" autoplay class="bg-red-600 absolute"></video>
            <canvas id="canvas" width="320" height="240" class=""></canvas>
        </div>
        <button id="snap" v-on:click="Capture();">Snap Photo</button>
        <div class="mt-[15px] flex flex-col">
            <h1>{{ canvas }}</h1>
            <h1>{{ context }}</h1>
            <h1>{{ video }}</h1>
            <h1>{{ counter.Image_Base64 }}</h1>
        </div>
    </div>
</template>

<script>
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';
import VueCookies from 'vue-cookies'
import {PhotoCapture, VideoCapture} from 'vue-media-recorder'



export default {

    data(){
        return {
            canvas: null,
            context: null,
            video:null,
        }
    },
    setup() {

        const counter = useCounterStore();
        return { counter }
    },
    mounted: function () {
        this.Play_Video();
    },
    methods:{
        Play_Video(){
            var video = document.getElementById('video');

            // Get access to the camera!
            if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                // Not adding `{ audio: true }` since we only want video now
                navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
                    //video.src = window.URL.createObjectURL(stream);
                    video.srcObject = stream;
                    video.play();
                });
            }
        },
        Capture(){
            this.canvas = document.getElementById('canvas');
            this.context = canvas.getContext('2d');
            this.video = document.getElementById('video');

            // Trigger photo take
             
            this.context.drawImage(this.video, 0, 0, 320, 240);
            this.counter.Image_Base64 = this.canvas.toDataURL();
            
        }
    }
    ,
}
</script>