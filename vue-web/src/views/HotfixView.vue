<template>
  <div class="upload-container">
    <h2>热修复包上传</h2>
    <el-form
      ref="uploadForm"
      :model="form"
      :rules="rules"
      label-width="120px"
      class="upload-form"
      @submit.prevent="submitUpload"
    >
      <el-form-item label="版本号" prop="version">
        <el-input
          v-model="form.version"
          placeholder="例如：v1.0.1"
          clearable
        />
      </el-form-item>

      <el-form-item label="版本描述" prop="describe">
        <el-input
          v-model="form.describe"
          type="textarea"
          :rows="3"
          placeholder="请描述本次热修复的内容"
          maxlength="200"
          show-word-limit
        />
      </el-form-item>

      <el-form-item label="热修复文件" prop="file">
        <el-upload
          ref="uploadRef"
          class="upload-demo"
          drag
          :auto-upload="false"
          :on-change="handleFileChange"
          :file-list="fileList"
          :limit="1"
          accept=".zip,.rar,.7z,.png,.apk"
          :show-file-list="true"
        >
          <el-icon class="el-icon--upload"><upload-filled /></el-icon>
          <div class="el-upload__text">
            将文件拖到此处，或<em>点击上传</em><br>
            <span class="el-upload__tip">支持ZIP/RAR/7Z格式，大小不超过100MB</span>
          </div>
        </el-upload>
      </el-form-item>

      <el-form-item>
        <el-button
          type="primary"
          :loading="uploading"
          @click="submitUpload"
        >
          提交上传
        </el-button>
        <el-button @click="resetForm">重置</el-button>
      </el-form-item>
    </el-form>

    <!-- 上传结果展示 -->
    <el-dialog
      v-model="resultDialogVisible"
      title="上传结果"
      width="30%"
      center
    >
      <div v-if="uploadSuccess" class="success-result">
        <el-icon class="success-icon"><check /></el-icon>
        <h3>上传成功！</h3>
        <div class="result-details">
          <p><strong>文件名：</strong>{{ resultData.filename }}</p>
          <p><strong>文件大小：</strong>{{ formatFileSize(resultData.size) }}</p>
          <p><strong>下载链接：</strong>
            <el-link
              type="primary"
              :href="resultData.path"
              target="_blank"
            >
              点击下载
            </el-link>
          </p>
        </div>
      </div>
      <div v-else class="error-result">
        <el-icon class="error-icon"><close /></el-icon>
        <h3>上传失败</h3>
        <p>{{ errorMessage }}</p>
      </div>
      <template #footer>
        <el-button type="primary" @click="resultDialogVisible = false">确定</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Check, Close, UploadFilled } from '@element-plus/icons-vue'
import type { FormInstance, FormRules, UploadFile, UploadFiles, UploadInstance } from 'element-plus'
import { ElMessage } from 'element-plus'

interface FormData {
  version: string
  describe: string
}

interface ResultData {
  filename: string
  size: number
  path: string
}

// 表单数据
const form = ref<FormData>({
  version: '',
  describe: ''
})

// 表单验证规则
// 修改 rules 定义，移除 file 的验证
const rules = ref<FormRules>({
  version: [
    { required: true, message: '请输入版本号', trigger: 'blur' },
    { pattern: /^v\d+\.\d+\.\d+$/, message: '格式如：v1.0.0', trigger: 'blur' }
  ],
  describe: [
    { required: true, message: '请输入版本描述', trigger: 'blur' },
    { min: 10, message: '至少10个字符', trigger: 'blur' }
  ]
  // 移除 file 的验证规则
})

// 文件上传相关
const uploadRef = ref<UploadInstance>()
const fileList = ref<UploadFiles>([])
const uploading = ref(false)
const resultDialogVisible = ref(false)
const uploadSuccess = ref(false)
const resultData = ref<ResultData>({
  filename: '',
  size: 0,
  path: ''
})
const errorMessage = ref('')
const uploadForm = ref<FormInstance>()

// 处理文件变化
const handleFileChange = (file: UploadFile, files: UploadFiles) => {
  // 强制只保留最新文件
  fileList.value = [file]
}

// 格式化文件大小
const formatFileSize = (bytes: number): string => {
  if (bytes === 0) return '0 Bytes'
  const k = 1024
  const sizes = ['Bytes', 'KB', 'MB', 'GB']
  const i = Math.floor(Math.log(bytes) / Math.log(k))
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(2))} ${sizes[i]}`
}

// 提交上传
const submitUpload = async () => {
  if (!uploadForm.value) return

  try {
    // 先验证表单
    await uploadForm.value.validate()

    // 直接检查文件（替代表单验证）
    if (fileList.value.length === 0) {
      ElMessage.error('请选择上传文件')
      return
    }

    await doUpload()
  } catch (error) {
    console.error('表单验证出错:', error)
  }
}

// 执行上传
const doUpload = async () => {
  uploading.value = true

  const formData = new FormData()
  formData.append('version', form.value.version)
  formData.append('describe', form.value.describe)
  if (fileList.value[0]?.raw) {
    formData.append('file', fileList.value[0].raw)
  }

  try {
    // 这里替换为你的实际API调用
    const response = await fetch('http://192.168.31.197:5000/upload_hotfix', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }


    const data = await response.json()

    if (data.status === 'success') {
      uploadSuccess.value = true
      resultData.value = {
        filename: fileList.value[0]?.name || '',
        size: data.size || 0,
        path: data.path || ''
      }
    } else {
      uploadSuccess.value = false
      errorMessage.value = data.error || '上传失败'
    }
  } catch (error) {
    uploadSuccess.value = false
    if (error instanceof Error) {
      errorMessage.value = error.message || '网络错误'
    } else {
      errorMessage.value = '未知错误'
    }
  } finally {
    uploading.value = false
    resultDialogVisible.value = true
  }
}

// 重置表单
const resetForm = () => {
  uploadForm.value?.resetFields()
  uploadRef.value?.clearFiles()
  fileList.value = []
}
</script>

<style scoped>
.upload-container {
  max-width: 800px;
  margin: 30px auto;
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.upload-form {
  margin-top: 30px;
}

.success-result {
  text-align: center;
  color: var(--el-color-success);
}

.error-result {
  text-align: center;
  color: var(--el-color-danger);
}

.success-icon,
.error-icon {
  font-size: 60px;
  margin-bottom: 20px;
}

.result-details {
  text-align: left;
  margin-top: 20px;
  color: var(--el-text-color-regular);
}

.result-details p {
  margin: 10px 0;
}

.el-upload__tip {
  font-size: 12px;
  color: var(--el-text-color-secondary);
  margin-top: 10px;
}

.el-icon--upload {
  font-size: 67px;
  color: var(--el-text-color-secondary);
  margin-bottom: 16px;
  line-height: 50px;
}
</style>
