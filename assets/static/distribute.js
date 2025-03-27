// 初始化主题
const savedTheme = localStorage.getItem('theme') || 'light'
if (savedTheme === 'dark') {
    document.documentElement.classList.add('dark-mode')
}

fetch('/distribute-file-info')
    .then(res => res.json())
    .then(data => {
        document.querySelector('.file-name').textContent = data.name
        document.querySelector('.file-details').innerHTML = `
                <span>大小：${formatSize(data.size)}</span> •
                <span>更新：${new Date(data.time).toLocaleDateString()}</span>`
    })

function formatSize(bytes) {
    const units = ['B', 'KB', 'MB', 'GB']
    let size = bytes
    let unitIndex = 0
    while (size >= 1024 && unitIndex < units.length - 1) {
        size /= 1024
        unitIndex++
    }
    return `${size.toFixed(1)} ${units[unitIndex]}`
}