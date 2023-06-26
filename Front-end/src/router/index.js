import { createRouter, createWebHistory } from 'vue-router'
import Employees from '../components/Employees.vue'
import Edit from '../components/Edit.vue'
import NewEmployee from '../components/NewEmployee.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/danh-sach-nhan-vien',
      name: 'list',
      component: Employees
    },
    {
      path: '/chinh-sua-nhan-vien/:id',
      name: 'edit',
      component: Edit
    },
    {
      path: '/them-nhan-vien',
      name: 'add',
      component: NewEmployee
    },
    {
      path: '/home',
      name: 'home',
      component: Employees
    }
  ]
})

export default router
