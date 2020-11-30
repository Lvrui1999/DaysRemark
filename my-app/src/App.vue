<template>
  <v-app>
    <v-container>
      <p>123</p>
      <v-btn elevation="2" v-on:click="ss">
          <p>+1</p>     
      </v-btn>
      <v-content> {{val}} </v-content>
    </v-container>
    <bar>
    </bar>
  </v-app>
  
</template>

<script>
  import bar from './components/bar.vue'
  export default {
    data: () => ({ value: 'recent', val:1 }),
    methods:{
      ss:function(){
        this.val += 1
      }
    },
    components: { bar }
  }

</script>