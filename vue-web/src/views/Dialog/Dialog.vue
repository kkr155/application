<script setup lang="ts">

</script>

<template>
  <div  class="modal-mask" >
    <div class="modal-window">
      <slot>
      </slot>
    </div>
  </div>

</template>

<style scoped>
/* 基础弹窗框架 */
.modal-mask {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0,0,0,0.5);
  display: grid;
  place-items: center;
  z-index: 1000;
}


.modal-window {
  width: auto;
  background: var(--decoration-border);
  padding: 20px;
  border-radius: 8px;
  max-width: 600px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  animation: fadeIn 0.3s ease;
}

/* 动画 */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
  .modal-window {
    max-width: 100%; /* 双重保险 */
    padding: 16px;
    border-radius: 12px; /* 更大圆角更符合移动端风格 */
    max-height: 80vh; /* 更严格的高度限制 */
  }
}
</style>
