// 自动加载文档
async function loadDocx() {
    try {
        const response = await fetch('/word/modern-history');
        if (!response.ok) throw new Error(`HTTP错误: ${response.status}`);

        const arrayBuffer = await response.arrayBuffer();
        console.log(arrayBuffer)
        const result = await mammoth.convertToHtml({arrayBuffer}, {
        convertLists: false,
                styleMap: [
                    "u => u", // 下划线

                ]
            }
        );
        console.log(result.value)

        // 处理文档内容
        processDocument(result.value);
    } catch (error) {
        console.error('加载失败:', error);
        document.getElementById('doc-container').innerHTML = `
                <div class="alert alert-danger">
                    文档加载失败: ${error.message}
                </div>
            `;
    }
}

// 处理文档内容并生成目录
function processDocument(html) {
    const docContainer = document.getElementById('doc-container');
    docContainer.innerHTML = html;

     const chapterRegex = /第[一二三四五六七八九十百千零]+章/g;
     const headings = Array.from(docContainer.querySelectorAll('h1, h2, h3, h4, h5, h6, p'))
         .filter(el => chapterRegex.test(el.textContent));
     const tocContainer = document.getElementById('toc-container');
     if (headings.length > 0) {
         tocContainer.innerHTML = '<h4>目录</h4>' +
             headings.map((heading, index) => {
                 const id = `chapter-${index}`;
                 heading.id = id;
                 heading.classList.add('chapter-title');
                 const result = heading.textContent.replace(/选择题：$/, '');
                 return `<div class="toc-item" onclick="scrollToChapter('${id}')">
                     ${result}
                 </div>`;
             }).join('');
     } else {
         tocContainer.innerHTML = '<p>未检测到章节标题</p>';
     }
}

function scrollToChapter(id) {
    const element = document.getElementById(id);
    if (element) {
        element.scrollIntoView({behavior: 'smooth'});
        document.querySelectorAll('.chapter-title').forEach(el => {
            el.style.backgroundColor = '';
        });
        element.style.backgroundColor = '#fff3cd';
    }
}


window.addEventListener('DOMContentLoaded', loadDocx);