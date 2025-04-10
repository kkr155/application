<script setup lang="ts">

</script>


<template>
  <body onload="sampleApp1()">



  <div>
    <canvas id="glcanvas" width="272" height="376">
    </canvas>
  </div>


  </body>
</template>

<style scoped>
#glcanvas {
  position: fixed;          /* 使用固定定位 */
  bottom: 10px;             /* 距离底部20px */
  right: 10px;              /* 距离右侧20px */
  padding: 0 0;       /* 内边距 */
  border-radius: 5px;       /* 圆角 */
  z-index: 1000;            /* 确保控件在最上层 */
}

</style>


