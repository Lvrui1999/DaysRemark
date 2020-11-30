<template>
  <div id="bar">
    <v-container>
        <v-banner elevation="5" width="500">
            <v-btn elevation="2" @click="ss" >
                <p>+1</p>     
            </v-btn>
            <v-content> {{val}} </v-content>
        </v-banner>
    </v-container>
  </div>
</template>
 
<script>
export default {
  data () {
    return {
        val:1
    }
  },
  methods :{
    ss : function(){
        this.val += 1
    }
  }
}
</script>
 
<style>
</style>