<template>
	<div>
		<el-table
		:data="tableData"
		stripe
		:cell-style="{ textAlign: 'center' }"
		:header-cell-style="{ textAlign: 'center' }"
		style="width: 100%"
		>
		<el-table-column
		label="ID"
		prop="id"
		sortable></el-table-column>
		<el-table-column
		label="姓名"
		prop="name"></el-table-column>
		<el-table-column
		label="密码"
		prop="password"></el-table-column>
		<el-table-column
		label="邮箱"
		prop="email"></el-table-column>
		<el-table-column
		label="性别"
		prop="sex"></el-table-column>
		<el-table-column
		label="创建时间"
		prop="c_time"></el-table-column>
		 <el-table-column 
		 align="right">
		  <template slot="header" slot-scope="scope">
		        <el-input
		          v-model="search"
		          size="mini"
		          placeholder="输入关键字搜索"/>
				  <el-button @click="commit" size="mini">搜索</el-button>
					 <el-button size="mini" @click="add">新增</el-button>
					 
		      </template>
		
		
			  
			    <template slot-scope="scope">
			          <el-button
			            size="mini"
						@click="edit(scope.$index, scope.row)"
			            >编辑</el-button>
					  <el-button
			            size="mini"
			            type="danger"
						@click="delete_user(scope.$index, scope.row)"
			           >删除</el-button>
			        </template>
		 </el-table-column>
		</el-table>
		<el-dialog
		:title="dialogTitle" :visible.sync="dialogTableVisible">
		<el-form :model="form">
			<el-form-item label="姓名":label-width='formLabelWidth'>
				<el-input v-model="form.name" placeholder="请输入姓名"></el-input>
			</el-form-item>
			<el-form-item label="邮箱":label-width='formLabelWidth'>
				<el-input v-model="form.email" placeholder="请输入邮箱"></el-input>
			</el-form-item>
			 <el-form-item label="选择性别" :label-width="formLabelWidth">
			      <el-select v-model="form.sex" placeholder="请选择性别">
			        <el-option label="男"value="男"></el-option>
			        <el-option label="女"value="女"></el-option>
			      </el-select>
			    </el-form-item>
		</el-form>
		 <div slot="footer" class="dialog-footer">
		    <el-button @click="dialogTableVisible=false">取 消</el-button>
		    <el-button type="primary" @click="chioce">确 定</el-button>
		  </div>
		</el-dialog>
		<!-- <el-pagination
		  @current-change = 'handleCurrentChange'
		  @size-change = 'handleSizeChange'
		  :page-size="pageSize"
		  :current-page="currentPage"
		  background
		  layout="prev, pager, next"
		   :total="300"
		 >
		</el-pagination> -->
	</div>
</template>

<script>
	export default{
		inject:['reload'],
		data(){
			return{
				tableData:[],
				form:{
					name:'',
					sex:'',
					email:''
				},
				currentPage :1,
				pageSize :10,
				dialogTitle: '',
				search : '',
				dialogTableVisible: false,
				// dialogFormVisible: false,
				 formLabelWidth: '120px'
			}
		},
		created() {
		    this.init()
		  },
		methods:{
			init(){
				this.$axios.get('/all_user',JSON.stringify({
						currentPage:this.currentPage
				}),).then(res => {
					console.log(res);
					this.tableData = res.data
				})
				// 其中this指当前vue实例
			},
			
			handleSizeChange(val) {
				this.pageSize = val;
			},
			handleCurrentChange(val) {
				this.currentPage = val;
				console.log(val)
				    this.init()
				
			},
			
			edit(index,row){
				// this.dialogFormVisible = true
				this.dialogTableVisible = true
				this.dialogTitle = '编辑记录'
				 this.form = JSON.parse(JSON.stringify(row))
					  
			},
			add(){
				this.dialogTableVisible = true
				this.dialogTitle = '新增记录'
				 this.form = {}
			},
			delete_user(index,row){
				console.log(row.id)
				// let id = JSON.parse(JSON.stringify(row)).id
				this.$axios.delete(`/delete_user?id=${id}`).then(res => {
				  if (res.code == 200) {
				    this.$notify.success({
				      title: '成功',
				      message: res.msg,
				      duration: 2000
				    })
					
				  } else {
				    this.$notify.error({
				      title: '失败',
				      message: res.msg,
				      duration: 2000
				    })
				  }
				  this.reload()
				})
			},
			commit(){
				console.log(this.search)
				this.$axios.post('/search',JSON.stringify({
				search:this.search
			}),
				
				).then(res =>{
					console.log(res)
					this.tableData = res.data
				} )
	
	        },
			
			chioce(){
				if(this.form.id){
					console.log(this.form.id)
					this.$axios.post('/update_user',this.form

					).then(
					res =>{
						console.log(res)
						this.tableData = res.data
						if (res.code =200){
							this.$notify.success({
							  message: res.msg
							})
						}
						else{
							this.$notify.error({
								message: res.msg
							})
						}
						this.reload()
					});
				}else{
					this.$axios.post('/add_user',this.form,
					
					).then(
					res =>{
						console.log(res)
						this.tableData = res.data
						if (res.code =200){
							this.$notify.success({
							  message: res.msg
							})
						}
						else{
							this.$notify.error({
								message: res.msg
							})
						}
						this.reload()
					}
					);
				}
			},
	     
         
			},
		    
		
		
	}
</script>

<style>
</style>