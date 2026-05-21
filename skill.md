# SEO Blog Generator for Drama.Land

Generate SEO-optimized blog articles following Drama.Land's content specification.

> **2026 更新：** 本 skill 已根据《Google Search Live 2026》调整。Google 已明确——
> 纯粹为排名而写的模板化内容会失去优势，真正获得优势的是有真实经验、差异化、
> genuinely useful 的内容。所有分支都必须遵守下方「核心原则」。

## Usage

```
/SEO-Blog [type] [topic]
```

**文章类型：**
- `/SEO-Blog how-to [主题]` - 教程类文章
- `/SEO-Blog model-launch [模型名]` - 模型上线类文章
- `/SEO-Blog [topic]` - 自动识别类型

---

## ⭐ 核心原则（2026 SEO 方向）

> 来源：《Google Search Live 2026》。**所有分支、所有文章都必须遵守。**

### 1. 差异化内容（Non-Commodity Content）

Google 明确弱化 commodity content——"谁都能写"的泛化通识，强化只有真正做过的人才写得出的内容。

```
✗ Commodity（被弱化）          ✓ Non-Commodity（被奖励）
─────────────────────────────────────────────────────────
"How to Make AI Anime Videos"  "我们用 Drama.Land 跑了 50 条动漫视频：
"Top 10 AI Video Tips"          最毁画面的 3 个 Prompt 错误"
泛化、模板化、缺差异化经验      真实案例、一手观察、深度分析、独家视角
```

每篇文章都要问一句：**"这篇是不是只有真正用过 Drama.Land 的人才写得出来？"**

### 2. 真实经验与 E-E-A-T

- AI 辅助写作可以，但**绝不伪造人类亲历**——不假装"我经历过""我测试过"。
- `Examples` / `Pro Tips` / `Common Mistakes` 必须基于**真实生成结果**，附真实截图与可复制 Prompt。
- 准确性第一：产品规格、模型信息、定价必须最新。
- 2026 最被看重的维度是 **Experience（一手经验）**。

### 3. 多模态优先

- 搜索正在多模态化——图片、视频 SEO 权重持续上升。
- Drama.Land 是 AI 视频产品，**博客嵌入生成的视频是最大的增量 SEO 机会**（见 🔧 视频 SEO）。
- 每篇文章都要规划三件事：**结构化数据 + 图片 SEO + 视频 SEO**。

### 4. 语义与意图 > 关键词

- 重心放 semantic relevance / topical authority / intent matching。
- 关键词密度只是参考（1–2%，不堆砌即可），**不当 KPI**。
- Google 用 BERT/RankBrain/MUM 理解整句和真实 intent，而非匹配关键词。

### 5. 反 spam / 反洗稿

- 不做 cloaking / doorway pages / scraped content / link spam。
- **不跨文章轻改写同质内容**——Google 去重后只保留 canonical version，其余降权。
- 不痴迷内链堆砌——Google：内容质量 > 内链操作。

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

**核心目标：** 让零基础用户能跟着做出来。

**2026 要求：** 不要写成"谁都能搜到的泛化教程"。教程要建立在**真实操作 Drama.Land 的经验**上——每个步骤有真实截图、真实 Prompt、真实结果；要有"踩过坑才知道"的细节。

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
   │   ├── 具体示例/Prompt（代码块）
   │   └── 真实截图（带 ALT）
   ├── Step 2 ~ Step 6: 同上结构
   └── CTA #3

4️⃣ Pro Tips（专业技巧）
   ⚠️ 基于真实测试经验，不是泛泛建议
   ├── Tip 1 + 真实示例
   ├── Tip 2 ~ Tip 5 + 真实示例

5️⃣ Examples: What You Can Create
   ⚠️ 必须基于真实生成结果，附真实截图/视频与 Prompt——不得虚构场景假装真实案例
   ├── Example 1: [真实案例] - Concept / Scenes / Result
   ├── Example 2: [真实案例]
   └── Example 3: [真实案例]

6️⃣ Common Mistakes to Avoid
   ⚠️ 基于真实踩坑，不是"想当然的错误"
   ├── Mistake 1 + 为什么错 + 怎么避免
   ├── Mistake 2 ~ Mistake 5

7️⃣ FAQ（5-7个问题）
   ├── 用用户真实搜索语言提问
   ├── 每个答案开头直接给结论（便于被 AI Overview 引用）
   └── → 生成 FAQPage 结构化数据

8️⃣ Start Creating（结尾 CTA）
   ├── 总结核心价值
   ├── 鼓励用户开始
   └── CTA #4（最终号召；高 intent 读者引导至产品/工具页）
```

---

## 📖 How-To 标题公式

```
How to [动作] + [对象]: [具体、差异化的附加价值]

⚠️ 2026 提示：附加价值要具体，避免空泛的 "Tips & Examples"。
   越能体现"独家角度/真实结果"，越不容易被判为 commodity content。

示例：
├── "How to Make AI Anime Videos: 6 Steps + Real Prompts That Work"
├── "How to Create AI Music Videos with Drama.Land (Beat-Synced)"
├── "How to Use Character Packs to Keep One Character Across Scenes"
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

☐ 真实操作素材（差异化的关键来源）
  ├── 实际在 Drama.Land 走一遍流程
  ├── 收集每步真实截图
  ├── 收集真实可用的 Prompt
  ├── 记录真实生成结果（图片/视频）
  └── 记录真实踩坑点 → 用于 Common Mistakes

☐ 竞品调研（WebSearch）
  ├── 搜索 "how to [主题] [年份]"
  ├── 搜索 "best [工具类型] [年份]"
  └── 提取竞品文章结构（用于差异化，不照抄）

☐ SEO 关键词与意图（WebSearch）
  ├── 主关键词: "how to [动作] [对象]"
  ├── 长尾/语义相关词:
  │   ├── "[对象] tutorial"
  │   ├── "[对象] step by step"
  │   ├── "best [工具类型] for [用途]"
  │   ├── "[产品名] tutorial [年份]"
  │   └── "free [工具类型]"
  ├── 确认搜索意图（教程意图）与分支匹配
  └── Tags: 3-5个

☐ 用户问题收集
  ├── 搜索 "[主题] FAQ"
  ├── 搜索 "[主题] common questions"
  └── 整理 5-7 个 FAQ（用用户真实语言）
```

---

## 📖 How-To 必须包含元素

```
☐ 产品优势部分（Why [产品]）
☐ 分步骤教程（Step 1-6）
☐ 每步骤有具体示例/Prompt（代码块）+ 真实截图（带 ALT）
☐ Pro Tips 部分（5条，基于真实测试）
☐ Examples 部分（3个真实案例，附真实截图/视频）
☐ Common Mistakes 部分（5个真实踩坑）
☐ FAQ 部分（5-7个问题）
☐ CTA 分布：开头1 + Why后1 + 教程后1 + 结尾1 = 4个
☐ 结构化数据：Article + HowTo + FAQPage schema
☐ 嵌入视频时：VideoObject schema + 视频 SEO 要求（见 🔧 视频 SEO）
☐ 图片：用 <img>/<picture>，AVIF/WebP，全部带 ALT
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

**核心目标：** 让用户理解模型价值 + 驱动试用。

**2026 要求：** 用**具体能力 + 真实生成结果**说话，不堆空洞的最高级形容词。每个能力配真实演示图/视频。

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
   │   ├── What this means for [平台]: [用户价值]
   │   └── 真实演示图/视频（带 ALT）
   ├── 能力 2 ~ 能力 3: 同上结构
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
[模型名] + [具体能力卖点] + [动作] + [平台]

⚠️ 2026 提示：避免 "The Most Powerful / The Best / Ultimate" 这类空洞最高级。
   它们读着像营销腔，损 trust。用具体、可验证的卖点。

✗ 平淡 / 空洞              ✓ 具体卖点
──────────────────────────────────────────────────────────
"Seedance 2.0 发布"        "Seedance 2.0 on Drama.Land:
"The Most Powerful Model"   Multi-Reference Video That Keeps Characters Consistent"
"Kling 3.0 更新"           "Kling 3.0 on Drama.Land: Multi-Character Scenes in One Shot"
"Nano Banana 2 上线"       "Nano Banana 2 on Drama.Land: Native 4K Image-to-Video"
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
  ├── 能力名称（用户语言，见「能力命名规范」）
  ├── 具体数据/数字
  ├── 用户场景
  └── 战略意义

☐ 真实演示素材
  ├── 用该模型在 Drama.Land 实际生成
  ├── 每个能力配一张真实效果图/视频
  └── 对比图（新 vs 旧）尽量用真实结果

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
☐ 每个能力配真实演示图/视频（带 ALT）
☐ 输入能力对比表（Input Type | Limit | What It Controls）
☐ Before vs After 用户价值表
☐ 操作流程（Step 1-5）
☐ CTA 分布：能力介绍后1 + 结尾1 = 2个
☐ 结构化数据：Article schema（+ 嵌视频则 VideoObject）
```

---

## 🚀 Model Launch Before/Now 模板

```markdown
### [能力编号]. [能力名称]

**Before:** [之前的痛点/限制]

**Now:** [新模型如何解决]

**What this means for [平台]:** [对用户的具体价值]

![Alt Text 描述真实画面内容](/blog/content/image.jpg)
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
dateModified: "YYYY-MM-DD"
meta description: "[150字符内摘要]"
coverImage: "/blog/cover/YY-MM-DD-Cover-DramaLand-keywords.jpg"
coverImageAlt: "[封面图描述]"
category: "[Tutorial/Model/Guide/News]"
author: "[作者名 + 可体现的专业身份]"
tags: ["Tag1", "Tag2", "Tag3"]
keywords: ["keyword1", "keyword2", "keyword3", ...]
---
```

> `dateModified` 用于结构化数据的 freshness 信号；内容更新时同步刷新。

---

## 🔧 文件命名规范

```
文章文件:   YYYY-MM-DD-english-keyword.md
封面图:     YY-MM-DD-Cover-DramaLand-keyword1-keyword2.[webp/avif]
内容图:     YY-MM-DD-01-DramaLand-description.[webp/avif]
素材文档:   YYYY-MM-DD-slug-素材.md
结构化数据: YYYY-MM-DD-slug-schema.json
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
- 关键段落开头直接给结论（便于被 AI Overview 摘录引用）

### 标题层级
- ⚠️ 只用 `##`（H2）和 `###`（H3）
- 永远不用 `#`（H1）- 那是页面标题

### 真实性（2026 红线）
- AI 辅助写作可以，但**不伪造人类亲历**
- 不假装真实案例、真实测试、专业经历
- Google：反对的不是 AI，而是 fake authenticity

---

## 🔧 CTA 模板

```markdown
> **Ready to create?** [Drama.Land](https://dramastudio.ai/) ...

**[Try Drama.Land Free →](https://dramastudio.ai/)**

**[Create Your First [X] on Drama.Land →](https://dramastudio.ai/)**
```

> **意图提示：** 博客本身转化意图偏弱。高 intent 的读者，CTA 应引导到
> 具体的**产品页 / 工具页**（高转化页），而不是只停在博客。

---

## 🔧 结构化数据（Structured Data）

> 结构化数据 = 给 Google 的"机器可读内容层"，告诉它"这段内容到底是什么"。
> 不直接影响排名，但能触发富媒体结果（Rich Results）。

每篇文章按类型生成对应 JSON-LD，作为 `YYYY-MM-DD-slug-schema.json` 交付：

```
☐ Article / BlogPosting（所有文章必须）
  └── headline / author / datePublished / dateModified / image / publisher

☐ HowTo（How-To 分支）
  └── 把 Step 1-6 映射为 HowTo step（name / text / 可选 image）

☐ FAQPage（含 FAQ 段的文章）
  └── 把每个 Q&A 映射为 Question / acceptedAnswer

☐ VideoObject（嵌入视频时，见 🔧 视频 SEO）
```

注意：
- schema 字段必须与正文一致，内容更新时同步维护
- 富媒体结果不保证一定展示

---

## 🔧 图片 SEO

```
☐ 重要图片用 <img> 或 <picture>，绝不用 CSS background-image（无法可靠索引）
☐ <picture> 必须含 <img> fallback
☐ 每张图都有清晰、准确的 ALT（描述真实画面，自然含关键词）
   ✓ "rapper lip syncing in a neon cyberpunk city, made with Drama.Land"
☐ 图片周边有 caption / 描述性正文
☐ 格式优先 AVIF / WebP（质量、压缩、性能平衡最好）
☐ 图片已压缩；文件名按命名规范
☐ 图中 AI 生成的文字要准确（影响抓取与理解）
☐ 大量图片时提供 Image Sitemap
```

---

## 🔧 视频 SEO ⭐ Drama.Land 最大机会

> Drama.Land 是 AI 视频产品。博客嵌入生成的视频，是 2026 多模态搜索下最大的增量机会。
> 搜索结果正越来越多融合视频，Video SEO 的逻辑接近 YouTube SEO。

### 嵌入视频的要求

```
☐ 视频明显可见——不藏 embed、不放太靠下、不 lazy-hide
☐ 视频周边有描述性正文 / caption
☐ 重要视频建议有独立 watch page（独立 URL + 标题/描述/metadata）
```

### VideoObject 结构化数据（嵌视频必须）

```
☐ name          视频标题
☐ description   视频描述
☐ thumbnailUrl  高质量缩略图 URL（直接影响 CTR）
☐ uploadDate
☐ duration      ISO 8601 格式，如 PT2M15S（2分15秒）
☐ contentUrl    真实视频文件 URL
☐ embedUrl      嵌入地址
☐ (可选) regionsAllowed / ineligibleRegion
```

### Video Sitemap

- 嵌入式视频特别依赖 sitemap 被发现
- 可附额外字段：`family_friendly`、`restriction`（地区）

### 格式与缩略图

- 推荐 **MP4 + H.264**（兼容性最好）
- Thumbnail 高质量——影响 CTR、snippet 展示、Discover 点击率

---

## 🔧 国际化与本地化（多语言发布时）

> 触发：使用 `/SEO-Blog translate-to-english` 或发布多语言版本时。

```
☐ 各语言版本用独立 URL，推荐 subdirectory：dramastudio.ai/ja/blog/...
☐ hreflang 双向 return links：EN 页指向 JA，JA 页也必须回指 EN
☐ language / region code 必须正确：en-US、en-GB、zh-CN、zh-TW
☐ 同时指定语言 + 地区（同语言不同地区 intent 不同）
☐ 页面可见正文本身就是目标语言（Google 主要靠可见内容判断语言）
☐ 本地化 ≠ 翻译：避免机翻 SEO 页（AI Search 能识别并降权）
```

---

## 🔧 SEO 关键词与意图流程

```
1️⃣ WebSearch "[主题] [年份]" — 了解真实搜索词与问法
2️⃣ WebSearch "[主题] tutorial how to" / "[主题] FAQ"
3️⃣ 确认搜索意图（教程 / 资讯 / 对比 …）→ 匹配正确分支
4️⃣ 分类：
   ├── 主关键词（1-2个）
   ├── 产品专属关键词（3-5个）
   ├── 功能相关长尾 / 语义相关词（5-8个）
   └── 用户真实问法（用于 FAQ）
5️⃣ 更新 frontmatter keywords 数组
6️⃣ ⚠️ 重心是 semantic relevance / topical authority / intent matching，
   不是关键词覆盖率。密度 1-2% 仅作参考，不堆砌。
```

---

## 🔧 发布前自检清单（2026 版）

每篇文章发布前，逐项核对。

```
1. 内容差异化 ⭐ 最高优先级
☐ 不是 commodity content，不写"谁都能写"的泛化通识
☐ 有"只有真正做过的人才写得出"的角度（真实测试/独家观察/具体踩坑）
☐ Examples / Pro Tips / Common Mistakes 基于真实生成结果，附真实截图与 Prompt
☐ 全文有独特观点，不是竞品文章重写

2. E-E-A-T 与真实性
☐ 有真实一手经验（Experience）的体现
☐ 未伪造人类亲历（AI 辅助 OK，不假装"我经历过"）
☐ 产品规格、模型信息、定价最新且准确

3. 技术 SEO
☐ Title 50–60 字符含主关键词；Meta 120–160 字符
☐ 文件名 slug：YYYY-MM-DD-english-keyword.md，全小写连字符
☐ 只用 ## / ###，不出现 #
☐ Frontmatter 完整，category 取值正确
☐ canonical 清晰；新文章有内链指向，不成孤立页

4. 关键词与意图
☐ 主关键词在 Title + 首段 + ≥1 个 H2 + Meta + URL
☐ 重心是语义相关/意图匹配；密度 1–2% 仅参考，不堆砌
☐ 搜索意图与分支匹配（教程→How-To，资讯→Model Launch）

5. 结构化数据
☐ Article / BlogPosting schema
☐ How-To 文章 → HowTo schema
☐ 有 FAQ 段 → FAQPage schema
☐ 嵌入视频 → VideoObject schema

6. 图片 SEO
☐ 重要图用 <img>/<picture>，非 CSS background-image
☐ 每张图有清晰准确 ALT；周边有描述性文字
☐ 格式 AVIF/WebP，已压缩

7. 视频 SEO（嵌视频时）
☐ 视频明显可见，周边有描述文字
☐ VideoObject schema 完整（含 thumbnailUrl、ISO 8601 duration）
☐ 高质量 thumbnail；有 Video Sitemap

8. 国际化（多语言时）
☐ 独立 URL（subdirectory）；hreflang 双向 return links
☐ language/region code 正确；非机翻 SEO 页

9. 用户体验与转化
☐ 首屏 5 秒传达核心信息；段落 2–3 句，可扫描
☐ 图文比例 300–500 词/图
☐ CTA 服务真实价值（How-To 4个 / Model Launch 2个），链接正确
☐ 高 intent 读者引导到产品页/工具页
☐ 品牌信号清晰（Site Name、作者身份）

10. 发布前最终核对
☐ 与站内已有文章无轻改写/同质化（避免 canonical 降权）
☐ 不触碰 spam（cloaking / doorway / scraped content / link spam）
☐ 拼写语法检查；链接无 404；日期一致；交付物齐全
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

> ⚠️ 模型、功能、定价随产品迭代变化——撰文前核对官网，确保 accuracy。

---

## 🔧 快速命令

```
/SEO-Blog how-to [topic]        → 📖 How-To 分支
/SEO-Blog model-launch [model]  → 🚀 Model Launch 分支
/SEO-Blog update-keywords       → 重新搜索 SEO 关键词与意图
/SEO-Blog translate-to-english  → 翻译为英文（遵守 🔧 国际化 规范）
/SEO-Blog generate-assets       → 生成素材规划文档
/SEO-Blog generate-schema       → 生成结构化数据 JSON-LD
```

---

## 🔧 交付物清单

```
├── YYYY-MM-DD-[slug].md              # 博客正文
├── YYYY-MM-DD-[slug]-素材.md         # 素材规划（如需要）
├── YYYY-MM-DD-[slug]-schema.json     # 结构化数据 JSON-LD
├── images/
│   ├── cover.[webp/avif]
│   └── content-01.[webp/avif] ...
├── videos/                           # 嵌入视频（如有）+ thumbnail
└── SEO-质检报告.md                   # 对照「发布前自检清单」（如需要）
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

然后按对应分支的结构和清单执行，**全程遵守「⭐ 核心原则（2026 SEO 方向）」**，
并在交付前对照「🔧 发布前自检清单（2026 版）」逐项核对。
