  function showTab(tabId) {
            // 隐藏所有内容
            const contents = document.querySelectorAll('.tab-content');
            contents.forEach(content => {
                content.classList.remove('active');
            });

            // 移除所有标签的活动状态
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => {
                tab.classList.remove('active');
            });

            // 显示当前选中的内容
            document.getElementById(tabId).classList.add('active');

            // 设置当前标签为活动状态
            const activeTab = Array.from(tabs).find(tab => tab.id === tabId+'tab');
            if (activeTab) {
                activeTab.classList.add('active');
            }
        }