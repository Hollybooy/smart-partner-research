# Smart Partner 评估研究 | Y1 EAP Project

一个静态前端页面（纯英文），展示针对 **Smart Partner**（帮助西浦大一学生通过 EAP 考试的 AI 学习智能体）的**任务型混合设计评估研究**。

研究核心是"参与者做了什么、我们如何评估效果"，而非主观感受问卷：参与者先完成一次真实的 EAP 写作—修订任务，再由客观产出（草稿质量的前后变化与延迟迁移表现）判定效果。问卷降为任务后的辅助解释工具。

> **研究尚未执行**：页面上的数字全部为占位符（"—"）。回收数据后，替换 `index.html` 底部 `DATA` 对象中的数值即可，所有图表与 KPI 会自动更新。

## 设计要点

| 要素 | 内容 |
|---|---|
| 设计 | 2×2 混合设计（被试间：反馈方式 A/B；被试内：时间 T1/T2） |
| 任务 | 35 分钟写作—修订：前测写作 10 min（无 AI）→ AI 辅助修订 15 min → 后测 5 min，1 周后延迟迁移测验 10 min |
| 干预 | A 直接纠错 / B 引导提示，两者指出相同的错误，差别仅在是否给出正确形式 |
| 分层变量 | EAP 四个层级（A 基础 / B、C 核心 / High Level 高阶）用于分层随机化 |
| 主要结局 | 修订后草稿质量（0–100 量表，双盲双评，ICC 校验） |
| 样本 | 便利抽样，目标 40 人（每组 20 人） |

## 项目结构

```
smart-partner-research/
├── index.html    # 页面本体（单文件：样式 + 图表渲染 + 二维码，无任何外部依赖）
└── README.md     # 本指南
```

页面不引用任何本地资源，也不依赖构建工具——`index.html` 单独一个文件即可发布。

## 一、填入数据

编辑 `index.html` 底部 `<script>` 里的 `DATA` 对象，每项只有一份英文文字（`label` / `sub`）：

| 字段 | 用途 |
|---|---|
| `kpiSample` | 样本构成 KPI（有效人数、条件数、层级数、回访保留率） |
| `donut` | EAP 四层级构成环形图 |
| `kpiOutcome` | 主要结局 KPI（初稿 / 终稿 / 提升 / 迁移均分） |
| `qualityBars` | 草稿质量条形图（A、B 两组的 T1 / T2 / T3） |
| `behaviourBars` | 修订行为（采纳率、自主修正占比） |
| `subjectiveBars` | 任务后主观评价（有用性、信任、认知负荷） |

数值为 0 时，图表显示占位卡而不渲染空坐标轴，因此可以在数据不完整时安全发布。

## 二、问卷二维码

编辑 `index.html` 脚本里的 `const SURVEY_URL = '';`，填入问卷链接（如问卷星 / Qualtrics 的短链）。第 7 部分（Instruments & Ethics）的二维码会在页面加载时自动生成；未填写时显示 "Awaiting" 标签，不会出现失效二维码。

## 三、发布到 GitHub Pages

1. 访问 https://github.com/new 创建仓库 `smart-partner-research`（选 Public）
2. **Add file → Upload files**，把 `index.html` 拖进去提交
3. **Settings → Pages → Deploy from a branch → main / (root) → Save**
4. 约 1–2 分钟后获得链接 `https://<用户名>.github.io/smart-partner-research/`

> `*.github.io` 在大陆无法直连，访问者若无代理打不开，可把同一份 `index.html` 再发到国内静态托管。

## 四、本地预览

直接双击 `index.html` 用浏览器打开即可（图表动画正常；二维码需联网加载）。

## 五、当前版本要点

1. **纯英文页面**：`<html lang="en">`，无中文与语言切换。
2. **任务型混合设计**：先完成任务再评估产出，问卷仅作任务后的解释工具。
3. **章节结构（01–09）**：Research questions → Evaluation design → The task → Intervention → Measures → Results & charts → Instruments & ethics → Reflection → References，末尾另有一个无编号的 Pending 区块。
4. **参考文献 11 条**：覆盖二语写作反馈、反馈层级理论、认知负荷、信任量表、ICC、问卷方法、主题编码与混合方法框架，每条附一句"支撑什么"。
5. **占位策略**：顶部一条状态条 + 末尾"待补充材料"看板；无数据时图表与二维码显示占位卡。
6. **黑白瑞士网格版式**：左侧 sticky 大号章节编号、发丝线分隔、无圆角无阴影、无彩色。
