<script setup lang="ts">
import {Plus} from '@element-plus/icons-vue'
import {onMounted, ref} from 'vue'
import Dialog from '@/views/Dialog/Dialog.vue'
import {
  addConfigApi, checkVersionApi,
  type Config,
  deleteConfigApi,
  getConfigsApi,
} from '@/net/api/pgyer.ts'
import { ElMessage } from 'element-plus'
import qr from '@/assets/pgyer-manage-qr.png';
const addUserDialogVisible = ref(false)
const qrCodeVisible = ref(false)
const loading = ref(false)
const error = ref<string | null>(null)
const isSubmitting = ref(false)
const configs = ref<Config[]>([])
const newConfig = ref<Config>({
  config_id: 0,
  name: '',
  apikey: '',
  appkey: '',
})
const deletingId = ref<number | null>(null)
// 获取用户列表
const fetchConfigs = async () => {
  try {
    loading.value = true
    error.value = null
    const response = await getConfigsApi()
    configs.value = response.data
    for (const item of configs.value) {
      const version = await checkVersionApi({ _api_key: item.apikey, appKey: item.appkey })
      console.log('配置数据:', version) // 调试
      if (version.code == 0){
        item.buildBuildVersion = version.data.buildBuildVersion
        item.downloadURL = version.data.downloadURL
        item.buildVersion = version.data.buildVersion
        item.buildVersionNo = version.data.buildVersionNo
        item.buildUpdateDescription = version.data.buildUpdateDescription
        item.buildFileKey = version.data.buildFileKey
      }
    }
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
    const response = await addConfigApi(newConfig.value)
    if (response.code == 200) {
      addUserDialogVisible.value = false
      // 清空表单
      newConfig.value = { config_id: 0, name: '', apikey: '', appkey: '' }
      // 刷新列表
      await fetchConfigs()
    } else {
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
const deleteConfig = async (config_id: number) => {
  if (!confirm('确定要删除这个用户吗？')) return

  try {
    deletingId.value = config_id
    await deleteConfigApi(config_id)
    // 删除成功后更新本地数据
    configs.value = configs.value.filter((config) => config.config_id !== config_id)
  } catch (err) {
    error.value = '删除用户失败'
    console.error('Error deleting user:', err)
  } finally {
    deletingId.value = null
  }
}

const downloadFile = (url: string, fileName: string = "app.apk") => {
  const a = document.createElement("a");
  a.href = url;
  a.download = fileName; // 设置下载文件名
  a.style.display = "none";
  document.body.appendChild(a);
  a.click(); // 触发浏览器下载
  document.body.removeChild(a);
};
// 初始化加载数据
onMounted(() => {
  fetchConfigs()
})
</script>

<template>
  <button class="fixed-toggle" @click="addUserDialogVisible = true">
    <Plus />
  </button>
  <button class="fixed-toggle-secondary" @click="qrCodeVisible = true">
    <img :src="qr" alt="Logo" class="auto-shrink-img">
  </button>
  <Dialog v-if="qrCodeVisible" @click.self="qrCodeVisible = false">
    <img :src="qr" alt="Logo" class="auto-shrink-img-detail">
  </Dialog >
  <Dialog v-if="addUserDialogVisible" @click.self="addUserDialogVisible = false">
    <h2>添加新配置</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="name">应用名称</label>
        <input v-model="newConfig.name" type="text" id="name" required />
      </div>
      <div class="form-group">
        <label for="apikey">apikey</label>
        <input v-model="newConfig.apikey" type="text" id="apikey" required />
      </div>
      <div class="form-group">
        <label for="appkey">appkey</label>
        <input v-model="newConfig.appkey" type="text" id="appkey" required />
      </div>
      <button class="add-btn" type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? '提交中...' : '添加配置' }}
      </button>
    </form>
  </Dialog>

  <div class="user-management">
    <!-- 用户列表 -->
    <div class="user-list">
      <h2>配置列表</h2>
      <div v-if="loading" class="loading">加载中...</div>

      <!-- 空状态 -->
      <div v-else-if="configs.length === 0" class="empty-state">
        <img src="@/assets/empty.svg" alt="无数据" width="120" />
        <p>暂无用户数据</p>
        <button @click="fetchConfigs">刷新数据</button>
      </div>

      <!-- 用户列表 -->
      <ul v-else>
        <li v-for="config in configs" :key="config.config_id" class="user-item">
          <div class="user-info">
            <span class="name">{{ config.name }}</span>
            <span class="minor" v-if="config.buildBuildVersion != null && config.buildBuildVersion.trim() !== ''">蒲公英构建版本：{{ config.buildBuildVersion }}</span>
            <span class="minor" v-if="config.buildUpdateDescription != null && config.buildUpdateDescription.trim() !== ''">构建表述</span>
            <span class="detail" v-if="config.buildUpdateDescription != null && config.buildUpdateDescription.trim() !== ''">{{ config.buildUpdateDescription }}</span>
            <button class="add-btn" v-if="config.downloadURL != null && config.downloadURL.trim() !== ''" @click="downloadFile(config.downloadURL,config.buildFileKey ??'yuxinzhihui.apk')">
              下载
            </button>
          </div>

          <button
            @click="deleteConfig(config.config_id)"
            class="delete-btn"
            :disabled="deletingId === config.config_id"
          >
            {{ deletingId === config.config_id ? '删除中...' : '删除' }}
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.user-management {
  max-width: 800px;
  margin: 0 auto;
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
  width: 400px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.user-list {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.loading,
.empty-state {
  text-align: center;
  padding: 40px 0;
  color: #666;
}

.user-item {
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--decoration-border);
  background: var(--decoration-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px auto 0 auto;
  padding: 20px;
  border-bottom: 1px solid #eee;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.name {
  font-weight: bold;
}

.minor{
  color: var(--text-secondary);
  font-size: 0.95em;
  margin-top: 15px;
}

.detail {
  margin-left: 20px;
  color: var(--text-primary);
  font-size: 0.85em;
  margin-top: 4px;
  margin-bottom: 10px;
  background: var(--decoration-border) ;
}

.add-btn {
  margin-top: 10px;
  background: var(--secondary);
}

.delete-btn {
  background: var(--primary);
}
.empty-state img {
  margin-bottom: 15px;
}
.auto-shrink-img {
  width: 24px;       /* 设置目标宽度 */
  height: 24px;      /* 设置目标高度 */
  object-fit: contain; /* 保持比例，完整显示图片 */
}

.auto-shrink-img-detail{
  width: 200px;       /* 设置目标宽度 */
  height: 200px;      /* 设置目标高度 */
  object-fit: contain; /* 保持比例，完整显示图片 */
}
</style>
