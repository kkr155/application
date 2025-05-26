<script setup lang="ts">
const langData = [
  { name: 'Kotlin', percent: 55.22, color: '#7F52FF' },
  { name: 'JavaScript', percent: 25.8, color: '#F7DF1E' },
  { name: 'Python', percent: 4.58, color: '#3776AB' },
  { name: 'Vue', percent: 3.72, color: '#41B883' },
  { name: 'HTML', percent: 3.69, color: '#E44D26' },
  { name: 'Java', percent: 3.61, color: '#007396' },
  { name: 'CSS', percent: 2.55, color: '#2965F1' },
  { name: 'TypeScript', percent: 0.84, color: '#3178C6' },
]

function getLangOffset(index: number) {
  // 计算每个语言段的起始偏移量
  let offset = 0
  for (let i = 0; i < index; i++) {
    offset += langData[i].percent
  }
  return 283 - offset * 2.83
}

function getMainLang() {
  return langData[0].name // 返回占比最高的语言
}
</script>

<template>
  <div class="github-langs-card">
    <h2><i class="fas fa-code"></i> 代码语言分布</h2>
    <div class="langs-container">
      <!-- 环形图 -->
      <div class="langs-chart">
        <svg viewBox="0 0 100 100">
          <!-- 背景圆 -->
          <circle cx="50" cy="50" r="45" fill="none" stroke="#f0f0f0" stroke-width="10" />

          <!-- 动态语言段 -->
          <circle
            v-for="(lang, index) in langData"
            :key="lang.name"
            cx="50"
            cy="50"
            r="45"
            fill="none"
            :stroke="lang.color"
            stroke-width="10"
            :stroke-dasharray="`${lang.percent * 2.83} 283`"
            :stroke-dashoffset="getLangOffset(index)"
          />
        </svg>

        <!-- 中心文字 -->
        <div class="chart-center">
          <div class="total-langs">{{ langData.length }}种语言</div>
          <div class="main-lang">{{ getMainLang() }}</div>
        </div>
      </div>

      <!-- 进度条列表 -->
      <div class="langs-list">
        <div v-for="lang in langData" :key="`list-${lang.name}`" class="lang-item">
          <div class="lang-meta">
            <span class="lang-color" :style="{ background: lang.color }"></span>
            <span class="lang-name">{{ lang.name }}</span>
            <span class="lang-percent">{{ lang.percent }}%</span>
          </div>
          <div class="lang-progress">
            <div
              class="lang-progress-bar"
              :style="{
                width: `${lang.percent}%`,
                backgroundColor: lang.color,
              }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.github-langs-card {
  background: white;
  border-radius: 10px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);

  h2 {
    color: #24292e;
    margin-bottom: 1.5rem;
    font-size: 1.25rem;

    i {
      margin-right: 10px;
    }
  }
}

.langs-container {
  display: flex;
  flex-direction: column;
  gap: 2rem;

  @media (min-width: 768px) {
    flex-direction: row;
    align-items: center;
  }
}

.langs-chart {
  position: relative;
  width: 180px;
  height: 180px;
  margin: 0 auto;

  svg {
    width: 100%;
    height: 100%;

    circle {
      transition: all 0.6s ease;
    }
  }

  .chart-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;

    .total-langs {
      font-size: 0.9rem;
      color: #586069;
    }

    .main-lang {
      font-weight: 600;
      color: #24292e;
      margin-top: 4px;
    }
  }
}

.langs-list {
  flex: 1;

  .lang-item {
    margin-bottom: 12px;

    &:last-child {
      margin-bottom: 0;
    }
  }

  .lang-meta {
    display: flex;
    align-items: center;
    margin-bottom: 4px;
    font-size: 0.9rem;

    .lang-color {
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      margin-right: 8px;
    }

    .lang-name {
      flex: 1;
      color: #24292e;
    }

    .lang-percent {
      color: #586069;
    }
  }

  .lang-progress {
    height: 8px;
    background: #f0f0f0;
    border-radius: 4px;
    overflow: hidden;

    .lang-progress-bar {
      height: 100%;
      border-radius: 4px;
      transition: width 0.6s ease;
    }
  }
}
</style>
