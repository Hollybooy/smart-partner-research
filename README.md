# Smart Partner 智能体调研统计 | Y1 EAP Project

一个静态前端页面，展示针对 **Smart Partner**（帮助西浦大一学生通过 EAP 考试的 AI 学习智能体）的调研统计结果：调研主题、目标人群、使用情况、使用目的、调研图片。

## 项目结构

```
smart-partner-research/
├── index.html    # 页面（单文件，含样式、图表与图片上传逻辑）
├── images/       # 长期展示的调研图片放这里（1.jpg、2.jpg…，png 也可以）
└── README.md     # 本指南
```

## 一、替换成你的真实调研数据

页面里的图表全部是**示例数据**（页面顶部有黄色提示条）。所有数据集中在 `index.html` 底部 `<script>` 里的一个 `DATA` 对象中，改数字即可：

```js
const DATA = {
  kpiAudience: [...]   // 第 2 部分「目标人群」的四张数据卡
  donut: [...]         // 第 2 部分环形图（按 EAP 班级）
  kpiUsage: [...]      // 第 3 部分「使用情况」的四张数据卡
  freqBars: [...]      // 使用频率分布条形图
  featureBars: [...]   // 各功能使用率条形图
  purposeBars: [...]   // 使用目的条形图
}
```

- 每条数据都有 `zh` / `en` 两份文字，对应页面右上角的中英文切换
- 文字说明（主题介绍、关键发现等）直接在 HTML 中搜索 `★ 可编辑` 找到对应段落修改

## 二、调研图片的两种放法

1. **长期展示（推荐）**：把图片复制到 `images/` 文件夹，命名为 `1.jpg`、`2.jpg`…（png 也可以），页面打开会自动按顺序加载
2. **临时预览**：在页面第 5 部分点击上传区域或拖拽图片进去，立即可见，但**刷新后会消失**（纯前端页面不会保存文件）

## 三、发布到 GitHub Pages

如果你之前已按问卷项目的步骤注册了 GitHub：

1. 访问 https://github.com/new 创建新仓库，如 `smart-partner-research`（选 Public）
2. **Add file → Upload files**，把 `index.html` 拖进去提交
3. **Settings → Pages → Deploy from a branch → main / (root) → Save**
4. 约 1–2 分钟后获得链接 `https://<用户名>.github.io/smart-partner-research/`

> 网页上传方式不能直接传文件夹。要上传 `images/` 里的图片：在 GitHub 仓库页点 **Add file → Create new file**，文件名框输入 `images/1.jpg`（输入斜杠会自动创建文件夹），然后用 "Upload files" 按钮选本地图片，或逐个用 Add file → Upload files 时先把浏览器路径栏后缀改为 `/images/` 再拖入。最省事的做法：一次 **Add file → Upload files** 时把 `index.html` 与所有图片一起拖入，图片会平铺在根目录——若用这种方式，请把 `index.html` 中的 `images/${i}.jpg` 改为 `/${i}.jpg`。

> 与之前相同的提醒：`*.github.io` 在大陆无法直连，访问者若无代理打不开，可把同一份文件再发到国内静态托管。

## 四、本地预览

直接双击 `index.html` 用浏览器打开即可（图片上传预览、图表动画都能正常使用）。
