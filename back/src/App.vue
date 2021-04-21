<template>
    <v-app>
        <v-container fluid v-if="not_login" style="margin: 0px; padding: 0px; width: 100%">
            <v-card flat>
                <v-col>
                    <v-alert
                    v-model="alert"
                    dismissible
                    type="warning"
                    outline
                    transition="scale-transition"
                    >
                    Wrong password or username!
                    </v-alert>
                    <v-alert
                    v-model="alert2"
                    dismissible
                    type="warning"
                    outline
                    transition="scale-transition"
                    >
                    Username has been used!
                    </v-alert>
                    <v-alert
                    v-model="alert3"
                    dismissible
                    type="warning"
                    outline
                    transition="scale-transition"
                    >
                    Username or password shouldn't be empty!
                    </v-alert>
                    <v-text-field label="Username"  v-model="uname">

                    </v-text-field>
                    <v-text-field label = "Password" type="password" v-model="pword">

                    </v-text-field>
                    <v-container >
                        <v-row style="justify-content: center">
                            <v-btn @mousedown="login" @touchdown="login">
                                <v-col>
                                    Login
                                </v-col>
                            </v-btn>
                            <v-btn @mousedown="regi" @touchdown="regi">
                                <v-col>
                                    Register
                                </v-col>
                            </v-btn>
                        </v-row>
                    </v-container>
                    
                </v-col>
            </v-card>
        </v-container>
        <v-container id = "a" align="start" fluid v-if="view" style="margin: 0px; padding: 0px; padding-top : 0px, height: 100% width: 100%">
            <v-row>
                <v-col>
                    <v-card
                    dark
                    flat
                    >
                    <v-btn
                        absolute
                        bottom
                        color="pink"
                        right
                        fab
                        @click="add_event"
                    >
                        <v-icon>mdi-plus</v-icon>
                    </v-btn>
                    <v-card-title class="pa-2 purple lighten-3">
                        <v-btn icon @click="er = true; view = false">
                        <v-icon>mdi-menu</v-icon>
                        </v-btn>
                        <h3 class="title font-weight-light text-center grow">
                        DaysMatter
                        </h3>
                    </v-card-title>
                    <v-img
                        src="https://cdn.vuetifyjs.com/images/cards/forest.jpg"
                        gradient="to top, rgba(0,0,0,.44), rgba(0,0,0,.44)"
                        height="300px"
                    >
                        <v-container class="fill-height" style="justify-content: center">
                        <v-row  align="center" >
                            <v-col justify="end" cols="4" >
                                <strong class="font-weight-regular mr-6">{{date}}</strong>
                                <div class="headline font-weight-light">
                                    {{date_week}}
                                </div>
                                <div class="text-uppercase font-weight-light">
                                    {{date_month}}
                                </div>
                            </v-col>
                            <v-col justify="end" >
                                
                            <!-- </v-row> -->
                            </v-col>
                        </v-row>
                        </v-container>
                    </v-img>
                    </v-card>
                    <v-timeline
                    align-top
                    dense
                     v-for="itemm in time_item" 
                     :key = itemm
                    >
                        <v-timeline-item
                            color="lime lighten-2"
                            small
                        >
                            <v-row class="pt-1">
                                <v-col cols="3">
                                    <strong>{{itemm[2]}}</strong>
                                </v-col>
                                <v-col>
                                    <strong>{{itemm[0]}}</strong>
                                    <div class="caption mb-2">
                                        {{itemm[1]}}
                                    </div>
                                    <!-- <v-avatar>
                                        <v-img
                                        src="https://avataaars.io/?avatarStyle=Circle&topType=LongHairFrida&accessoriesType=Kurt&hairColor=Red&facialHairType=BeardLight&facialHairColor=BrownDark&clotheType=GraphicShirt&clotheColor=Gray01&graphicType=Skull&eyeType=Wink&eyebrowType=RaisedExcitedNatural&mouthType=Disbelief&skinColor=Brown"
                                        ></v-img>
                                    </v-avatar> -->
                                </v-col>
                            </v-row>
                        </v-timeline-item>

                    </v-timeline>
                </v-col>
            </v-row>
        </v-container>
        <v-container v-else-if="!not_login" fluid>
            <v-card v-if="!er">
                <v-row style="justify-content: center">
                    <v-col>
                        <v-alert
                        v-model="alert4"
                        dismissible
                        type="warning"
                        outline
                        transition="scale-transition"
                        >
                        Please check the value you have input!
                        </v-alert>
                        <v-text-field label="Matter Title" v-model="m_t"></v-text-field>

                        <v-text-field label="Matter Content" v-model="m_c"></v-text-field>

                        <v-menu
                            ref="menu2"
                            v-model="menu"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            :return-value.sync="date1"
                            transition="scale-transition"
                            offset-y
                            lazy
                            full-width
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="date1"
                                label="Matter Date"
                                readonly
                                v-on="on"
                            ></v-text-field>
                            </template>
                            <v-date-picker v-model="date1" no-title scrollable>
                            <v-spacer></v-spacer>
                            <v-btn flat color="primary" @click="menu = false">Cancel</v-btn>
                            <v-btn flat color="primary" @click="$refs.menu2.save(date1);menu = false">OK</v-btn>
                            </v-date-picker>
                        </v-menu>

                        <v-menu
                            ref="menu1"
                            v-model="menu2"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            :return-value.sync="time"
                            lazy
                            transition="scale-transition"
                            offset-y
                            full-width
                            max-width="290px"
                            min-width="290px"
                        >
                            <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="time"
                                label="Matter Time"
                                readonly
                                v-on="on"
                            ></v-text-field>
                            </template>
                            <v-time-picker
                            v-if="menu2"
                            v-model="time"
                            full-width
                            >
                            <v-spacer></v-spacer>
                            <v-btn flat color="primary" @click="menu2 = false">Cancel</v-btn>
                            <v-btn flat color="primary" @click="$refs.menu1.save(time);menu2 = false">OK</v-btn>
                            </v-time-picker>
                        </v-menu>
                        <v-text-field label="length" v-model="length"></v-text-field>
                        <v-row style="justify-content: center">
                        <v-btn @click="add_eve"><v-col>ADD_EVENT</v-col></v-btn>
                        <v-btn @click="cancel_add_eve"><v-col>Cancel</v-col></v-btn>
                        </v-row>
                    </v-col>
                </v-row>
            </v-card>
            <v-card v-else>
                <v-toolbar color="light-blue" dark>
                <v-btn icon @click="er = false;view = true">
                    <v-icon>mdi-arrow-left</v-icon>
                </v-btn>
                <v-row style="justify-content: center">
                <v-toolbar-title>Delete</v-toolbar-title>
                </v-row>
                </v-toolbar>

                <v-list flat>
                <!-- <v-subheader>REPORTS</v-subheader> -->
                <v-list-item-group
                    v-model="selectedItem"
                    color="primary"
                >
                    <v-list-item
                    v-for="item in ttime_item"
                    :key="item"
                    @click="dele(item[3])"
                    >
                    <v-list-item-content v-if="item[0]">
                        <v-list-item-title v-text="item[0]"></v-list-item-title>
                    </v-list-item-content>
                    </v-list-item>
                </v-list-item-group>
                </v-list>
            </v-card>
        </v-container>
    </v-app>

</template>

<script>
    export default {
        data: () => ({ //前端所需诗数据
            value: 'recent', //vue所需参数
            uname : '', //用户名
            pword : '', //密码
            state : 0, //当前状态
            m_t : '', //标题
            m_c : '', //内容
            length : '', //期望持续事件
            not_login : true, //是否登录
            view : false, //是否为主界面
            date : "", //当前时间
            date_month : "", //当前年月
            date_week : "", //当前日期
            time_item : [], //时间列表
            ttime_item : [], //事件列表
            alert : false, //输出参数
            alert2 : false, //输出参数
            alert3 : false, //输出参数
            alert4 : false, //输出参数
            date1 : new Date().toISOString().substr(0, 10), //截止时间 （日期）
            time : '12:30', //截止时间（时分）
            menu2: false, //模块所需
            modal2: false, //模块所需
            menu: false,  //模块所需
            modal: false, //模块所需
            er : false //是否为删除
        }),
        created() { //websocket创建
            this.initWebSocket();
        },
        destroyed() { //websocket销毁
            this.websock.close()
        },
        mounted:function(){ //初始化钩子
            var _this = this;
            this.timer = setInterval(function(){   //一个线程事件用来维护页面上的时间
                let DD = new Date();
                _this.date = DD.getHours() + ':' + DD.getMinutes() + ':' + DD.getSeconds()
                _this.date_month = DD.getMonth() + " " + DD.getFullYear()
                _this.date_week = DD.getDate()
                _this.time_item[0] = ['','',_this.date];
            },1000);
        },
        methods:{
            dele(val){
                this.websock.send("del:"+this.uname+":"+val); //删除时间
            },
            initWebSocket(){ //初始化weosocket
                const wsuri = "ws://10.128.240.40:5678";
                this.websock = new WebSocket(wsuri);
                this.websock.onmessage = this.websocketonmessage;
                this.websock.onopen = this.websocketonopen;
                this.websock.onerror = this.websocketonerror;
                this.websock.onclose = this.websocketclose;
            },
            add_eve (){       //添加事件
                let n = parseInt(this.length);
                if(this.m_t.length != 0 && this.m_c.length != 0 && !isNaN(n)) //检查
                {    
                    this.ddl = this.date1 + '-' + this.time.replace(':','-') + '-0';
                // console.log(this.ddl);
                    this.websock.send("add:"+this.m_t+":"+this.m_c + ":" + this.ddl + ":" + this.length + ":" + this.uname);
                    this.view = true
                }
                else{
                    this.alert4 = true;
                }
            },
            cancel_add_eve (){ //取消
                this.view = true
            },
            add_event (){ //进入添加页面
                this.view = false;
            },
            check (){ //检查是否合法
                let vu = this.uname;
                let vp = this.pword;
                console.log(vu.length);
                console.log(vp.length);
                if(vu.length == 0 || vp.length == 0){
                    return true;
                }
                return false;
            },
            login (){ //登录
                if(this.check()){
                    this.alert3 = true;
                    this.alert2 = false
                    this.alert = false
                }
                else{
                    this.state = 1;
                    this.websock.send("log:"+this.uname+":"+this.pword);
                }
                
            },
            regi (){ //注册
                if(this.check()){
                    this.alert3 = true;
                    this.alert2 = false
                    this.alert = false
                }
                else{
                    this.state = 2;
                    this.websock.send("regi:"+this.uname+":"+this.pword);
                }
            },
            websocketonopen(){ //连接建立之后内容
                // let actions = {"test":"12345"};
                // this.websocketsend(JSON.stringify(actions));
            },
            websocketonerror(){//连接建立失败重连
                this.initWebSocket();
            },
            websocketonmessage(e){ //数据接收
                console.log(e.data)
                if(e.data[0] == 'c'){ //登录或注册成功
                    if(this.state == 2){
                        this.state = 4;
                        this.not_login = false;
                        this.view = true;
                        this.websocketsend("fetch:" + this.uname)
                    }
                    if(this.state == 1){
                        this.state = 3;
                        this.websocketsend("fetch:" + this.uname)
                    }
                }
                if(e.data[0] == 'f' && e.data[1] == 'b'){ //成功获取返回数据
                    if(this.state == 3){
                        this.state = 4;
                        this.not_login = false;
                        this.view = true;
                    }
                    let p = e.data;
                    let cc = p.split(";")
                    let x;
                    let c = 0;
                    this.time_item = [['','',this.date]];
                    this.ttime_item = [];
                    for (x in cc){
                        if(x == 0)continue;
                        let ce = cc[x];
                        let cec = ce.split(',')
                        this.time_item.push(cec)
                        c += 1;
                        cec.push(c)
                        this.ttime_item.push(cec)
                    }
                }
                if(e.data[0] == 's'){ //登录失败
                    this.alert = true
                    this.alert2 = false
                    this.alert3 = false
                }
                if(e.data[0] == 'f' && e.data[1] == 'a'){ //注册失败
                    this.alert2 = true
                    this.alert = false
                    this.alert3 = false
                }
            },
            websocketsend(Data){//数据发送
                this.websock.send(Data);
            },
            websocketclose(e){  //关闭
                console.log('断开连接',e);
            },
        },
    }

</script>

<style>
html,body,#app {
	height:100%;
}
</style>