<template>
  <button class="fixed-toggle" @click="visible = true">
    <Plus />
  </button>
  <!-- 添加用户表单 -->
  <Dialog v-if="visible" @click.self="visible = false">
    <h2>添加用户</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">名字(用以区分是谁的账号)</label>
        <input v-model="newUser.name" type="text" id="name" required>
      </div>
      <div class="form-group">
        <label for="username">账号</label>
        <input v-model="newUser.username" type="text" id="username" required>
      </div>
      <div class="form-group">
        <label for="password">密码</label>
        <input v-model="newUser.password" type="password" id="password" required>
      </div>
      <button class="add-btn" type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? '提交中...' : '添加用户' }}
      </button>
    </form>
  </Dialog>

  <div  class="user-management">
    <!-- 用户列表 -->
    <div class="user-list">
      <h2>用户列表</h2>
      <div v-if="loading" class="loading">加载中...</div>

      <!-- 空状态 -->
      <div v-else-if="users.length === 0" class="empty-state">
        <img src="@/assets/empty.svg" alt="无数据" width="120">
        <p>暂无用户数据</p>
        <button @click="fetchUsers">刷新数据</button>
      </div>

      <!-- 用户列表 -->
      <ul v-else>
        <li v-for="user in users" :key="user.user_id" class="user-item">
          <div class="user-info">
            <span class="name">{{ user.name }}</span>
            <span class="username">@{{ user.username }}</span>
          </div>
          <button
            @click="deleteUser(user.user_id)"
            class="delete-btn"
            :disabled="deletingId === user.user_id"
          >
            {{ deletingId === user.user_id ? '删除中...' : '删除' }}
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import {Plus} from "@element-plus/icons-vue";
import {type User, getUsersApi, addUserApi, deleteUserApi} from '@/net/api/yuxin'
import Dialog from "@/views/Dialog/Dialog.vue";
import { ElMessage } from 'element-plus'

//添加用户弹窗的状态
const visible = ref(false)
// 用户列表数据
const users = ref<User[]>([])
const loading = ref(false)
const error = ref<string | null>(null)


// 添加用户表单
const newUser = ref<User>({
  user_id: 0,
  name: '',
  username: '',
  password: ''
})

const isSubmitting = ref(false)

// 删除状态
const deletingId = ref<number | null>(null)


// 获取用户列表
const fetchUsers = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await getUsersApi()
    users.value = response.data
  } catch (err) {
    error.value = '获取用户列表失败'
    console.error('Error fetching users:', err)
  } finally {
    loading.value = false
  }
}

// 添加用户
const handleSubmit = async () => {
  try {
    isSubmitting.value = true
    const response = await addUserApi(newUser.value)
    if (response.code == 200){
      visible.value = false
      // 清空表单
      newUser.value = { user_id: 0,name: '', username: '', password: '' }
      // 刷新列表
      await fetchUsers()
    }else{
      ElMessage.error(response.message)
    }

  } catch (err) {
    console.error('Error Add User:', err)
    error.value = '添加用户失败'
  } finally {
    isSubmitting.value = false
  }
}

// 删除用户
const deleteUser = async (user_id: number) => {
  if (!confirm('确定要删除这个用户吗？')) return

  try {
    deletingId.value = user_id
    await deleteUserApi(user_id)
    // 删除成功后更新本地数据
    users.value = users.value.filter(user => user.user_id !== user_id)
  } catch (err) {
    error.value = '删除用户失败'
    console.error('Error deleting user:', err)
  } finally {
    deletingId.value = null
  }
}

// 初始化加载数据
onMounted(() => {
  fetchUsers()
})
</script>


<style scoped>
h3 {
  font-size: 1.2rem;
  margin-top: 1rem;
  color: var(--text-primary);
}

.user-management {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 300px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

@media (max-width: 768px) {
  input {
    max-width: 80vw
  }
}


.user-list {
  background: var(--decoration-border);;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.loading, .empty-state {
  text-align: center;
  padding: 40px 0;
  color: #666;
}

.user-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 0;
  border-bottom: 1px solid #eee;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.name {
  font-weight: bold;
}

.username {
  color: var(--text-secondary);
  font-size: 0.9em;
}

.add-btn {
  background: var(--secondary);
}

.delete-btn {
  background: var(--primary);
}

.empty-state img {
  margin-bottom: 15px;
}

</style>
