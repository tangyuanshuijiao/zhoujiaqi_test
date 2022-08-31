import Vue from 'vue'
import VueRouter from 'vue-router'
import buju from '../components/buju.vue'
import login from '../views/login.vue'
import register from '../views/register.vue'

Vue.use(VueRouter)

const routes = [
	{
		path :'/register',
		name:'register',
		 component: register
	},
	{
		path :'/',
		name:'login',
		 component: login
	},
  {
     path: '/buju',
	component : buju,
    name: 'Home',
	children:[{
			  path:'home',
			  component: () => import('@/views/Home.vue')
			  }]
    
  },
  {
    path: '/buju',
	component : buju,
    name: 'test',
	children:[{
			  path:'test',
			   component: () => import('@/views/Test.vue')
			  }]
  
  },
  {
    path: '/buju',
	component : buju,
    name: 'index',
	children:[{
			  path:'/',
			   component: () => import('@/views/index.vue')
			  }]
  },
  {
	  path: '/buju',
	  component : buju,
	  name : 'table',
	  children:[{
		  path:'table',
		  component: () => import('@/views/table.vue')
		  }]
	
  },
  {
  	  path: '/buju',
	  component : buju,
  	  name : 'head',
	  children:[{
	  		  path:'head',
	  		   component: () => import('@/views/buju.vue')
	  		  }]
  },
  {
  	  path: '/buju',
	  component : buju,
  	  name : 'comment',
	  children:[{
	  		  path:'comment',
	  		   component: () => import('@/views/comment.vue')
	  		  }]
  },

]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

 // 导航守卫
           // 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
            router.beforeEach((to, from, next) => { 
             if (to.path === '/' || to.path === '/register') {    next();  } 
             else {    let token = localStorage.getItem('token');    
             if (token === null || token === '')
             {      next('/');    } 
             else {      next();    }  
             }
});




export default router
