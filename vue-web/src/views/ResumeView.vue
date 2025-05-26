<script setup lang="ts">

// 简历数据
const resumeData = {
  personalInfo: {
    name: '张先杰',
    title: 'Android',
    avatar: '.jpg',
    contacts: [
      { icon: 'fas fa-phone', text: '150-5209-3802' },
      { icon: 'fas fa-envelope', text: '1473366726@qq.cpm' },
      { icon: 'fas fa-map-marker-alt', text: '南京 · 中国' }
    ]
  },
  skills: [
    { name: 'Android(Kotlin/Java)开发', level: 90 },
    { name: 'Python Flask开发', level: 6 },
    { name: 'Vue.js/Vue3', level: 4 }
  ],
 /* languages: [
    { name: '英语 · 专业八级', level: 90 },
    { name: '日语 · N1', level: 80 }
  ],*/
  profile: '精通企业级（ToB）及消费级（ToC）项目开发，参与过电商、O2O服务、企业管理类系统等高复杂度项目。擅长Kotlin语言开发，具备从0到1架构设计能力，熟悉MVC/MVP/MVVM模式选型与落地。核心能力：\n' +
    '▸ 性能优化专家：深度掌握内存泄漏治理（Java GC机制/内存模型）、启动速度优化（冷热启动分级策略）、布局渲染（层级压缩/异步加载）及APK瘦身（资源混淆/动态加载）\n' +
    '▸ 系统级开发能力：精通Android消息机制（Handler/Looper）、事件分发体系（冲突解决策略）、自定义View开发（沉浸式/协调者布局）及多版本适配（Android 5-14特性适配）\n' +
    '▸ 工程化实践：搭建标准化网络框架（TCP长连接/协议栈封装，SDK模块化输出至GitHub），主导Gradle构建优化（Flavor多环境配置/Task自动化打包），C++混合开发（CMake/JNI集成）\n' +
    '▸ 全链路闭环经验：第三方服务集成（微信支付/环信IM）、性能监控（App Inspection工具链）、应用商店上架（小米/华为等平台合规流程）',
  experiences: [
    {
      period: '2024.12 - 至今',
      company: '江苏小拉科技有限公司',
      position: 'Android 开发',
      items: [
        '需求评审，参与需求会议',
        '针对程序进行优化：\n 1、架构分离打包,apk大小减小20%；\n 2、基于buildTypes的环境分离与基于task的批量打包，上架效率提升40%',
        '基于需求迭代旧代码旧功能',
        '基于需求进行版本迭代',
        "负责上架小米、华为、oppo、vivo、应用宝 商店"
      ]
    },
    {
      period: '2022.3 - 2024.10',
      company: '北京光速斑马数据科技有限公司',
      position: 'Android 开发',
      items: [
        '需求评审，参与版本需求会议， 确认改进方案， 提供改进建议',
        '业务处理，完成自己负责的业务相关代码',
        'UI绘制，负责项目中复杂布局的自定义绘制',
        '技术革新与优化，替换掉某些已经过期到马上被移除的方法'
      ]
    },
    {
      period: '2021.10 - 2022.1）',
      company: '北京开阳创和科技有限公司',
      position: 'Android 开发',
      items: [
        '负责驻场公司（中国航天科工二院）的技术选型及UI设计',
        '编写项目日志以及交接材料',
        '根据甲方需求进行迭代及各项适配',
        '配合甲方进行项目测试'
      ]
    },
    {
      period: '2018.8 - 2021.10',
      company: '百灵传播(北京)科技有限公司',
      position: 'Android 开发',
      items: [
        '参与产品需求分析，确定产品方案',
        '负责架构搭建及框架技术选型',
        '负责完整项目的独立编写并撰写 md 文档',
        '根据客户要求完成功能定制并进行性能优化与兼容,降低崩溃率',
        '后期完成项目新增需求改动和 bug 修改，确保产品具有优质的用户体验与良好的兼容性 '
      ]
    }
  ],
  education: {
    period: '2014.09 – 2018.07',
    school: '三江学院',
    major: '计算机科学与技术 · 本科',
    items: [
    ]
  },
  projects: [
    {
      title: '雨欣智慧',
      description: '一款toB APP，针对于丙肝领域，基本涵盖了医疗的整体流程，问诊、开药、入库及' +
        '售后、数据统计，除此之外 还有针对医生的目标管理、项目管理。 ',
      tags: ['医疗', 'old项目', '维护', '复杂布局']
    },
    {
      title: '星火除虫',
      description: '一款toB APP，类似美团骑手端，对除虫师考勤，服务 管理，包括完整接单流程，位' +
        '置持续监听。',
      tags: ['服务管理', 'toB', '除虫师骑手端', '架构搭建', '保活']
    },
    {
      title: '小年鱼',
      description: '电商，卖莆田货。',
      tags: ['电商', 'toC', '经典', '部分开发']
    },
    {
      title: '点到',
      description: '点到是一款 O2O 服务类 App。 \n' +
        'App 可以根据用户提供的定位来为用户提供距离最近的医师，并且可以定点预约。',
      tags: ['生活服务', 'OtoO', '部分开发']
    },
    {
      title: '资产管理系统',
      description: '运行在特定的pos机，主要是对货物流水进行盘点用。',
      tags: ['后勤管理', '盘点', '政府项目', '从零到一']
    }
  ]
}
</script>

<template>
  <div class="resume-container">


    <div class="resume">
      <!-- 左侧边栏 -->
      <aside class="sidebar">
        <img :src="resumeData.personalInfo.avatar" alt="头像" class="avatar">
        <h1 class="name">{{ resumeData.personalInfo.name }}</h1>
        <p class="title">{{ resumeData.personalInfo.title }}</p>

        <div class="card">
          <h2><i class="fas fa-id-card"></i> 联系方式</h2>
          <div
            class="contact-item"
            v-for="(contact, index) in resumeData.personalInfo.contacts"
            :key="index"
          >
            <i :class="contact.icon"></i>
            <span>{{ contact.text }}</span>
          </div>
        </div>

        <div class="card">
          <h2><i class="fas fa-star"></i> 专业技能</h2>
          <div class="skill" v-for="(skill, index) in resumeData.skills" :key="'skill-'+index">
            <div class="skill-name">
              <span>{{ skill.name }}</span>
              <span>{{ skill.level }}%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-level" :style="{ width: `${skill.level}%` }"></div>
            </div>
          </div>
        </div>

<!--        <div class="card">
          <h2><i class="fas fa-language"></i> 语言能力</h2>
          <div class="skill" v-for="(lang, index) in resumeData.languages" :key="'lang-'+index">
            <div class="skill-name">
              <span>{{ lang.name }}</span>
              <span>{{ lang.level }}%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-level" :style="{ width: `${lang.level}%` }"></div>
            </div>
          </div>
        </div>-->
      </aside>

      <!-- 主内容区 -->
      <main class="main">
        <section class="section">
          <h2>个人简介</h2>
          <p class="timeline-desc">
            {{ resumeData.profile }}
          </p>
        </section>

        <section class="section">
          <h2>工作经历</h2>
          <div class="timeline">
            <div class="timeline-item" v-for="(exp, index) in resumeData.experiences" :key="'exp-'+index">
              <div class="timeline-date">{{ exp.period }}</div>
              <h3 class="timeline-title">{{ exp.company }} · <span>{{ exp.position }}</span></h3>
              <ul class="timeline-desc">
                <li v-for="(item, i) in exp.items" :key="i">{{ item }}</li>
              </ul>
            </div>
          </div>
        </section>

        <section class="section">
          <h2>教育背景</h2>
          <div class="timeline">
            <div class="timeline-item">
              <div class="timeline-date">{{ resumeData.education.period }}</div>
              <h3 class="timeline-title">{{ resumeData.education.school }} · <span>{{ resumeData.education.major }}</span></h3>
              <ul class="timeline-desc">
                <li v-for="(item, index) in resumeData.education.items" :key="'edu-'+index">{{ item }}</li>
              </ul>
            </div>
          </div>
        </section>

        <section class="section">
          <h2>精选项目</h2>
          <div class="projects">
            <div class="project-card" v-for="(project, index) in resumeData.projects" :key="'proj-'+index">
              <h3><i class="fas"></i> {{ project.title }}</h3>
              <p>{{ project.description }}</p>
              <div class="project-tags">
                <span class="tag" v-for="(tag, i) in project.tags" :key="i">{{ tag }}</span>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<style scoped>



/* 主容器 - 杂志风格布局 */
.resume {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 2rem;
  perspective: 1800px;
}

/* 左侧边栏 - 立体卡片效果 */
.sidebar {
  background: var(--light);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-lg);
  transform-style: preserve-3d;
  position: relative;
  border: 1px solid rgba(255,255,255,0.1);
}

.sidebar::before {
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  background: var(--gradient);
  transform: translateZ(-20px);
  opacity: 0.1;
  z-index: -1;
}

/* 头像 - 3D悬浮效果 */
.avatar {
  width: 180px;
  height: 180px;
  border-radius: var(--radius-full);
  object-fit: cover;
  margin: 0 auto 1.5rem;
  display: block;
  border: 4px solid white;
  box-shadow: var(--shadow-primary);
  transition: all 0.4s ease;
  transform: rotateY(0deg);
}

.avatar:hover {
  transform: rotateY(15deg) scale(1.05);
}

/* 主标题 - 渐变文字 */
.name {
  font-size: 2rem;
  font-weight: 800;
  background: var(--gradient);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  text-align: center;
  margin-bottom: 0.5rem;
  letter-spacing: -0.5px;
}

.title {
  font-size: 1.1rem;
  color: var(--secondary);
  text-align: center;
  margin-bottom: 2rem;
  font-weight: 500;
  position: relative;
}

.title::after {
  display: block;
  width: 60px;
  height: 3px;
  background: var(--gradient);
  margin: 0.8rem auto 0;
  border-radius: var(--radius-full);
}

/* 信息卡片 - 微交互 */
.card {
  margin-bottom: 2rem;
  position: relative;
}

.card::after {
  position: absolute;
  bottom: -1rem;
  left: 0;
  width: 40px;
  height: 3px;
  background: var(--accent);
  border-radius: var(--radius-full);
  transition: width 0.3s ease;
}

.card:hover::after {
  width: 80px;
}

.card h2 {
  font-size: 1.3rem;
  margin-bottom: 1.2rem;
  color: var(--dark);
  display: flex;
  align-items: center;
}

.card h2 i {
  margin-right: 0.6rem;
  color: var(--primary);
  font-size: 1.1rem;
}

/* 联系信息 - 图标动画 */
.contact-item {
  display: flex;
  align-items: center;
  margin-bottom: 0.8rem;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: var(--radius-sm);
}

.contact-item:hover {
  background: rgba(107, 90, 237, 0.08);
  transform: translateX(5px);
}

.contact-item i {
  width: 18px;
  height: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--gradient);
  color: white;
  border-radius: 50%;
  margin-right: 0.5rem;
  font-size: 0.9rem;
}

/* 技能条 - 动态填充 */
.skill {
  margin-bottom: 1.2rem;
}

.skill-name {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.4rem;
  font-weight: 500;
}

.skill-bar {
  height: 8px;
  background: var(--gray);
  border-radius: var(--radius-full);
  overflow: hidden;
  position: relative;
}

.skill-level {
  height: 100%;
  border-radius: var(--radius-full);
  background: var(--gradient);
  position: relative;
  transition: width 1s cubic-bezier(0.65, 0, 0.35, 1);
}

.skill-level::after {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg,
  rgba(255,255,255,0.3) 0%,
  rgba(255,255,255,0) 100%);
}

/* 主内容区 - 杂志风格 */
.main {
  display: grid;
  gap: 2rem;
}

.section {
  background: var(--light);
  border-radius: var(--radius-lg);
  padding: 2rem;
  box-shadow: var(--shadow-md);
  position: relative;
  overflow: hidden;
}

.section::before {
  position: absolute;
  top: 0;
  left: 0;
  width: 5px;
  height: 100%;
  background: var(--gradient);
}

.section h2 {
  font-size: 1.5rem;
  margin-bottom: 1.5rem;
  color: var(--primary);
  position: relative;
  display: inline-block;
}

.section h2::after {
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 40px;
  height: 3px;
  background: var(--gradient);
  border-radius: var(--radius-full);
}

/* 时间轴 - 3D效果 */
.timeline {
  position: relative;
  padding-left: 1.5rem;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 10px;
  bottom: 10px;
  width: 2px;
  background: var(--gray);
  transform: translateZ(-10px);
}

.timeline-item {
  position: relative;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: rgba(255,255,255,0.05);
  border-radius: var(--radius-md);
  transition: all 0.3s ease;
  border: 1px solid var(--gray);
}

.timeline-item:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-sm);
  border-color: var(--primary);
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -20px;
  top: 1.8rem;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--gradient);
  border: 2px solid var(--light);
  z-index: 1;
}

.timeline-date {
  font-size: 0.9rem;
  color: var(--secondary);
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.timeline-title {
  font-size: 1.2rem;
  margin-bottom: 0.8rem;
  color: var(--dark);
}

.timeline-title span {
  color: var(--primary);
  font-weight: 600;
}

.timeline-desc {
  color: var(--dark);
  opacity: 0.9;
  white-space: pre-line;
}

.timeline-desc li {
  margin-bottom: 0.5rem;
  position: relative;
  padding-left: 1.2rem;
}

.timeline-desc li::before {
  content: '•';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-weight: bold;
}

/* 项目展示 - 卡片组 */
.projects {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.project-card {
  background: var(--light);
  border-radius: var(--radius-md);
  padding: 1.5rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--gray);
  transition: all 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-md);
  border-color: var(--secondary);
}

.project-card h3 {
  font-size: 1.1rem;
  margin-bottom: 0.8rem;
  color: var(--secondary);
  display: flex;
  align-items: center;
}

.project-card h3 i {
  margin-right: 0.6rem;
  color: var(--primary);
}

.project-card p {
  color: var(--dark);
  opacity: 0.9;
  font-size: 0.95rem;
  margin-bottom: 1rem;
}

.project-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.tag {
  background: rgba(107, 90, 237, 0.1);
  color: var(--secondary);
  padding: 0.3rem 0.8rem;
  border-radius: var(--radius-full);
  font-size: 0.8rem;
  font-weight: 500;
}


/* 响应式设计 */
@media (max-width: 992px) {
  .resume {
    grid-template-columns: 1fr;
  }

  .projects {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  body {
    padding: 1rem;
  }

  .section, .sidebar {
    padding: 1.5rem;
  }
}

/* 打印优化 */
@media print {
  body {
    padding: 0;
    background: white !important;
    color: black !important;
  }

  .resume {
    grid-template-columns: 240px 1fr;
    gap: 1rem;
  }

  .sidebar, .section {
    box-shadow: none;
    border: 1px solid #ddd;
    page-break-inside: avoid;
  }

  a {
    text-decoration: none !important;
    color: inherit !important;
  }
}
</style>
