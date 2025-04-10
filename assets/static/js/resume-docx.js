// 自动加载文档
async function loadDocx() {
    try {
        const response = await fetch('/word/resume');
        if (!response.ok) throw new Error(`HTTP错误: ${response.status}`);

        const arrayBuffer = await response.arrayBuffer();
        console.log(arrayBuffer)
        const result = await mammoth.convertToHtml({arrayBuffer}, {
                convertLists: false,
                styleMap: []
            }
        );
        console.log(result.value)

        // 处理文档内容
        const docContainer = document.getElementById('doc-container');
        docContainer.innerHTML = result.value;
    } catch (error) {
        console.error('加载失败:', error);
        document.getElementById('doc-container').innerHTML = `
                <div class="alert alert-danger">
                    文档加载失败: ${error.message}
                </div>
            `;
    }
}

window.addEventListener('DOMContentLoaded', loadDocx);
