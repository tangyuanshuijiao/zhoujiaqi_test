<template>
<div>
  <!-- 循环获取列表 -->
  <p>books:</p>
  <ol>
	<li v-for="book in books">
      {{ book }}
   </li>
  </ol>
  
  <!-- 点击事件 -->
  <button @click="increment" id="test1">{{ count }}</button>
  <buttonconunter></buttonconunter>
  <buttonconunter v-bind:"post"></buttonconunter>
  <buttonconunter title="看我看我"></buttonconunter>
  
  <!-- 直接在大括号中调用message方法 -->
  <p>{{ message() }}</p>
  <!-- 测试计算属性和方法的区别,感觉就是更不更新的问题，不是响应式依赖 -->
  <p>{{ now() }}</p>
  <!-- 调用字典里的方法 -->
  <ul>
	  <li v-for="(value,key,index) in myobject">
		 {{ key }}:{{ value }}:{{ index }}
	  </li>
  </ul>
  <!-- 弹窗 -->
  <button @click="say('放宽心')">弹窗按钮</button>
  <!-- 键盘按键,回车键执行提交 -->
  <input @keyup.enter = 'submit'/>
  <!-- v-model的使用，绑定数据来源 它将始终将当前绑定的 JavaScript 状态视为数据的正确来源-->
  <p>Message is :{{ message_1 }}</p>
  <input v-model = 'message_1' placeholder="编辑文本"/>
  </br>
  <!-- 怎么实现自动刷新？ -->
  <span>Multiline message is:</span>
  <p style="white-space: pre-line;">{{ message_2 }}</p>
  <textarea v-model="message_2" placeholder="add multiple lines"></textarea>
  <!-- 复选框 为什么能实现自动添加至列表中-->
	<div>Checked names: {{ checkedNames }}</div>
	<!-- label表示input的标题，和input进行绑定通过id， input框绑定了v-model，那么就可以获取到input框中的值-->
	<input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
	<label for="jack">Jack</label>
	
	<input type="checkbox" id="john" value="John" v-model="checkedNames">
	<label for="john">John</label>
	
	<input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
	<label for="mike">Mike</label>
	</br>
	<!-- 选择器 -->
	<select v-model="selected">
		<option v-for="option in options" :value="option.value">
			{{ option.text }}
		</option>
	</select>
	<div>Selected:{{ selected }}</div> 
	<button @click="refresh">刷新按钮</button>
	<el-form
	  :model="userform"
	  status-icon
	  ref="form"
	  label-width="60px"
	>
	  <el-form-item label="用户名" prop="name">
	    <el-input v-model="userform.name" autocomplete="off" />
	  </el-form-item>
	  <el-form-item label="密码" prop="password">
	   <el-input v-model="userform.password" autocomplete="off" />
	  </el-form-item>
	</el-form>
	<span slot="footer" class="dialog-footer">
	  <el-button @click="check">重置</el-button>
	  <el-button type="primary" @click="check_form">确 定</el-button>
	</span>
	

</div>
  </template>
  
<script>
	import buttonconunter from '../components/buttoncounter.vue'
	
export default {
	inject:['reload'],
	components:{
		buttonconunter
	},
	// components: 局部注册，局部注册的组件在后代组件中并不可用
  data(){
    return{
      count : 1,
	  message_1 : '',
	  message_2 : '',
	  userform : {
		  'name':'',
		  'password':''
	  },
	  selected :'',
	  checkedNames: [],
	  books : [
		  "第一本书",
		  "第二本书",
		  "第三本书"
	  ],
	  options :[
		  {text :'one',value:'A'},
		  {text :'two',value:'B'},
		  {text :'three',value:'C'}
	  ],
	  myobject : {
		title : 132,
		author : "周树人",
		time : `${this.now()}`  
	  },

	 
    }
  },
  methods:{
	  
    increment(){
      this.count++
    },
	
	message(){
		return this.books
	},
    now(){
  	return new Date(Date.now())
  },
    say(something){
		alert(something);
	},
	refresh(){
		this.reload()
		
	},	
	check_form(){
		 console.log(this.userform)
	},
	
	check(){    console.log(this.userform)
				this.$axios.post('/login',this.userform,JSON.stringify({
					name:this.userform.name,
					password:this.userform.password
	
				}),{
	    headers: {
	        'Content-Type':'application/json',
			'Access-Control-Allow-Origin':'*'
	    }
	}).then(res =>{
		   console.log(res)
		   
		   
	
	})
			},
	},
	mounted() {
		console.log("打印日志")
	}
  }

</script>