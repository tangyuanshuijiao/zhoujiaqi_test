<template>
<el-card class="el-card-d" shadow="always">
             <div class="infinite-list-wrapper" style="overflow:auto;">
                <el-timeline
                  infinite-scroll-disabled="disabled">
                <div v-if="allmessages.length>0"> 
                  <el-timeline-item v-for="(item,index) in allmessages"  :key="index" :timestamp='item.createTime' placement="top">
                    <el-card class="el-card-m" style="height:120px">
                      <h4>{{item.name}}：</h4>
                      <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{item.context}}</p>
                    </el-card>
                  </el-timeline-item>
                </div>
				
                <div v-else>
                   <el-timeline-item placement="top">
                    <el-card class="el-card-m" style="height:120px">
                      <h4>大黄子：</h4>
                      <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 说点什么吧😁</p>
                    </el-card>
                  </el-timeline-item>
                </div>
              </el-timeline> 
              </div>
              <div class="el-card-messages">
                 <el-input type="textarea" :rows="5" placeholder="输入留言" maxlength="200" v-model="message"></el-input>
                 <el-button type="info" round class="submit-message" @click="submitMessage">留言</el-button>
              </div>
            </el-card>


</template>
<script>
	export default {
		 inject:['reload'],
	    data() {
	      return {
			allmessages:'',
			message:'',
	      }
	    },
		created() {
			this.allmsg()
		},
	    methods: {
			allmsg(){
				this.$axios.post('/all_msg').then(res =>{
				console.log(res)
				this.allmessages = res.data })
			},
			
	  		init(){
				this.$axios.post('/add_blog',{
				message:this.message,
				}
				).then(res =>{
					console.log(this.message)
					this.reload()
		            console.log(res)
		  
	   })
			},
			submitMessage(){
			      if(this.message=='' || this.message.replace(/(^\s*)|(\s*$)/g, "")==""){
			          this.$message('写点啥提交也行呀');
			          return;
			      // 前端点击提交后，反向解码token，先获取当前用户name值，将name值一起传给add_blog接口
				  
				  }else{
		      this.init()   }
	        },
	  }
	  }
	  
      
</script>
<style>
	 .infinite-list-wrapper{
	      width: 100%;
	      height: 500px;
	    }
	    .submit-message{
	        width: 100%; 
	        background: rgb(235, 245, 247);
	        color: cadetblue;
	        letter-spacing:20px;
	    }
	 @media screen and (max-width: 3000px) and (min-width: 767px) {
	    .el-card-d{
	      float: left;
	     /* margin-top: 20px; */
	     margin-left: 10%;
	      width: 80%;
	      height: 100%;
	    }
	
	   }
	  /*
	  屏幕小于768px的
	  */
	  @media screen and (max-width:768px) and (min-width: 100px){  
	     .el-card-d{
	
	      width: 100%;
	      height: 100%;
	    }
	  }

</style>