# 术语中英对照

| 中文 | 英文 | 说明 |
|---|---|---|
| 计算机视觉 | computer vision | 本书主题 |
| 图像分类 | image classification | 单标签/多标签 |
| 目标检测 | object detection | 输出边界框与类别 |
| 语义分割 | semantic segmentation | 逐像素分类 |
| 实例分割 | instance segmentation | 区分同类个体 |
| 全景分割 | panoptic segmentation | 语义 + 实例 |
| 关键点检测 | keypoint detection | 人体姿态等 |
| 深度估计 | depth estimation | 单目/双目/多视图 |
| 光流 | optical flow | 像素级运动 |
| 多目标跟踪 | multi-object tracking | MOT |
| 图像生成 | image generation | 扩散模型等 |
| 视觉-语言模型 | vision-language model | VLM |
| 开放词汇 | open-vocabulary | 不限定闭集类别 |
| 零样本 | zero-shot | 未见类别/任务 |
| 少样本 | few-shot | 少量标注 |
| 自监督学习 | self-supervised learning | 无需人工标签 |
| 对比学习 | contrastive learning | 拉近正样本、推远负样本 |
| 迁移学习 | transfer learning | 预训练到下游 |
| 微调 | fine-tuning | 更新部分或全部参数 |
| 参数高效微调 | parameter-efficient fine-tuning | PEFT，如 LoRA |
| 线性探测 | linear probe | 冻结 backbone 只训练分类头 |
| 骨干网络 | backbone | 特征提取器 |
| 颈部 | neck | 特征融合模块 |
| 检测头 | head | 输出预测 |
| 感受野 | receptive field | 输出单元对应的输入区域 |
| 步幅 | stride | 卷积/池化步长 |
| 填充 | padding | 边界填充 |
| 空洞卷积 | dilated convolution | 扩大感受野 |
| 批归一化 | batch normalization | BN |
| 残差连接 | residual connection | 跳跃连接 |
| 注意力 | attention | 本书以自注意力为主 |
| 多头自注意力 | multi-head self-attention | MHSA |
| 补丁 | patch | ViT 的输入单元 |
| 位置编码 | positional encoding | 注入位置信息 |
| 数据增强 | data augmentation | 训练时变换 |
| 混合增强 | mixup / cutmix | 样本混合 |
| 标签平滑 | label smoothing | 正则化 |
| 指数移动平均 | exponential moving average | EMA |
| 混合精度 | mixed precision | AMP |
| 梯度累积 | gradient accumulation | 小显存大批量 |
| 边界框 | bounding box | 本书默认 xyxy |
| 交并比 | intersection over union | IoU |
| 非极大值抑制 | non-maximum suppression | NMS |
| 锚框 | anchor | 检测先验框 |
| 平均精度均值 | mean average precision | mAP |
| 感兴趣区域 | region of interest | RoI |
| 感兴趣区域对齐 | RoI Align | 避免量化误差 |
| 集合预测 | set prediction | DETR 范式 |
| 匈牙利匹配 | Hungarian matching | 二分图匹配 |
| 转置卷积 | transposed convolution | 上采样 |
| 空洞空间金字塔池化 | atrous spatial pyramid pooling | ASPP |
| 提示分割 | promptable segmentation | SAM 范式 |
| 点云 | point cloud | 3D 数据 |
| 体素 | voxel | 3D 网格单元 |
| 柱体 | pillar | PointPillars 的编码单元 |
| 鸟瞰图 | bird's-eye view | BEV |
| 占用栅格 | occupancy grid | occupancy |
| 神经辐射场 | neural radiance field | NeRF |
| 3D 高斯泼溅 | 3D Gaussian splatting | 3DGS |
| 扩散模型 | diffusion model | DDPM/DDIM |
| 潜空间扩散 | latent diffusion | Stable Diffusion |
| 推理延迟 | inference latency | 端到端耗时 |
| 吞吐 | throughput | 单位时间样本数 |
| 量化 | quantization | INT8/FP16 等 |
| 知识蒸馏 | knowledge distillation | 大模型教小模型 |
| 剪枝 | pruning | 去除冗余参数 |
| 校准 | calibration | 置信度与准确率一致 |
| 分布外检测 | out-of-distribution detection | OOD |
| 对抗样本 | adversarial example | 对抗攻击 |
| 可解释性 | interpretability | CAM/Grad-CAM 等 |
| 数据表 | datasheet | 数据集说明 |
