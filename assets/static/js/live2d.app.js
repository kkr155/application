// 初始化Live2D环境
Live2D.init();

// 设置画布上下文
const canvas = document.getElementById('live2d-canvas');
const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');

// 创建模型实例
const model = Live2DModelWebGL.loadModel("{{ url_for('static', filename='live2d/kokoro.moc') }}");

// 加载模型
//model.loadModel("{{ url_for('static', filename='live2d/kokoro.moc') }}");

// 加载纹理
const texture = new Image();
texture.onload = function () {
    model.setTexture(0, texture); // 绑定纹理到插槽0
    startAnimation();
};
texture.src = "{{ url_for('static', filename='live2d/texture_00.png') }}";

// 启动渲染循环
function startAnimation() {
    model.setGL(gl);
    model.update();
    model.draw();
    requestAnimationFrame(startAnimation);
}
