<template>
	<div>
	  <button @click="count++" id="test1">{{ count }}</button>
	    <h1>{{ title }}</h1>
		<h2>{{ post }}</h2>
	</div>
</template>

<script>
	export default{
		data(){
			return{
				count : 1,
				post:{
					id :1,
					name : 'zhou'
				}
			}
		},
		props:['title']
	}
</script>

<style>
</style>