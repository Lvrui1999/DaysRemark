<template>
    <div>
        <v-container id="bar" fluid>
            <v-banner color = "white" id = "upper" elevation="5" height="100" width="500" @mousedown.native="drag1($event)" @touchdown.native="drag2($event)">
                <v-card-text class="noselect"> {{for_c}} </v-card-text>
            </v-banner>
            <v-card id = "lock" elevation="0" height="100" width="500" :color="cc"></v-card>
        </v-container>
    </div>
</template>
 
<script>
export default {
    data () {
        return {
            val:1,
            state : true,
            cc : 'red'
        }
    },
    methods :{
        drag1 : function(e){
            let odiv = e.currentTarget;
            let orileft = "0px";
            let disX = e.clientX;
            let ce = false
            document.onmousemove = (e)=>{ 
                let left = e.clientX - disX;    
                if(left > 0 && left < 120)
                odiv.style.left = left + 'px';
                if(left > 100 && !ce){
                    ce = true
                    if(this.state){
                        this.state = !this.state;
                        this.cc = 'success';
                    }
                    else{
                        this.state = !this.state;
                        this.cc = 'red'
                    }
                    //trans
                }
                
            };
            document.onmouseup = () => {
                document.onmousemove = null;
                document.onmouseup = null;
                odiv.style.left = orileft;
            };
        },
        drag2 : function(e){
            let odiv = e.currentTarget;
            let orileft = "0px";
            let disX = e.clientX;
            let ce = false
            document.ontouchmove = (e)=>{ 
                let left = e.clientX - disX;    
                if(left > 0 && left < 120)
                odiv.style.left = left + 'px';
                if(left > 100 && !ce){
                    ce = true
                    if(this.state){
                        this.state = !this.state;
                        this.cc = 'success';
                    }
                    else{
                        this.state = !this.state;
                        this.cc = 'red'
                    }
                    //trans
                }
                
            };
            document.ontouchup = () => {
                document.ontouchmove = null;
                document.ontouchup = null;
                odiv.style.left = orileft;
            };
        } 
    },
    props : ["for_c","top_plc","left_plc"]
}
</script>
 
<style>
    #bar{
        position: relative;
    }
    #upper{
        position: absolute;
        left: 0px;
        z-index: 2;
    }
    #lock{
        position: absolute;
        left: 0px;
        z-index: 1;
    }
    .noselect{
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
</style>