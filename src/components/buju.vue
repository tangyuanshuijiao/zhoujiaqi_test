<template>
	<el-container>
	  <el-aside  width="200px">
		     <el-menu :default-openeds="['1', '3']">
		         <el-submenu index="1">
		           <template slot="title"><i class="el-icon-message"></i>导航一</template>
		           <el-menu-item-group>
		             <template slot="title">分组一</template>
		             <el-menu-item index="1-1" id="table" @click="go_table">table</el-menu-item>
		             <el-menu-item index="1-2" id="test" @click="go_test">test</el-menu-item>
		           </el-menu-item-group>
		           <el-menu-item-group title="分组2">
		             <el-menu-item index="1-3" id="home" @click="go_home">home</el-menu-item>
					 <el-menu-item index="1-4-1" id="head" @click="go_head">设置中心</el-menu-item>
		           </el-menu-item-group>
		           <el-submenu index="1-4">
		             <template slot="title" >选项4</template>
		             <el-menu-item index="1-4-1" @click="go_comment">评论区</el-menu-item>
		           </el-submenu>
		         </el-submenu>
		         <el-submenu index="2">
		           <template slot="title"><i class="el-icon-menu"></i>导航二</template>
		           <el-menu-item-group>
		             <template slot="title">分组一</template>
		             <el-menu-item index="2-1">选项1</el-menu-item>
		             <el-menu-item index="2-2">选项2</el-menu-item>
		           </el-menu-item-group>
		           <el-menu-item-group title="分组2">
		             <el-menu-item index="2-3">选项3</el-menu-item>
		           </el-menu-item-group>
		           <el-submenu index="2-4">
		             <template slot="title">选项4</template>
		             <el-menu-item index="2-4-1">选项4-1</el-menu-item>
		           </el-submenu>
		         </el-submenu>
		         <el-submenu index="3">
		           <template slot="title"><i class="el-icon-setting"></i>导航三</template>
		           <el-menu-item-group>
		             <template slot="title">分组一</template>
		             <el-menu-item index="3-1">选项1</el-menu-item>
		             <el-menu-item index="3-2">选项2</el-menu-item>
		           </el-menu-item-group>
		           <el-menu-item-group title="分组2">
		             <el-menu-item index="3-3">选项3</el-menu-item>
		           </el-menu-item-group>
		           <el-submenu index="3-4">
		             <template slot="title">选项4</template>
		             <el-menu-item index="3-4-1">选项4-1</el-menu-item>
		           </el-submenu>
		         </el-submenu>
		       </el-menu>
	  </el-aside >
	  <el-container>
	    <el-header>
			<el-dropdown>
			  <span class="el-dropdown-link">
			    个人中心<i class="el-icon-arrow-down el-icon--right"></i>
			  </span>
			  <el-dropdown-menu slot="dropdown">
			    <el-dropdown-item><a href="/">登录</a></el-dropdown-item>
			    <el-dropdown-item >
					退出登录</el-dropdown-item>
			    <el-dropdown-item >test</el-dropdown-item>
			  </el-dropdown-menu>
			</el-dropdown>
			<button @click="loginout">退出登录</button>
		</el-header>
	    <el-main>
			 <div class="container">
			            <keep-alive>
			                <router-view></router-view>
			            </keep-alive>
			        </div>
		</el-main>
	 <!--   <el-footer>Footer</el-footer> -->
	  </el-container>
	</el-container>
</template>


<style>
	.el-header {
	  background-color: #B3C0D1;
	  color: #333;
	  line-height: 60px;
	}
	
	.el-aside {
	  color: #333;
	}
</style>
<script>
	export default {
	  data() {
	    return {   
	    }
	  },
	  created() {
	  	this.public()
	  },
	  methods:{
		  go_login(){
			  this.$router.replace('/login')
		  },
		  go_table(){
			  this.$router.replace('/buju/table')
		  },
		  go_home(){
			  this.$router.replace('/buju/home')
		  },
		  go_test(){
			  this.$router.replace('/buju/test')
		  },
		  go_head(){
			  this.$router.replace('/buju/head')
		  },
		  go_comment(){
			  this.$router.replace('/buju/comment')
		  },
		  public(){
			 let token = window.localStorage.getItem('token')
			 this.$axios.post('/public',JSON.stringify({
				 'token':token
			 }),).then(
			 res =>{
				 console.log(res);
			 })
		  },
		  loginout(){
			  this.$axios.get('/login_out').then(
			 res =>{
				 console.log(res);
				 if(res.code == 200){
				  this.$router.replace('/')
				 localStorage.removeItem('token')
				  }
			 })
			
		  },
			  
		  }
		  
}
</script>