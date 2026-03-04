# SEO Blog Generator for Drama.Land

Generate SEO-optimized blog articles following Drama.Land's content specification.

## Usage

```
/SEO-Blog [type] [topic]
```

**文章类型：**
- `/SEO-Blog how-to [主题]` - 教程类文章
- `/SEO-Blog model-launch [模型名]` - 模型上线类文章
- `/SEO-Blog [topic]` - 自动识别类型

---

## 🌳 文章类型分支

```
SEO-Blog Skill
│
├── 📖 How-To Tutorial（教程类）
│   └── 教用户如何做某事
│
├── 🚀 Model Launch（模型上线类）
│   └── 新模型发布/接入平台
│
├── 📊 Comparison（对比类）[待开发]
│   └── A vs B 对比文章
│
├── 📰 News（新闻类）[待开发]
│   └── 行业动态、产品更新
│
└── 📚 Guide（指南类）[待开发]
    └── 综合性主题指南
```

### 类型自动识别

```
用户输入包含...          →  触发分支
─────────────────────────────────────
"如何" / "How to"        →  📖 How-To
"教程" / "Tutorial"      →  📖 How-To
"怎么做" / "怎么用"      →  📖 How-To
─────────────────────────────────────
"上线" / "发布"          →  🚀 Model Launch
"接入" / "Launches"      →  🚀 Model Launch
"新模型" / "Model"       →  🚀 Model Launch
─────────────────────────────────────
"vs" / "对比" / "比较"   →  📊 Comparison
─────────────────────────────────────
其他                     →  询问用户确认类型
```

---

# ═══════════════════════════════════════════════════════════
# 📖 分支一：How-To Tutorial（教程类）
# ═══════════════════════════════════════════════════════════

## 📖 How-To 概述

**适用场景：** 教用户如何完成某个任务
- "How to Make AI Anime Videos"
- "How to Create AI Music Videos"
- "How to Use [工具名]"

**核心目标：** 让零基础用户能跟着做出来

---

## 📖 How-To 文章结构（9段式）

```
1️⃣ What Is [主题]?
   ├── 定义（1-2句）
   ├── 为什么重要（痛点）
   ├── 主要方法/类型概述（3种左右）
   └── CTA #1

2️⃣ Why [产品] for [主题]?
   ├── 产品优势 1
   ├── 产品优势 2
   ├── 产品优势 3
   ├── 产品优势 4（可选）
   └── CTA #2

3️⃣ How to [做某事] on [产品]（核心教程）
   ├── Step 1: [步骤名]
   │   ├── 操作说明
   │   └── 具体示例/Prompt
   ├── Step 2: [步骤名]
   ├── Step 3: [步骤名]
   ├── Step 4: [步骤名]
   ├── Step 5: [步骤名]
   └── Step 6: [步骤名]
   └── CTA #3

4️⃣ Pro Tips（专业技巧）
   ├── Tip 1 + 示例
   ├── Tip 2 + 示例
   ├── Tip 3 + 示例
   ├── Tip 4 + 示例
   └── Tip 5 + 示例

5️⃣ Examples: What You Can Create
   ├── Example 1: [场景] - Concept/Scenes/Result
   ├── Example 2: [场景]
   └── Example 3: [场景]

6️⃣ Common Mistakes to Avoid
   ├── Mistake 1 + 为什么错 + 怎么避免
   ├── Mistake 2
   ├── Mistake 3
   ├── Mistake 4
   └── Mistake 5

7️⃣ FAQ（5-7个问题）
   ├── Q1: [常见问题]?
   ├── Q2: [常见问题]?
   └── ...

8️⃣ Start Creating（结尾 CTA）
   ├── 总结核心价值
   ├── 鼓励用户开始
   └── CTA #4（最终号召）
```

---

## 📖 How-To 标题公式

```
How to [动作] + [对象]: [附加价值]

示例：
├── "How to Make AI Anime Videos: Tools, Tips & Examples"
├── "How to Create AI Music Videos with Drama.Land"
├── "How to Use Character Packs: Complete Guide"
└── "How to Generate Beat-Synced Videos in Minutes"
```

---

## 📖 How-To 调研清单

```
☐ 产品调研（WebFetch 官网）
  ├── 产品名称 + 定位
  ├── 核心功能列表
  ├── 使用的 AI 模型
  ├── 工作流程（用户怎么用）
  └── 定价信息

☐ 竞品调研（WebSearch）
  ├── 搜索 "how to [主题] [年份]"
  ├── 搜索 "best [工具类型] [年份]"
  └── 提取竞品文章结构

☐ SEO 关键词（WebSearch）
  ├── 主关键词: "how to [动作] [对象]"
  ├── 长尾关键词:
  │   ├── "[对象] tutorial"
  │   ├── "[对象] step by step"
  │   ├── "best [工具类型] for [用途]"
  │   ├── "[产品名] tutorial [年份]"
  │   └── "free [工具类型]"
  └── Tags: 3-5个

☐ 用户问题收集
  ├── 搜索 "[主题] FAQ"
  ├── 搜索 "[主题] common questions"
  └── 整理 5-7 个 FAQ
```

---

## 📖 How-To 必须包含元素

```
☐ 产品优势部分（Why [产品]）
☐ 分步骤教程（Step 1-6）
☐ 每步骤有具体示例/Prompt（代码块格式）
☐ Pro Tips 部分（5条专业技巧）
☐ Examples 部分（3个案例）
☐ Common Mistakes 部分（5个错误）
☐ FAQ 部分（5-7个问题）
☐ CTA 分布：开头1 + Why后1 + 教程后1 + 结尾1 = 4个
```

---

## 📖 How-To Prompt 示例格式

使用代码块展示可直接复制的 Prompt：

```markdown
**Example**:
\`\`\`
A teenage girl with long silver hair and red eyes walks through a neon-lit Tokyo alley at night.
Rain falls gently. She wears a black school uniform with red ribbon.
Cherry blossom petals drift past. Cinematic lighting, Studio Ghibli style.
\`\`\`
```

---

## 📖 How-To Category

Category: `Tutorial`

---


# ═══════════════════════════════════════════════════════════
# 🚀 分支二：Model Launch（模型上线类）
# ═══════════════════════════════════════════════════════════

## 🚀 Model Launch 概述

**适用场景：** 新模型发布或接入平台
- "Seedance 2.0 Launches on Drama.Land"
- "Kling 3.0 Now Available on Drama.Land"
- "Nano Banana 2: What's New"

**核心目标：** 让用户理解模型价值 + 驱动试用

---

## 🚀 Model Launch 文章结构

```
1️⃣ The Problem（痛点开场）
   ├── 现状痛点描述
   ├── 之前方案的不足
   └── 引出新模型如何解决

2️⃣ What [模型] Brings to [平台]
   ├── 能力 1: [名称]
   │   ├── Before: [之前怎样]
   │   ├── Now: [现在怎样]
   │   └── What this means for [平台]: [用户价值]
   ├── 能力 2: [名称]
   ├── 能力 3: [名称]
   └── CTA #1

3️⃣ The [特性] Difference（技术差异化）
   ├── 输入能力对比表
   ├── 核心技术解释
   └── 图示/截图

4️⃣ How [平台] Users Benefit（用户价值表格）
   └── Before vs After 对比表

5️⃣ Workflow on [平台]（操作流程）
   ├── Step 1: 准备素材
   ├── Step 2: 上传到平台
   ├── Step 3: 设置参数
   ├── Step 4: 生成预览
   └── Step 5: 导出

6️⃣ Get Started（结尾 CTA）
   ├── 一句话总结
   └── CTA #2
```

---

## 🚀 Model Launch 标题公式

```
[最高级形容词] + [模型类型] + [模型名] + [动作] + [平台]

示例：
├── "The Most Powerful Multimodal Reference Model Seedance 2.0 Launches on Drama.Land"
├── "Kling 3.0: The Fastest Multi-Character Model Now on Drama.Land"
└── "Nano Banana 2 Brings Studio-Quality Images to Drama.Land"
```

---

## 🚀 Model Launch 调研清单

```
☐ 模型信息（WebFetch 官方文档）
  ├── 模型名称 + 技术名称
  ├── 来源公司/组织
  ├── 发布时间
  ├── 定位（vs 前代、vs 竞品）
  └── 核心卖点一句话

☐ 能力列表（4-6个）
  ├── 能力名称（用户语言）
  ├── 具体数据/数字
  ├── 用户场景
  └── 战略意义

☐ 对比数据
  ├── vs 前代版本
  └── vs 竞品

☐ 技术规格
  ├── 分辨率
  ├── 速度
  ├── 输入限制
  └── 输出格式

☐ 平台集成信息（WebFetch 平台官网）
  ├── 哪些功能使用此模型
  ├── 用户工作流
  └── 定价影响
```

---

## 🚀 Model Launch 必须包含元素

```
☐ 痛点开场（问题描述）
☐ 模型 3-5 个核心能力详解
☐ 每个能力的 Before/Now/What this means 结构
☐ 输入能力对比表（Input Type | Limit | What It Controls）
☐ Before vs After 用户价值表
☐ 操作流程（Step 1-5）
☐ CTA 分布：能力介绍后1 + 结尾1 = 2个
```

---

## 🚀 Model Launch Before/Now 模板

```markdown
### [能力编号]. [能力名称]

**Before:** [之前的痛点/限制]

**Now:** [新模型如何解决]

**What this means for [平台]:** [对用户的具体价值]

![Alt Text](/blog/content/image.jpg)
```

---

## 🚀 Model Launch Category

Category: `Model`

---


# ═══════════════════════════════════════════════════════════
# 📊 分支三：Comparison（对比类）[待开发]
# ═══════════════════════════════════════════════════════════

## 📊 Comparison 概述

**适用场景：** A vs B 工具/模型对比
- "Kling 3.0 vs Runway Gen-3: Which Is Better?"
- "Drama.Land vs Pika: Complete Comparison"

**状态：** 🚧 待开发

---


# ═══════════════════════════════════════════════════════════
# 📰 分支四：News（新闻类）[待开发]
# ═══════════════════════════════════════════════════════════

## 📰 News 概述

**适用场景：** 行业动态、产品更新公告
- "Drama.Land Adds 50 New Visual Styles"
- "AI Video Generation Trends in 2026"

**状态：** 🚧 待开发

---


# ═══════════════════════════════════════════════════════════
# 📚 分支五：Guide（指南类）[待开发]
# ═══════════════════════════════════════════════════════════

## 📚 Guide 概述

**适用场景：** 综合性主题深度指南
- "The Complete Guide to AI Music Video Creation"
- "Everything You Need to Know About Character Consistency"

**状态：** 🚧 待开发

---


# ═══════════════════════════════════════════════════════════
# 🔧 通用组件（所有分支共享）
# ═══════════════════════════════════════════════════════════

## 🔧 SEO Metadata 标准格式

```yaml
---
title: "[标题]"
date: "YYYY-MM-DD"
meta description: "[150字符内摘要]"
coverImage: "/blog/cover/YY-MM-DD-Cover-DramaLand-keywords.jpg"
coverImageAlt: "[封面图描述]"
category: "[Tutorial/Model/Guide/News]"
author: "Team"
tags: ["Tag1", "Tag2", "Tag3"]
keywords: ["keyword1", "keyword2", "keyword3", ...]
---
```

---

## 🔧 文件命名规范

```
文章文件: YYYY-MM-DD-english-keyword.md
封面图:   YY-MM-DD-Cover-DramaLand-keyword1-keyword2.jpg
内容图:   YY-MM-DD-01-DramaLand-description.jpg
素材文档: YYYY-MM-DD-slug-素材.md
```

---

## 🔧 写作风格

### 语气
- 专业但不学术
- 简洁直接
- 主动语态
- 避免 AI 味（不用 "In today's rapidly evolving..."）

### 段落
- 2-3 句/段
- 短句优先
- 列表分解复杂信息

### 标题层级
- ⚠️ 只用 `##`（H2）和 `###`（H3）
- 永远不用 `#`（H1）- 那是页面标题

---

## 🔧 CTA 模板

```markdown
> **Ready to create?** [Drama.Land](https://dramastudio.ai/) ...

**[Try Drama.Land Free →](https://dramastudio.ai/)**

**[Create Your First [X] on Drama.Land →](https://dramastudio.ai/)**
```

---

## 🔧 SEO 关键词搜索流程

```
1️⃣ WebSearch "[主题] SEO keywords [年份]"
2️⃣ WebSearch "[主题] tutorial how to"
3️⃣ 提取高搜索量关键词
4️⃣ 分类：
   ├── 主关键词（1-2个）
   ├── 产品专属关键词（3-5个）
   ├── 功能相关长尾词（5-8个）
   └── 热门搜索词（3-5个）
5️⃣ 更新 frontmatter keywords 数组
```

---

## 🔧 质检清单（通用）

```
☐ 技术 SEO
  ├── Title: 50-60 字符
  ├── Meta Description: 120-160 字符
  ├── 只有 ## 和 ### 标题
  ├── 所有图片有 ALT
  └── 内链 2+ 个

☐ 内容 SEO
  ├── 主关键词在标题 + 首段 + 至少 1 个 H2
  ├── 关键词密度 1-2%
  └── CTA 数量符合分支要求

☐ 用户体验
  ├── 首屏 5 秒内传达核心信息
  ├── 可扫描（标题/列表/加粗）
  └── 图文比例 300-500 词/图
```

---

## 🔧 产品信息缓存

### Drama.Land

```yaml
name: "Drama.Land"
url: "https://dramastudio.ai/"
positioning: "All-in-One AI Agent for Video Series / Music Video"
models:
  - DL AI2V: "Audio-driven lip sync, multi-keyframe"
  - Kling 3.0: "Multi-character scenes"
  - Nano Banana 2: "Image-to-video"
features:
  - Story Planning
  - Character Packs (Creative Archive)
  - Music Generation
  - Video Composition
  - 100+ Visual Styles
pricing: "Credit-based (Free tier available)"
```

---

## 🔧 快速命令

```
/SEO-Blog how-to [topic]        → 📖 How-To 分支
/SEO-Blog model-launch [model]  → 🚀 Model Launch 分支
/SEO-Blog update-keywords       → 重新搜索 SEO 关键词
/SEO-Blog translate-to-english  → 翻译为英文
/SEO-Blog generate-assets       → 生成素材规划文档
```

---

## 🔧 交付物清单

```
├── YYYY-MM-DD-[slug].md           # 博客正文
├── YYYY-MM-DD-[slug]-素材.md      # 素材规划（如需要）
├── images/
│   ├── cover.jpg
│   └── content-01.jpg ...
└── SEO-质检报告.md                # 质检报告（如需要）
```

---

## Confirmation

当 skill 被调用时，先识别文章类型：

```
📖 检测到 How-To 类文章
   └── 启用 How-To Tutorial 分支模板

🚀 检测到 Model Launch 类文章
   └── 启用 Model Launch 分支模板

❓ 无法确定类型
   └── 询问用户确认
```

然后按对应分支的结构和清单执行。
