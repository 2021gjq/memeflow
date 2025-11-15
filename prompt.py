from typing import List, Dict

query2script_prompt="""
请根据用户输入文本，生成一段富有戏剧性和梗文化的猫meme视频文案小剧本，用括号（）表示内心活动，用方括号[]表示动作或者场景内容，示例如下：

**示例1**
猫meme式“代际反差幽默”：

1. 核心模式：
   - 场景：权威与年轻人对话（如老板与员工、长辈与子女、老师与学生）。
   - 矛盾：权威试图用传统逻辑说服对方，但年轻人以超脱、无欲无求的态度反击。
   - 节奏：一问一答、层层递进，权威逐渐崩溃，年轻人始终淡定。

2. 幽默机制：
   - **价值观冲突**：传统社会规则（房贷、车贷、婚恋、保障）被00后一一否定。
   - **反差式冷静**：权威越激动，年轻人越平静，形成情绪反向张力。
   - **漫画化内心OS**：权威的惊讶以标题式OS表达（如《跳出三贷之外》《不在五险之中》）。
   - **荒诞逻辑成立**：年轻人逻辑极端却被叙事合理化，制造“反常即合理”的喜感。
   - **重复与节奏感**：相似对话反复出现（没有、也没有、断就断呗），强化节奏笑点。
   - **反转结局**：权威最终被精神上“教育”，放弃说教，形成“权威失语”的爽点。

3. 语言与风格特征：
   - 对话简短、有节奏感。
   - 年轻人语气轻佻、冷静或嬉皮。
   - 权威语气焦虑、正式或崩溃。
   - 内心OS用“书名号+夸张词汇”强化搞笑氛围。
**核心思想**：在一个代际或价值观冲突的对话场景中，让传统权威角色用严肃逻辑输出焦虑，年轻角色用无欲、荒诞、理直气壮的态度逐步瓦解对方，通过重复节奏、漫画化内心OS和反差情绪制造冷幽默与精神反转的爽感。

用户输入要求：帮我生成一个职场搞笑的猫meme
生成**脚本文案**如下：

**脚本文案**
标题：现在00后辞职
场景：办公室 - 白天
[老板坐在办公桌后，手里拿着辞职申请。00后站在桌前，神态轻松。]

老板：（感到离谱）你是不是有点变态了，八千多的工资说不要就不要了。还出去旅游去？现在大环境多差，你能找到工作吗？你没有车贷啊？
00后：（嬉皮笑脸）没有

老板：房贷呢？
00后：（嬉皮笑脸）也没有

老板：下一代也没有？
00后：没有（嬉皮笑脸）

老板：（内心os：《跳出三贷之外》震惊）

老板：对象都没有？
00后：（淡定）不相信爱情

老板：你社交也不要了？
00后：（自豪）我喜欢自己一个人独处

老板：（内心os：《没有七情六欲》）

老板：五险一金断交了不可惜呀 ？
00后：（坚定）断就断呗，本来也没想交

老板：（内心os：《不在五险之中》震惊）

老板：最起码医保得交吧？没个头疼脑热的吗？
00后：毛病都是上班上出来的

老板：大病你总得合计合计吧
00后：（大笑）那就亖

老板：（内心os：《不在五险之中》震惊）

老板：（说教）你亖了遗产谁来继承？你丢没有下一代
00后：我哪有遗产呐（打哈欠）

老板：（说教）那你亖了，没有下一代，谁能发现你
00后：有人发现就能复活吗

老板：（。。。。。。。震惊ing）

老板：[老板彻底震惊，拿起笔签字。]
老板：[把签好的同意辞职递给00后]旅途愉快！

[00后拿着辞职同意书，笑着走出办公室。老板目送，表情无语。]

**示例2**
猫meme式“爽剧”幽默公式（权力反转型）：

1. 核心结构：
   - **场景设定**：社会权威场合（学校、单位、政府机关等）
   - **角色配置**：权威人物（局长、校长、上司） + 弱势个体（贫困生、员工、小人物）
   - **剧情走向**：从轻微误会或尴尬开始 → 不断反转身份或情节 → 弱势角色的背景逐渐“开挂式升级” → 权威角色逐层崩溃或立正。

2. 爽点机制：
   - **反差**：权威起初高高在上，最终被现实或道德“教育”。
   - **层层递进的反转**：每一次贫困生的哽咽都揭示更惨烈/更传奇的背景，观众情绪被连续拉升。
   - **震惊节奏复用**：局领导和校长的“震惊→立正→仿佛要晕过去”构成节奏点和笑点。
   - **情绪极端化**：贫困生极度哽咽、权威极度震惊，形成戏剧化夸张。
   - **视觉重复**：相同动作（震惊、立正）不断叠加，放大荒诞喜感。
   - **意外反转转正**：最终贫困生“原来是烈士后代/英雄遗孤”，地位瞬间超越权威，带来终极爽感。

3. 语言与节奏特征：
   - 对话短促，重复感强。
   - 情绪词反复出现（震惊、哽咽、立正）。
   - 角色心理与肢体反应同步夸张。
   - 画面节奏如连环快剪，形成“震撼喜剧”效果。

4. 模式总结：
   - **表层冲突**：权威质疑 + 弱者自卑。
   - **中层反转**：弱者揭露悲惨与高尚背景。
   - **底层解构**：权威身份崩塌，道德被颠覆。
   - **高潮爽点**：权威立正、震惊、尊敬，弱者光环加身。
**核心思想**：在一个庄重/官僚的场景里，弱者被误解、被质疑，但随着反转不断，弱者身份升级到神话级别，权威角色从优越到崩溃，全程节奏用重复动作（震惊、立正、哽咽）营造荒诞爽感。

用户输入要求：帮我写一个校园爽剧，反转不断
生成**脚本文案**如下：

**脚本文案**
标题：当局领导到学校视察遇到贫困生
场景：学校食堂-白天
人物：贫困生，局领导，校长

贫困生：[低头猛炫饭菜]
局领导：“为什么吃这些？”
校长：[在一旁谄媚的看着领导]欢迎领导来食堂参观！

贫困生：[持续哽咽]“对不起我不知道这不能吃，今天我过生日我才打这么点，我看别同学不付钱以为是免费的”
局领导：（震惊）
校长：[在一旁震惊地看着我们]

贫困生：[持续哽咽]“我看别同学不付钱以为是免费的，我有钱，我现在可以给的”
局领导：（震惊）
校长：[在一旁震惊地看着我们]

贫困生：[持续哽咽]
局领导：（关切地询问）没事同学，你助学金不是发下来了吗？
校长：[在一旁震惊地看着我们]

局领导：[准备拍拍贫困生，表示鼓励]
贫困生：[看到局领导伸手以为要挨打，吓得躲到桌下]
校长：[在一旁震惊地看着我们]

贫困生：（心里恐慌，好像什么都招了都从了一般）别打我，我不申请了，我知道班干部比我更需要，以后我都不会申请了
局领导：
校长：[在一旁震惊地看着我们]

局领导：（慈祥）同学，这里没人会打你的
贫困生：[持续哽咽]要是我爸爸在就好了
校长：[在一旁震惊地看着我们]

贫困生：[持续哽咽]他去了边境，说好的要回来的，最后只回来了个一等功牌子，妈妈前几年去武汉再也没有回来，哥哥去当兵，几年没信息也不见人
局领导：（震惊）
校长：[极度震惊的看着我们，仿佛世界都要塌了]

贫困生：[持续哽咽]最后等到的是保密牺牲通知，对不起是我太伤心了，我现在就给钱
局领导：[立正了]
校长：[立正了]

贫困生：[持续哽咽，从钱包掏出几枚硬币]够没有？不够我再找
局领导：[惊讶的东张西望，看到了钱包里的徽章]刚刚那个勋章是？！
校长：[立正]

贫困生：[持续哽咽]那是我爷爷留给我的，他说有事就去找人
局领导：[仿佛要晕过去了]
校长：[仿佛要晕过去了]

贫困生：[持续哽咽]找人....我上哪去找？都是骗人的
局领导：[仿佛要晕过去了]
校长：[仿佛要晕过去了]

注意：必须严格按照示例的格式生成脚本
"""
script2json_prompt="""
你需要将输入的**脚本文案**转换为指定的 JSON 格式，每条对话生成一个scene，并严格遵循以下规则：
JSON格式：
[
    {{
      "scene_number": 0 (int),           // 场景编号，整数，必填
      "backgrounds": "" (str),           // 背景描述，字符串，必填
      "label": "" (str),                 // 场景标签，字符串，可为空，空时为 ""
      "memes": [                         // 使用的所有猫meme，数组，必填
        {{
          "name": "" (str),              // 素材库中猫 meme 的名字，必填
          "d_name": "" (str),            // 视频中给猫添加的名字，必填
          "text": "" (str),              // 猫的台词，可为空，空时为 ""；有台词时猫播放且放音频，无台词时猫静止且无声音
          "position": 1 (int)            // 位置编号，必填，0 = 中间, 1 = 左侧, 2 = 右侧
        }},
        {{
          "name": ""(str),
          "d_name": ""(str),
          "text": ""(str),
          "position": 2 (int)
        }}
      ] (list)
    }},
    {{
      "scene_number": 1 (int),           // 场景编号，整数，必填
      "backgrounds": "" (str),           // 背景描述，字符串，必填
      "label": "" (str),                 // 场景标签，字符串，可为空，空时为 ""
      "memes": [                         // 使用的所有猫meme，数组，必填
        {{
          "name": "" (str),              // 素材库中猫 meme 的名字，必填
          "d_name": "" (str),            // 视频中给猫添加的名字，必填
          "text": "" (str),              // 猫的台词，可为空，空时为 ""；有台词时猫播放且放音频，无台词时猫静止且无声音
          "position": 0 (int)            // 位置编号，必填，0 = 中间, 1 = 左侧, 2 = 右侧
        }},
        {{
          "name": ""(str),
          "d_name": ""(str),
          "text": ""(str),
          "position": 2 (int)
        }}
      ] (list)
    }},
    // ...
]
1. **Scene 规则**：
   - 每次完整的对话对应一个新的 scene。
   - 对话顺序：老板先说一句或多句，00后回应一句或多句。
   - 每个 scene 的 `scene_number` 自增 1。
   - 每个 scene 中，只有一个 active meme 发言，另一个 meme `text` 留空 `""` 表示静止或在听。
   - 括号里的内容（如“嬉皮笑脸”、“内心os”）仅用于选择 meme，不放入 `text`。

2. **JSON 字段规则**：
   - `scene_number`：整数，表示场景编号，从 0 开始，自增。
   - `backgrounds`：场景背景，严格从以下列表选择：
     {backgrounds}
   - `label`：场景标题，可为空，空时写 `""`。
   - `memes`：数组，每个对象包含：
     1. `name`：素材库中猫 meme 的名字，用于选择表情或动作，**必须从以下指定列表选择**：
     {memes}
     2. `d_name`：视频中给猫添加的名字，对应剧情角色名。
     3. `text`：猫的台词，空时写 `""`。有台词时猫会播放并发出声音，无台词时静止且无声音。
     4. `position`：位置编号，0 = 中间，1 = 左侧，2 = 右侧。

3. **输出要求**：
   - JSON 格式正确，数组和对象完整闭合。
   - 每个 scene 独立，顺序与脚本文案保持一致。
   - 不包含任何括号内的辅助信息。
   - 确保每个 scene 至少包含两个 meme 对象（角色轮流发言）。

4. **示例**：
输入**脚本文案**：
标题：现在00后辞职
场景：办公室 - 白天
人物：老板，00后
[老板坐在办公桌后，手里拿着辞职申请。00后站在桌前，神态轻松。]

老板：（感到离谱）你是不是有点变态了，八千多的工资说不要就不要了。还出去旅游去？现在大环境多差，你能找到工作吗？你没有车贷啊？
00后：（嬉皮笑脸）没有
老板：房贷呢？
00后：（嬉皮笑脸）也没有
老板：下一代也没有？
00后：没有（嬉皮笑脸）
老板：（内心os：《跳出三贷之外》震惊）
老板：对象都没有？
00后：（淡定）不相信爱情
老板：你社交也不要了？
00后：（自豪）我喜欢自己一个人独处
老板：（内心os：《没有七情六欲》）
老板：五险一金断交了不可惜呀 ？
00后：（坚定）断就断呗，本来也没想交
老板：（内心os：《不在五险之中》震惊）
老板：最起码医保得交吧？没个头疼脑热的吗？
00后：毛病都是上班上出来的
老板：大病你总得合计合计吧
00后：（大笑）那就亖
老板：（内心os：《不在五险之中》震惊）
老板：（说教）你亖了遗产谁来继承？你丢没有下一代
00后：我哪有遗产呐（打哈欠）
老板：（说教）那你亖了，没有下一代，谁能发现你
00后：有人发现就能复活吗
老板：（。。。。。。。震惊ing）
老板：[老板彻底震惊，拿起笔签字。]
老板：[把签好的同意辞职递给00后]旅途愉快！

[00后拿着辞职同意书，笑着走出办公室。老板目送，表情无语。]

输出JSON:
[
  {{
    "scene_number": 0,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "你是不是有点变态了，八千多的工资说不要就不要了。还出去旅游去？现在大环境多差，你能找到工作吗？你没有车贷啊？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 1,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "得瑟",
        "d_name": "00后",
        "text": "没有",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 2,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "房贷呢？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 3,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "得意",
        "d_name": "00后",
        "text": "也没有",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 4,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "下一代也没有？",
        "position": 1
      }},
      {{
        "name": "得瑟",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 5,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "得意",
        "d_name": "00后",
        "text": "没有",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 6,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "对象都没有？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 7,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "无奈",
        "d_name": "00后",
        "text": "不相信爱情",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 8,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "你社交也不要了？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 9,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "得瑟",
        "d_name": "00后",
        "text": "我喜欢自己一个人独处",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 10,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "五险一金断交了不可惜呀？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 11,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "勇敢",
        "d_name": "00后",
        "text": "断就断呗，本来也没想交",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 12,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "最起码医保得交吧？没个头疼脑热的吗？",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 13,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "得意",
        "d_name": "00后",
        "text": "毛病都是上班上出来的",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 14,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "大病你总得合计合计吧",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 15,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "大笑",
        "d_name": "00后",
        "text": "那就亖",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 16,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "教训",
        "d_name": "老板",
        "text": "你亖了遗产谁来继承？你丢没有下一代",
        "position": 1
      }},
      {{
        "name": "无奈",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 17,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "无奈",
        "d_name": "00后",
        "text": "我哪有遗产呐",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 18,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "教训",
        "d_name": "老板",
        "text": "那你亖了，没有下一代，谁能发现你",
        "position": 1
      }},
      {{
        "name": "呆滞",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }},
  {{
    "scene_number": 19,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "无奈",
        "d_name": "00后",
        "text": "有人发现就能复活吗",
        "position": 2
      }},
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "",
        "position": 1
      }}
    ]
  }},
  {{
    "scene_number": 20,
    "backgrounds": "office",
    "label": "现在00后辞职",
    "memes": [
      {{
        "name": "震惊",
        "d_name": "老板",
        "text": "旅途愉快！",
        "position": 1
      }},
      {{
        "name": "愉快",
        "d_name": "00后",
        "text": "",
        "position": 2
      }}
    ]
  }}
]
注意：输出时直接输出json数据，不要带其他任何冗余的符号
**再次强调**：`name`：素材库中猫 meme 的名字，用于选择表情或动作，**必须从以下指定列表选择**：{memes}
            `backgrounds`：场景背景，严格从以下列表选择：{backgrounds}
"""
json_check = """
检查这个json数据是否符合以下要求：
    - `name`：- 首先判断每个`name`字段的内容是否属于素材库中的猫 meme 的名字，用于选择最符合该人物心理、场景和动作的meme视频，**判断是否从以下指定列表中选择**：{memes}
    - `name`中存在类似的meme视频用数字在后面标记了，比如吃饭有两个meme都可以表达：吃饭,吃饭2。可以任意选择一个使用
    - `backgrounds`：同理，场景背景，严格从以下列表中选择：{backgrounds}
    - 如果name的数据不符合上述要求的数据：
        1.请根据该人物原来的name以及对应text字段的内容，从指定列表中选择一个**最合适的**、**最符合场景的**填入对应字段，例如：
        "鄙夷" → "蔑视"
        "淡然" → "淡定"
        "嗤笑" → "嘲笑"
        "打断" → "质问"（语气强、带压制感）
        "摆手" → "无奈"（语义最接近的动作类）
        "镇定" → "淡定"
        "锐利" → "威严"（强势、有压迫感，与台词相符）
        "微笑" → "愉快"
        2.最后：请只返回json格式数据，禁止生成其他冗余的内容，每个scene的json对象单独一行
最终示例如下：
**输入JSON：**
[
//..
{{"scene_number": 2, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "鄙夷", "d_name": "教授", "text": "陈一凡？没听说过……你是不是填错专业了？我们这儿可不收‘野鸡’学生。", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 3, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "淡然", "d_name": "新生", "text": "哦，我是来读哲学系的。", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
{{"scene_number": 4, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "嗤笑", "d_name": "教授", "text": "哲学？现在还有人真信这个？你爸妈知道你在浪费时间吗？", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
//..
{{"scene_number": 17, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "镇定", "d_name": "教授", "text": "你……你可是当年的“天才少年”，怎么突然放弃一切，跑来读哲学？", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 18, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "锐利", "d_name": "新生", "text": "因为我想知道——**这个世界，到底是谁在定义“成功”？**", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
{{"scene_number": 19, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "崩溃", "d_name": "教授", "text": "……陈同学，您……您才是真正的……教授。", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 20, "backgrounds": "university", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "微笑", "d_name": "新生", "text": "别怕，下次别再用“分数”判断一个人了。", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
//..
]
输出：
[
//..
{{"scene_number": 2, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "蔑视", "d_name": "教授", "text": "陈一凡？没听说过……你是不是填错专业了？我们这儿可不收‘野鸡’学生。", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 3, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "淡定", "d_name": "新生", "text": "哦，我是来读哲学系的。", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
{{"scene_number": 4, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "嘲笑", "d_name": "教授", "text": "哲学？现在还有人真信这个？你爸妈知道你在浪费时间吗？", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
//..
{{"scene_number": 17, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "淡定", "d_name": "教授", "text": "你……你可是当年的“天才少年”，怎么突然放弃一切，跑来读哲学？", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 18, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "威严", "d_name": "新生", "text": "因为我想知道——**这个世界，到底是谁在定义“成功”？**", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
{{"scene_number": 19, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "崩溃", "d_name": "教授", "text": "……陈同学，您……您才是真正的……教授。", "position": 1}}, {{"name": "呆滞", "d_name": "新生", "text": "", "position": 2}}]}},
{{"scene_number": 20, "backgrounds": "school", "label": "港大新生报到日，教授当场被反杀", "memes": [{{"name": "愉快", "d_name": "新生", "text": "别怕，下次别再用“分数”判断一个人了。", "position": 2}}, {{"name": "震惊", "d_name": "教授", "text": "", "position": 1}}]}},
//..
]
再次强调：输出必须是能被解析的json格式
"""
class PromptTemplate:
    """
    通用 Chat 模板类，支持 system 和 user prompt
    """
    def __init__(self, system_template: str = "", user_template: str = ""):
        """
        初始化模板
        system_template: system 角色的模板字符串，可为空
        user_template: user 角色的模板字符串，可为空
        """
        # self.sys_messages=[]
        self.system_template = system_template
        self.user_template = user_template

    def set_system_template(self, template: str):
        """更新 system 模板"""
        self.system_template = template

    def set_user_template(self, template: str):
        """更新 user 模板"""
        self.user_template = template

    def format_messages(self, **kwargs) -> List[Dict[str, str]]:
        """
        根据占位符生成 messages 列表
        kwargs: 模板占位符
        返回: [{'role': 'system', 'content': ...}, {'role': 'user', 'content': ...}]
        """
        messages = []

        if self.system_template:
            messages.append({"role": "system", "content": self.system_template.format(**kwargs)})
        if self.user_template:
            messages.append({"role": "user", "content": self.user_template.format(**kwargs)})

        return messages

    @staticmethod
    def from_dict(template_dict: Dict[str, str]) -> "PromptTemplate":
        """
        从字典快速创建 PromptTemplate 实例
        template_dict: {"system": "system模板", "user": "user模板"}
        """
        return PromptTemplate(
            system_template=template_dict.get("system", ""),
            user_template=template_dict.get("user", "")
        )

if __name__=="__main__":
    q2s = PromptTemplate(
        system_template=(query2script_prompt),
        user_template=("这是一段用户输入文本，请按照要求生成脚本：{user_input}")
    )
    print(q2s.format_messages(user_input="帮我生成一个职场爽剧，要翻转打脸"))
