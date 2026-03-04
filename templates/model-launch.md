# Model Launch Blog Template

当产品接入新模型时，使用此模版生成发布博客文章。

## Usage

```
/model-launch-blog [模型名称] [产品名称]
```

示例：
- `/model-launch-blog Nano Banana 2 Higgsfield`
- `/model-launch-blog GPT-5 Drama.Land`

---

## Template Structure

基于 Higgsfield 官方博客结构，适用于"模型上线/接入"类文章。

```markdown
---
title: "[模型名称]: [一句话卖点]. [创意 Hook]"
date: "YYYY-MM-DD"
meta description: "[产品名] 正式接入 [模型名称]，[核心能力1] + [核心能力2]，[用户价值]。"
coverImage: "/blog/cover/YY-MM-DD-Cover-[产品名]-[模型名]-Launch.jpg"
coverImageAlt: "[产品名] 平台展示 [模型名称] 的生成效果"
category: "Product Update"
author: "[产品名] Team"
tags: ["[模型名称]", "[底层技术]", "[能力标签]", "[产品名]"]
keywords: ["[模型名称小写]", "[产品名小写]", "[能力关键词]"]
---

## 前言
[1-2句 Hook，制造好奇心或痛点共鸣]
[1句：我们接入了什么，这意味着什么]

## [模型名称] 是什么
├── 一句话定位（来自哪里，解决什么问题）
├── 核心卖点（速度/质量/能力的平衡点）
└── 与同类模型的差异化

## 能力 1: [能力名称]
├── 这个能力是什么
├── 具体表现（数据/对比）
├── 用户能用来做什么（场景）
└── [配图: 效果展示]

## 能力 2: [能力名称]
├── 同上结构
└── [配图]

## 能力 3: [能力名称]
├── 同上结构
└── [配图]

## 能力 4: [能力名称]
├── 同上结构
└── [配图]

## (可选) 能力 5-6...

## 对比: [模型名称] vs [旧版本/竞品]
| 维度 | [新模型] | [旧版本] |
|------|----------|----------|
| 速度 | xxx | xxx |
| 质量 | xxx | xxx |
| 能力 | xxx | xxx |
| 价格 | xxx | xxx |

## 在 [产品名] 里能做什么
├── 基础用法：[核心功能]
├── 进阶用法：[组合工作流]
│   ├── [模型] → [功能A]
│   ├── [模型] → [功能B]
│   └── [模型] → [功能C]
└── [配图: 工作流示意图]

## Why This Matters
├── 对用户的价值（效率/成本/质量）
├── 对市场的意义（趋势/竞争格局）
└── 对产品的意义（定位/差异化）

### 总结
[1-2句总结核心价值]

---
**想试试 [模型名称]？点击 [[产品名]](产品链接) 开始！**
```

---

## Workflow

### Step 0: 信息补全（如用户未提供网址）

```
用户输入: "/model-launch-blog Nano Banana 2 Higgsfield"

⚠️ 不要自己去搜索！先问用户要信息！

检查清单:
☐ 模型官方网址/文档？
☐ 产品官网网址？
```

**处理方式**:
```markdown
AI: "请提供以下信息：
- 模型官方网址/文档：___________
- 产品官网网址：___________"

用户: "模型是 xxx，产品是 xxx"

AI: → WebFetch 抓取分析
```

| 缺失信息 | 处理方式 |
|----------|----------|
| 模型网址 | AskUserQuestion "请提供模型官方网址或文档链接" |
| 产品网址 | AskUserQuestion "请提供产品官网网址" |
| 用户说"你自己搜" | 才用 WebSearch 搜索 |

### Step 1: 收集信息
1. 模型官方发布文档/博客（搜索或用户提供）
2. 模型核心能力列表（4-6个）
3. 产品中哪些功能使用此模型（需要产品网址）
4. 与旧版本/竞品的对比数据

### Step 2: SEO 关键词研究
```
搜索：
- "[模型名称] features capabilities"
- "[模型名称] vs [竞品]"
- "[模型名称] tutorial how to use"
```

### Step 3: 分析产品视觉风格
- 访问产品官网
- 提取：配色、字体、图像风格、调性
- 用于生成配图的 prompt

### Step 4: 生成配图
需要的图片：
1. 封面图（模型 + 产品品牌）
2. 每个能力的效果展示图
3. 对比图（可选）
4. 工作流示意图

### Step 5: 撰写内容
按模版结构填充，注意：
- 每个能力单独 section，讲透
- 有数据/对比支撑
- 有场景说明用户能做什么
- 标题要有创意 hook

### Step 6: 质量检查
- [ ] 标题有 hook，不平淡
- [ ] 每个能力有：定义 + 数据 + 场景
- [ ] 有对比（vs 旧版本或竞品）
- [ ] 有"Why This Matters"市场视角
- [ ] 有工作流/使用方法
- [ ] 配图符合品牌视觉
- [ ] CTA 明确

---

## 标题 Hook 示例

| 模型 | 平淡标题 | 有 Hook 的标题 |
|------|----------|----------------|
| Nano Banana 2 | Nano Banana 2 发布 | Nano Banana 2: Pro-Level AI Image Generation. Let's Peel It Back |
| GPT-5 | GPT-5 接入上线 | GPT-5 来了：你的创作搭档刚刚升级了大脑 |
| Veo 3.1 | Veo 3.1 视频生成 | Veo 3.1: 8 秒出片，这次连声音都有了 |
| Kling 3.0 | Kling 3.0 更新 | Kling 3.0: 电影级画质，手机就能导 |

---

## 能力命名规范

不要用技术术语，用用户能理解的语言：

| 技术术语 | 用户语言 |
|----------|----------|
| Web Grounding | 联网知识，懂最新的事 |
| Subject Consistency | 角色一致性，同一个人不变形 |
| Instruction Following | 听话，复杂指令也能懂 |
| Native 4K Resolution | 原生 4K，印刷级画质 |
| Flash Speed | 秒出图 |
| Multi-modal | 图文视频全能 |

---

## 配图策略

### 核心原则

**不要生成抽象概念图，要用 AI 生成的真实图片来证明模型能力！**

### 能力 → 场景匹配表

| 模型能力 | 推荐场景 | Prompt 关键词 |
|----------|----------|---------------|
| 高分辨率/4K | 建筑细节、纹理特写 | architectural, texture, spiral staircase |
| 文字渲染 | 带文字的场景 | billboard, sign, poster with text |
| 速度快 | 动态/航拍场景 | aerial view, motion, drone photography |
| 角色一致性 | 人物肖像 | portrait, same person multiple poses |
| 联网知识 | 真实地标/品牌 | famous landmark, recognizable location |
| 光影质量 | 戏剧性光线 | dramatic lighting, golden hour, ethereal |

### 封面图 Metaprompt

```yaml
类型: 展示模型核心能力的高质量图
风格: "[产品调性]", photorealistic, cinematic, 8K

Prompt:
"[选择一个能展示模型核心卖点的场景].
Photorealistic, cinematic lighting, 8K quality,
professional photography style."

后期处理:
- 加品牌色边框: [强调色]
- 叠加文字: "[模型名称]" + "Available now at [产品]"
- 圆角裁剪
```

### 能力展示图 Metaprompt

```yaml
类型: 多图并排，每张证明一个能力
构图: 竖版 (2-4张并排)

为每个能力生成:
  能力: [能力名称]
  场景: [根据匹配表选择]

  Prompt:
  "[场景描述], [光线], photorealistic, high detail,
  professional photography, 8K quality"

后期排版:
- 多图水平并排
- 每张下方加白色标签: "[能力名称]"
- 统一圆角 (16px)
- 深色背景
```

### Higgsfield 实战示例

```yaml
封面图:
  场景: 日本武士 + 西瓜 (创意场景，展示图像质量)
  prompt: |
    A Japanese samurai master sitting in seiza position in traditional
    wooden dojo, dark blue hakama, holding katana. Natural warm light
    from window. Watermelon on wooden stand. Photorealistic, cinematic, 8K.
  后期:
    边框: "#d1fe17" (亮黄)
    文字: "NANO BANANA 2"
    副标题: "Available now at higgsfield.ai"

能力三连图:
  - 能力: "NATIVE 4K FIDELITY"
    场景: 建筑细节
    prompt: "Dramatic spiral staircase from below, circular skylight,
            ethereal light beams, concrete, minimalist, 4K"

  - 能力: "PERFECT TEXT RENDERING"
    场景: 带文字的建筑
    prompt: "Brutalist building with billboard 'NEW AI Experience
            the Future Today', people silhouettes, blue sky"

  - 能力: "UNMATCHED GENERATION SPEED"
    场景: 航拍动态
    prompt: "Aerial red kayak on dark water with white ice patterns,
            dramatic contrast, drone photography, 8K"
```

---

## 调用示例

```
用户: /model-launch-blog Nano Banana 2 Higgsfield

AI:
1. 收集 Nano Banana 2 官方信息
2. 分析 Higgsfield 视觉风格
3. SEO 关键词研究
4. 按模版生成大纲
5. 用户确认后生成正文
6. 生成配图
7. 打包交付
```

---

## 📋 实战案例：Nano Banana 2 + Higgsfield

以下是完整的分析输出示例，供后续调用参考。

### 模型分析报告

```markdown
📊 模型分析报告

**模型名称**: Nano Banana 2 (Gemini 3.1 Flash Image)
**来源**: Google DeepMind
**发布时间**: 2026年2月

**核心能力**:
1. **原生 4K 分辨率**: 直接输出 4096x4096，无需后期放大
2. **5 角色一致性**: 同一场景最多 5 个角色保持特征一致
3. **文字渲染**: 准确渲染图片内文字，支持多语言
4. **联网知识 (Web Grounding)**: 了解最新事件、人物、品牌
5. **极速生成 (Flash Speed)**: 秒级出图
6. **指令遵循**: 复杂多条件 prompt 也能准确执行

**技术亮点**:
- 基于 Gemini 3.1 Flash 的多模态架构
- 原生高分辨率（非超分辨率放大）
- 实时知识更新能力

**与竞品对比**:
| 维度 | Nano Banana 2 | DALL-E 3 | Midjourney v6 |
|------|---------------|----------|---------------|
| 分辨率 | 4K 原生 | 1024x1024 | 1024x1024 |
| 角色一致性 | 5人 | 有限 | 有限 |
| 文字渲染 | ✅ 优秀 | ✅ 良好 | ❌ 较差 |
| 速度 | 秒级 | 10-30s | 30-60s |
```

### 产品分析报告

```markdown
📊 产品分析报告

**产品名称**: Higgsfield
**产品链接**: https://higgsfield.ai

**使用 Nano Banana 2 的功能**:
Nano Banana 2 是**图像生成**模型，生成的图片可用于以下功能：

1. **Video (图生视频)**: 生成图 → 作为视频的起始帧/参考帧
2. **Face Swap (换脸)**: 生成图 → 提供人脸素材
3. **Angles (多角度)**: 生成图 → 生成同一主体的多个角度
4. **Edit (编辑)**: 生成图 → 进行局部编辑修改
5. **Upscale (放大)**: 生成图 → 进一步超分辨率放大
6. **Outfit Swap (换装)**: 生成图 → 更换服装样式

**工作流**:
┌──────────────────┐
│  Nano Banana 2   │ ← 用户输入 Prompt
│  (图像生成)       │
└────────┬─────────┘
         │ 生成图片
         ▼
┌────────────────────────────────────────┐
│  Higgsfield 下游功能                    │
├──────────┬──────────┬─────────────────┤
│  Video   │ Face Swap│  Angles         │
│  Edit    │ Upscale  │  Outfit Swap    │
└──────────┴──────────┴─────────────────┘
```

### 视觉风格分析

```markdown
🎨 视觉风格分析

**品牌**: Higgsfield
**主色调**: #0f1113 (深黑)
**强调色**: Cyan/Teal (青色/蓝绿色)
**字体风格**: Grotesk 无衬线字体，现代感
**图像风格**:
- Glassmorphism (毛玻璃效果)
- 发光边缘和连接线
- 电影级画面质感
- 深色背景 + 高对比度
**调性**: 专业、未来感、极客、创新

**配图 Prompt 基础**:
Dark background (#0f1113), cyan/teal accent colors,
glassmorphism UI cards with subtle glow effects,
futuristic tech aesthetic, professional and modern,
cinematic quality, high contrast,
clean typography, Grotesk font style.
```

### 参考文章结构分析

```markdown
📊 参考文章结构分析

**URL**: https://higgsfield.ai/blog/Nano-Banana-2-Gemini-3.1-Flash-AI-Image-Generation

**标题结构**:
- Hook 类型: 双关语 + 产品定位
- 示例: "Nano Banana 2: Pro-Level AI Image Generation. Let's Peel It Back"
- 技巧: "Peel It Back" 双关香蕉剥皮 + 深入探索

**内容结构**:
├── 前言: 直接点明"我们接入了什么"
├── Nano Banana 2 是什么: 一句话定位
├── 能力 1: Native 4K Resolution
├── 能力 2: Subject Consistency
├── 能力 3: Text Rendering
├── 能力 4: Web Grounding
├── 能力 5: Flash Speed
├── 能力 6: Instruction Following
├── 对比表格: vs 旧版本
├── 在 Higgsfield 里能做什么: 工作流展示
├── Why This Matters: 市场视角
└── CTA: "Try!" 按钮

**写作风格**:
- 段落长度: 短（2-3句）
- 语气: 专业但不刻板，有 Hook
- 特色: 每个能力独立 section，有数据支撑

**可复用元素**:
1. 双关语标题 (Peel It Back)
2. 能力逐个展开的结构
3. 对比表格
4. "Why This Matters" 市场视角
5. 工作流图示
```

### 生成的配图 Prompt

```markdown
📷 配图 Prompt 清单

**封面图**:
"A futuristic product launch visual for Nano Banana 2 on Higgsfield platform.
Dark background (#0f1113) with cyan/teal accent glows.
Central element: stylized banana icon with digital/AI aesthetic,
surrounded by floating UI cards showing image generation results.
Glassmorphism effect, professional tech aesthetic.
16:9 aspect ratio, 4K quality."

**能力展示图 (图生视频工作流)**:
"Split screen infographic showing image-to-video workflow.
Left side: AI-generated portrait image with Nano Banana 2 label.
Right side: video player showing the same image animated.
Arrow connecting them with 'Higgsfield Video' label.
Dark background, cyan accents, glassmorphism cards.
Clean, professional infographic style."

**完整工作流图**:
"Flowchart diagram with Nano Banana 2 as central node.
Connected to 6 output nodes: Video, Face Swap, Angles, Edit, Upscale, Outfit Swap.
Dark background (#0f1113), cyan/teal glowing connection lines.
Each node as glassmorphism card with icon.
Professional infographic style, futuristic tech aesthetic."
```
