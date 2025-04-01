 // 页面加载完成后执行
    document.addEventListener('DOMContentLoaded', function () {
        // 获取表格主体元素
        const tableBody = document.getElementById('table-body');

        // 请求API数据
        fetch('/json/modern-history')
            .then(response => {
                if (!response.ok) {
                    throw new Error('网络响应异常');
                }
                return response.json();
            })
            .then(data => {
                // 清空加载状态
                tableBody.innerHTML = '';
                console.log(data)
                // 遍历数据并填充表格
                data.forEach(item => {
                    const row = document.createElement('tr');

                    // 时间列
                    const timeCell = document.createElement('td');
                    timeCell.textContent = item.time;
                    row.appendChild(timeCell);

                    // 名称列
                    const nameCell = document.createElement('td');
                    nameCell.textContent = item.name;
                    row.appendChild(nameCell);

                    // 影响列（处理数组数据）
                    const impactCell = document.createElement('td');
                    if (Array.isArray(item.impact)) {
                        impactCell.innerHTML = item.impact.map(i => `• ${i}`).join('<br>');
                    } else {
                        impactCell.textContent = item.impact;
                    }
                    row.appendChild(impactCell);

                    // 特质列（处理数组/字符串）
                    const charCell = document.createElement('td');
                    if (Array.isArray(item.characteristics)) {
                        charCell.innerHTML = item.characteristics.map(c => `› ${c}`).join('<br>');
                    } else {
                        charCell.textContent = item.characteristics;
                    }
                    row.appendChild(charCell);

                    // 地点
                    const locationCell = document.createElement('td');
                    locationCell.textContent = item.location;
                    row.appendChild(locationCell);

                    // 人物
                    const partiesCell = document.createElement('td');
                    if (Array.isArray(item.parties)) {
                        partiesCell.innerHTML = item.parties.map(i => `• ${i}`).join('<br>');
                    } else {
                        partiesCell.textContent = item.parties;
                    }
                    row.appendChild(partiesCell);

                    // 类型列
                    const typeCell = document.createElement('td');
                    typeCell.textContent = item.name;
                    row.appendChild(typeCell);
                    // 将行添加到表格
                    tableBody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('获取数据失败:', error);
                tableBody.innerHTML = `
                <tr>
                    <td colspan="4" style="color: red; text-align: center;">
                        数据加载失败: ${error.message}
                    </td>
                </tr>
            `;
            });
    });