<template>
  <div id="app">
 
   <router-view v-if="isRouterAlive"></router-view>
  

  </div>
</template>

<style>
/* 引入外部css */
@import "./assets/reset.css";

</style>
<script>
	export default{
		name:'app',
		provide(){
			return{
				reload:this.reload
			}
		},
		data(){
			return{
				isRouterAlive :true
			}
		},
		methods:{
			reload(){
				this.isRouterAlive = false
				this.$nextTick(function(){
					this.isRouterAlive = true
				})
			}
		}
	}
</script>
