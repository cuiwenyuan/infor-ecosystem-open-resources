---
title: "LN Public Interfaces 速查 - Infor 生态开放资源导航站"
description: "Infor LN Public Interfaces (PI) 速查手册，按 Common / BusinessPartner / Item / Sales / Purchase / Finance / Manufacturing 等模块分类列出所有 PI 函数及调用模板。"
---

# LN Public Interfaces 速查

> Public Interfaces (PI) 是 LN 提供的标准业务功能方法，可在 Extension 中调用实现标准功能复用，**升级不受影响**。本手册基于 Infor LN 10.8 PI Reference Guide（2026 年 3 月版）整理。
>
> **前置阅读**：[LN 4GL 语言基础](ln-4gl-tips.md) | [LN Extension 开发实战](ln-extension-guide.md)

---

## 📋 目录

- [一、PI 调用基础](#一pi-调用基础)
- [二、异常处理模块](#二异常处理模块)
- [三、Common 通用模块](#三common-通用模块)
- [四、BusinessPartner 业务伙伴模块](#四businesspartner-业务伙伴模块)
- [五、Item 物料模块](#五item-物料模块)
- [六、Sales 销售模块](#六sales-销售模块)
- [七、Purchase 采购模块](#七purchase-采购模块)
- [八、Pricing 定价模块](#八pricing-定价模块)
- [九、Planning 计划模块](#九planning-计划模块)
- [十、Standard Costs 标准成本模块](#十standard-costs-标准成本模块)
- [十一、Manufacturing 制造模块](#十一manufacturing-制造模块)
- [十二、Calendar 日历模块](#十二calendar-日历模块)
- [十三、Warehouse 仓储模块](#十三warehouse-仓储模块)
- [十四、完整调用示例](#十四完整调用示例)

---

## 一、PI 调用基础

### 1.1 调用流程

```
1. 在 declaration 段声明 extern 函数原型
2. 在函数/section 中调用 PI 函数
3. 检查返回值（0=成功）
4. 成功：Exception.Delete(exception.id)
   失败：Exception.GetMessage() + 处理异常
```

### 1.2 参数规则

| 参数类型 | 说明 | 示例 |
|----------|------|------|
| **固定输入** | 必须按顺序传递 | `domain tccmp iFinancialCompany` |
| **固定输出** | `ref` 引用传递 | `ref domain tcamnt oTargetAmount` |
| **可变输入** | `"字段名"`, `值` 成对 | `"cadr"`, l.tccom114.cadr` |
| **可变输出** | `"字段名"`, `变量` 成对 | `"ccnt"`, l.tccom114.ccnt` |

### 1.3 `mb` 后缀说明

`mb` 后缀（如 `domain tcmcs.s999m oMsg mb`）表示该字符串参数允许返回多字节字符（中文、日文等）。

### 1.4 标准调用模板

```4gl
declaration:
    extern long SomeModule.SomeFunction(
        domain tccmp iComp,
        domain tcorno iOrder,
        ref domain tcamnt oAmount,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

| 调用
long ret
domain tcmcs.s999m oMsg mb
long oID

ret = SomeModule.SomeFunction(575, order.no, amount, oMsg, oID)
if ret = 0 then
    Exception.Delete(exception.id)
else
    Exception.GetMessage(oID, 1, oMsg)
    message("错误: " & oMsg)
    raise error
endif
```

---

## 二、异常处理模块

| 函数 | 说明 | DLL |
|------|------|-----|
| `Exception.Delete(id)` | 删除异常记录 | — |
| `Exception.GetMessage(id, seq, msg)` | 获取异常消息（seq 从 1 开始） | — |
| `Exception.NumberOfMessages(id)` | 获取异常消息数量 | — |

---

## 三、Common 通用模块

**DLL**：`tcextcomapi`

### 金额与数量转换

| 函数 | 说明 | 返回值 |
|------|------|--------|
| `Common.ConvertAmount(comp, amt, from.cur, rate.type, rate.date, to.cur, ref amt.out, ref msg, ref id)` | 货币金额转换 | 0=成功 |
| `Common.ConvertQuantity(comp, qty, from.unit, item, to.unit, ref qty.out, ref msg, ref id)` | 数量单位转换 | 0=成功 |
| `Common.ConvertPrice(comp, price, from.cur, from.unit, to.cur, to.unit, item, ref price.out, ref msg, ref id)` | 价格转换（含币种和单位） | 0=成功 |
| `Common.ConvertAmountToWords(comp, amt, cur, ref words, ref msg, ref id)` | 金额转文字（如"壹佰贰拾叁元整"） | 0=成功 |
| `Common.ConvertTime(from.unit, qty, to.unit, ref qty.out, ref msg, ref id)` | 时间单位转换 | 0=成功 |
| `Common.ConvertISODurationToSeconds(duration, ref seconds, ref msg, ref id)` | ISO 8601 工期转秒数 | 0=成功 |
| `Common.ConvertLeadTimeToISODuration(comp, item, days, ref duration, ref msg, ref id)` | 提前期天数转 ISO 工期 | 0=成功 |

### 金额计算

| 函数 | 说明 | 返回值 |
|------|------|--------|
| `Common.RoundAmount(comp, amt, cur, ref rounded, ref msg, ref id)` | 金额四舍五入 | 0=成功 |
| `Common.RoundQuantity(comp, qty, unit, item, ref rounded, ref msg, ref id)` | 数量四舍五入 | 0=成功 |
| `Common.CalculateDiscountAmounts(comp, amt, disc.pct, cur, ref disc.amt, ref net.amt, ref msg, ref id)` | 计算折扣金额 | 0=成功 |
| `Common.CalculateDueDates(comp, inv.date, terms, ref due.date, ref disc.date, ref msg, ref id)` | 计算到期日和折扣日 | 0=成功 |

### 编号与参数

| 函数 | 说明 | 返回值 |
|------|------|--------|
| `Common.GenerateFirstFreeNumber(comp, series, ref number, ref msg, ref id)` | 生成首个自由编号 | 0=成功 |
| `Common.ValidateNumberGroupSeries(comp, group, ref msg, ref id)` | 校验编号组 | 0=成功 |
| `Common.GetParameters(comp, param, ref value, ref msg, ref id)` | 获取系统参数 | 0=成功 |
| `Common.GetAdditionalEntityInfo(comp, ref msg, ref id, ...)` | 获取附加实体信息 | 0=成功 |
| `Common.GetFinancialCompanyOfEntity(entity, ref comp, ref msg, ref id)` | 获取实体所属财务公司 | 0=成功 |
| `Common.GetCurrencyRates(comp, cur, rate.type, date, ref buy.rate, ref sell.rate, ref msg, ref id)` | 获取汇率 | 0=成功 |
| `Common.GetConversionFactor(comp, item, from.unit, to.unit, date, ref factor, ref msg, ref id)` | 获取转换系数 | 0=成功 |
| `Common.GetFormattedAddress(...)` | 获取格式化地址字符串 | 0=成功 |
| `Common.GetISOCodeOfLNLanguage(lang, ref iso.code, ref msg, ref id)` | 获取 LN 语言的 ISO 代码 | 0=成功 |
| `Common.UpdateApprovedConversionFactor(comp, item, from.unit, to.unit, factor, ref msg, ref id)` | 更新已审批的转换系数 | 0=成功 |

### 地址与联系

| 函数 | 说明 | 返回值 |
|------|------|--------|
| `Address.Create(comp, bpid, role, ref msg, ref id, ...)` | 创建地址 | 0=成功 |
| `Address.StartDetail(comp, bpid, role, ...)` | 启动地址明细 Session | — |
| `Address.StartPrintByBusinessPartner(comp, bpid, ...)` | 打印业务伙伴地址 | — |
| `Contact.StartOverview(comp, bpid, ...)` | 启动联系人概览 Session | — |
| `Warehouse.StartOverview(...)` | 启动仓库概览 Session | — |

### 打印

| 函数 | 说明 |
|------|------|
| `Printing.CloseOpenReports()` | 关闭所有打开的报表 |

---

## 四、BusinessPartner 业务伙伴模块

**DLL**：`tcextcomapi`

### 数据获取

| 函数 | 说明 |
|------|------|
| `BusinessPartner.GetGeneralData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取通用数据 |
| `BusinessPartner.GetBuyFromData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取采购方数据 |
| `BusinessPartner.GetSoldToData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取收货方数据 |
| `BusinessPartner.GetShipToData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取送达方数据 |
| `BusinessPartner.GetShipFromData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取发货方数据 |
| `BusinessPartner.GetPayByData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取付款方数据 |
| `BusinessPartner.GetPayToData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取收款方数据 |
| `BusinessPartner.GetInvoiceToData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取收票方数据 |
| `BusinessPartner.GetInvoiceFromData(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取开票方数据 |
| `BusinessPartner.GetCreditLimitAndBalances(comp, bpid, dept, force, ref msg, ref id, ...)` | 获取信用额度和余额 |
| `BusinessPartner.CheckOverdueInvoices(comp, bpid, ref msg, ref id)` | 检查逾期发票 |

### Session 启动

| 函数 | 说明 |
|------|------|
| `BusinessPartner.StartOverview(...)` | 启动业务伙伴概览 |
| `BusinessPartner.StartEasyEntry(...)` | 启动简易录入 |
| `BusinessPartner.StartMultiMain(...)` | 启动多主数据 |
| `BusinessPartner.StartDetail(...)` | 启动业务伙伴明细 |
| `BuyFromBusinessPartner.StartOverview(...)` | 启动采购方概览 |
| `InvoiceToBusinessPartner.StartDetail(...)` | 启动收票方明细 |

### 其他

| 函数 | 说明 |
|------|------|
| `HoldReasons.StartOverview(...)` | 启动暂停原因概览 |
| `BillingCycle.GetInvoicedate(comp, bpcyc, ref date, ref msg, ref id)` | 获取开票日期 |
| `Series.StartOverview(...)` | 启动系列概览 |
| `Task.StartMultiMain(...)` | 启动任务多主数据 |
| `Activities.StartOverview(...)` | 启动活动概览 |

---

## 五、Item 物料模块

**DLL**：`tcextibdapi`

### 数据获取

| 函数 | 说明 |
|------|------|
| `Item.GetData(comp, item, force, ref msg, ref id, ...)` | 获取物料通用数据 |
| `Item.GetSalesData(comp, item, office, force, ref msg, ref id, ...)` | 获取销售视图数据 |
| `Item.GetPurchaseData(comp, item, office, force, ref msg, ref id, ...)` | 获取采购视图数据 |
| `Item.GetCostingData(comp, item, force, ref msg, ref id, ...)` | 获取成本视图数据 |
| `Item.GetProductionData(comp, item, site, force, ref msg, ref id, ...)` | 获取生产视图数据 |
| `Item.GetWarehousingData(comp, item, site, force, ref msg, ref id, ...)` | 获取仓储视图数据 |
| `Item.GetServiceData(comp, item, force, ref msg, ref id, ...)` | 获取服务视图数据 |
| `Item.GetOrderingData(comp, item, site, force, ref msg, ref id, ...)` | 获取订购数据 |
| `Item.GetSupplier(comp, item, ref msg, ref id, ...)` | 获取供应商信息 |
| `Item.GetRevision(comp, item, ref msg, ref id, ...)` | 获取物料版本 |
| `Item.GetLotSerialRegistration(comp, item, ref msg, ref id, ...)` | 获取批号/序列号注册信息 |
| `Item.GetPlanningTimeFenceDate(comp, item, site, ref date, ref msg, ref id)` | 获取计划时界日期 |
| `Item.ProjectPegAllowed(comp, item, ref allowed, ref msg, ref id)` | 检查是否允许项目挂钩 |

### 物料操作

| 函数 | 说明 |
|------|------|
| `Item.Copy(comp, from.item, to.item, ref msg, ref id)` | 复制物料 |
| `Item.CopySiteData(comp, item, from.site, to.site, ref msg, ref id)` | 复制站点数据 |
| `Item.CreateSerialNumber(comp, item, ...)` | 创建序列号 |
| `Item.InsertSerialNumber(comp, item, serial, ...)` | 插入序列号 |
| `Item.ConvertItemToPlanItem(comp, item, ref plan.item, ref msg, ref id)` | 物料转计划物料 |
| `Item.ConvertPlanItemToItem(comp, plan.item, ref item, ref msg, ref id)` | 计划物料转物料 |

### Session 启动

| 函数 | 说明 |
|------|------|
| `Item.StartDetail(comp, item)` | 启动物料明细 |
| `Item.StartCopy(comp, item)` | 启动物料复制 |
| `Item.StartMultiMain(...)` | 启动物料多主数据 |
| `Item.StartOverview(...)` | 启动物料概览 |
| `Item.StartWhereUsedComponent(comp, item)` | 启动物料用途查询 |
| `ItemBySite.StartDetail(...)` | 启动站点物料明细 |
| `ItemBySite.StartOverview(...)` | 启动站点物料概览 |
| `ItemPurchase.StartDetail(...)` | 启动采购物料明细 |
| `ItemPurchase.StartOverview(...)` | 启动采购物料概览 |
| `ItemPurchaseBySite.StartDetail(...)` | 启动站点采购物料明细 |
| `ItemPurchaseBusinessPartner.StartDetail(...)` | 启动物料供应商明细 |
| `ItemPurchaseBusinessPartner.StartOverview(...)` | 启动物料供应商概览 |
| `ItemPurchaseBusinessPartner.CalculateLeadTimes(...)` | 计算供应商提前期 |
| `ItemPurchaseBusinessPartner.GetSafetyTime(...)` | 获取安全时间 |
| `ItemSalesBusinessPartner.StartDetail(...)` | 启动销售物料明细 |
| `ItemSalesBusinessPartner.StartOverview(...)` | 启动销售物料概览 |
| `ItemSalesByOffice.StartOverview(...)` | 启动办公室销售物料概览 |
| `ItemPlanning.StartDetail(...)` | 启动计划物料明细 |
| `ItemPlanning.StartOverview(...)` | 启动计划物料概览 |
| `ItemSerial.CreateOrUpdate(...)` | 创建或更新序列号 |
| `ItemSerial.SetStatus(...)` | 设置序列号状态 |
| `LotAndSerialSet.StartOverview(...)` | 启动批号/序列号集概览 |
| `ItemsByManufacturerPartNumber.StartOverview(...)` | 启动制造商零件号概览 |
| `ItemByItemCodeSystem.StartOverview(...)` | 启动物料编码系统概览 |

---

## 六、Sales 销售模块

**DLL**：`tdextslsapi`

### 销售设置

| 函数 | 说明 |
|------|------|
| `Sales.GetOrderSettings(comp, office, ref msg, ref id, ...)` | 获取销售订单设置 |
| `Sales.GetGeneralSettings(comp, ref msg, ref id, ...)` | 获取通用销售设置 |
| `Sales.GetQuoteSettings(comp, office, ref msg, ref id, ...)` | 获取报价设置 |
| `Sales.GetContractSettings(comp, office, ref msg, ref id, ...)` | 获取合同设置 |
| `Sales.GetScheduleSettings(comp, ref msg, ref id, ...)` | 获取计划设置 |
| `Sales.CalculatePlannedDeliveryDate(comp, item, qty, date, office, ref del.date, ref msg, ref id)` | 计算计划交货日期 |
| `Sales.GenerateRetrobilledPriceChangeAdvices(...)` | 生成追溯性价格变更通知 |
| `Sales.StartProcessProFormaInvoices(...)` | 启动形式发票处理 |

### 销售报价

| 函数 | 说明 |
|------|------|
| `SalesQuote.Approve(comp, quno, ref msg, ref id)` | 审批报价 |
| `SalesQuote.Process(comp, quno, ref msg, ref id)` | 处理报价（转为订单） |
| `SalesQuote.StartMultiMain(...)` | 启动报价多主数据 |
| `SalesQuotes.StartOverview(...)` | 启动报价概览 |
| `SalesQuoteLine.RecalculatePriceAndDiscounts(...)` | 重新计算价格和折扣 |
| `SalesQuoteLine.StartDetail(...)` | 启动报价行明细 |

### 销售合同

| 函数 | 说明 |
|------|------|
| `SalesContract.GetTotalAmounts(comp, ccon, ref msg, ref id, ...)` | 获取合同总金额 |
| `SalesContract.StartMultiMain(...)` | 启动合同多主数据 |
| `SalesContract.StartWorkbench(...)` | 启动合同工作台 |
| `SalesContracts.StartOverview(...)` | 启动合同概览 |

### 销售计划

| 函数 | 说明 |
|------|------|
| `SalesSchedule.GetForecastQuantity(...)` | 获取预测数量 |
| `SalesSchedule.StartMultiMain(...)` | 启动销售计划多主数据 |
| `SalesScheduleLine.Reprice(...)` | 重新定价 |
| `SalesScheduleLine.RecalculatePriceAndDiscounts(...)` | 重新计算价格和折扣 |

### 销售订单

| 函数 | 说明 |
|------|------|
| `SalesOrder.Approve(comp, orno, ref msg, ref id)` | 审批销售订单 |
| `SalesOrder.Block(comp, orno, hold, ref msg, ref id)` | 阻塞/解阻销售订单 |
| `SalesOrder.CalculateAmounts(comp, orno, ref msg, ref id)` | 计算订单金额 |
| `SalesOrder.CopyBOM(comp, from.order, to.order, ref msg, ref id)` | 复制 BOM |
| `SalesOrder.CreditCheck(comp, orno, ref msg, ref id)` | 信用检查 |
| `SalesOrder.DetermineAdditionalCostLines(...)` | 确定附加费用行 |
| `SalesOrder.DetermineDefaultPurchaseOrderData(...)` | 确定默认采购订单数据 |
| `SalesOrder.FinalizeBlocking(comp, orno, ref msg, ref id)` | 完成阻塞 |
| `SalesOrder.GenerateStructure(...)` | 生成订单结构 |
| `SalesOrder.InitiateChangeRequest(comp, orno, ref msg, ref id)` | 发起变更请求 |
| `SalesOrder.RecalculatePriceAndDiscounts(comp, orno, ref msg, ref id)` | 重新计算价格和折扣 |
| `SalesOrder.ReleaseBlocking(comp, orno, ref msg, ref id)` | 释放阻塞 |
| `SalesOrder.Rush(comp, orno, ref msg, ref id)` | 加急订单 |
| `SalesOrder.StartIntakeWorkbench(...)` | 启动录入工作台 |
| `SalesOrder.StartMultiMain(...)` | 启动订单多主数据 |
| `SalesOrder.StartPrintAcknowledgement(...)` | 打印订单确认 |
| `SalesOrders.StartOverview(...)` | 启动订单概览 |

### 销售订单行

| 函数 | 说明 |
|------|------|
| `SalesOrderLine.Block(comp, orno, ponr, hold, ref msg, ref id)` | 阻塞/解阻订单行 |
| `SalesOrderLine.CalculateCostPriceByProject(...)` | 按项目计算成本价格 |
| `SalesOrderLine.Cancel(comp, orno, ponr, ref msg, ref id)` | 取消订单行 |
| `SalesOrderLine.ConfirmBackorderLine(...)` | 确认欠交行 |
| `SalesOrderLine.ConfirmSalesDelivery(...)` | 确认销售交货 |
| `SalesOrderLine.CopyFromOriginalInvoice(...)` | 从原发票复制 |
| `SalesOrderLine.CopyFromOriginalOrder(...)` | 从原订单复制 |
| `SalesOrderLine.CopyFromOriginalScheduleShipment(...)` | 从原计划装运复制 |
| `SalesOrderLine.CopyFromOriginalShipment(...)` | 从原装运复制 |
| `SalesOrderLine.CreateSalesDelivery(...)` | 创建销售交货 |
| `SalesOrderLine.ExecuteTradeComplianceCheck(...)` | 执行贸易合规检查 |
| `SalesOrderLine.GenerateProductionOrder(...)` | 生成生产订单 |
| `SalesOrderLine.GetStatusDescription(...)` | 获取状态描述 |
| `SalesOrderLine.LinkContract(...)` | 关联合同 |
| `SalesOrderLine.LinkOrUnlinkInstallationGroup(...)` | 关联/取消安装组 |
| `SalesOrderLine.RecalculatePriceAndDiscounts(...)` | 重新计算价格和折扣 |
| `SalesOrderLine.ReleaseBlocking(...)` | 释放阻塞 |
| `SalesOrderLine.ReleaseManualActivity(...)` | 释放手工活动 |
| `SalesOrderLine.ReleaseToWarehousing(...)` | 释放到仓储 |
| `SalesOrderLine.Split(...)` | 拆分订单行 |
| `SalesOrderLine.StartAutomaticProcessing(...)` | 启动自动处理 |
| `SalesOrderLine.StartDetail(...)` | 启动订单行明细 |

### 销售订单变更请求

| 函数 | 说明 |
|------|------|
| `SalesOrderChangeRequest.Approve(...)` | 审批变更请求 |
| `SalesOrderChangeRequest.Cancel(...)` | 取消变更请求 |
| `SalesOrderChangeRequest.Process(...)` | 处理变更请求 |

### 销售发票行

| 函数 | 说明 |
|------|------|
| `SalesOrderInvoiceLine.ChangePriceAndDiscounts(...)` | 变更价格和折扣 |
| `SalesOrderInvoiceLine.ReadInvoicingStatusDescription(...)` | 读取开票状态 |
| `SalesOrderInvoiceLine.ReleaseToInvoicing(...)` | 释放到开票 |

---

## 七、Purchase 采购模块

**DLL**：`tdextpurapi`

### 采购设置

| 函数 | 说明 |
|------|------|
| `Purchase.GetOrderSettings(comp, office, ref msg, ref id, ...)` | 获取采购订单设置 |
| `Purchase.GetGeneralSettings(comp, ref msg, ref id, ...)` | 获取通用采购设置 |
| `Purchase.GetRequisitionSettings(comp, ref msg, ref id, ...)` | 获取采购申请设置 |
| `Purchase.GetRFQSettings(comp, ref msg, ref id, ...)` | 获取询价设置 |
| `Purchase.GetContractSettings(comp, office, ref msg, ref id, ...)` | 获取采购合同设置 |
| `Purchase.GetScheduleSettings(comp, ref msg, ref id, ...)` | 获取采购计划设置 |
| `Purchase.GenerateRetrobilledPriceChangeAdvices(...)` | 生成追溯性价格变更通知 |

### 采购申请

| 函数 | 说明 |
|------|------|
| `PurchaseRequisition.Submit(comp, ref msg, ref id)` | 提交采购申请 |
| `PurchaseRequisition.ApproveApprovalRecord(...)` | 审批 |
| `PurchaseRequisition.RejectApprovalRecord(...)` | 驳回 |
| `PurchaseRequisition.StartMultiMain(...)` | 启动多主数据 |
| `PurchaseRequisitionLine.ConvertToPurchaseOrder(...)` | 转采购订单 |
| `PurchaseRequisitionLine.ConvertToPurchaseRFQ(...)` | 转询价单 |
| `PurchaseRequisitionLine.StartDetail(...)` | 启动申请行明细 |

### 采购合同

| 函数 | 说明 |
|------|------|
| `PurchaseContract.Activate(...)` | 激活合同 |
| `PurchaseContract.Deactivate(...)` | 停用合同 |
| `PurchaseContract.Terminate(...)` | 终止合同 |
| `PurchaseContract.GetTotalAmounts(...)` | 获取合同总金额 |
| `PurchaseContract.StartWorkbench(...)` | 启动合同工作台 |
| `PurchaseContractLine.Activate(...)` | 激活合同行 |
| `PurchaseContractLine.Deactivate(...)` | 停用合同行 |
| `PurchaseContractLine.Terminate(...)` | 终止合同行 |
| `PurchaseContractLine.GetNetAmountOnPriceDate(...)` | 获取价格日期的净额 |

### 采购询价

| 函数 | 说明 |
|------|------|
| `RequestForQuote.PrintRequestForQuote(...)` | 打印询价单 |
| `RequestForQuote.StartCancel(...)` | 启动取消 |
| `RequestForQuoteResponse.Accept(...)` | 接受报价 |
| `RequestForQuoteResponse.Reject(...)` | 拒绝报价 |

### 采购订单

| 函数 | 说明 |
|------|------|
| `PurchaseOrder.InitiateChangeRequest(...)` | 发起变更请求 |
| `PurchaseOrder.PrintPurchaseOrder(...)` | 打印采购订单 |
| `PurchaseOrder.RecalculateLandedCosts(...)` | 重新计算到岸成本 |
| `PurchaseOrder.StartAutomaticProcessing(...)` | 启动自动处理 |
| `PurchaseOrder.StartIntakeWorkbench(...)` | 启动录入工作台 |
| `PurchaseOrder.StartMultiMain(...)` | 启动多主数据 |
| `PurchaseOrder.StartPrintReminders(...)` | 打印催单 |
| `PurchaseOrders.StartOverview(...)` | 启动订单概览 |
| `PurchaseOrderLine.Approve(...)` | 审批订单行 |
| `PurchaseOrderLine.CalculatePlannedReceiptDate(...)` | 计算计划收货日期 |
| `PurchaseOrderLine.Cancel(...)` | 取消订单行 |
| `PurchaseOrderLine.ConfirmPotentialBackorder(...)` | 确认潜在欠交 |
| `PurchaseOrderLine.GetCurrentActivity(...)` | 获取当前活动 |
| `PurchaseOrderLine.ReleaseToWarehousing(...)` | 释放到仓储 |
| `PurchaseOrderLine.Split(...)` | 拆分订单行 |
| `PurchaseOrderLines.StartOverview(...)` | 启动订单行概览 |
| `PurchaseOrderReceipt.Confirm(...)` | 确认收货 |
| `PurchaseOrderReceipt.ConfirmV2(...)` | 确认收货（V2） |
| `PurchaseOrderReceipt.StartDetail(...)` | 启动收货明细 |
| `PurchasePayableReceipt.ChangePriceAndDiscountAfterReceipt(...)` | 收货后变更价格和折扣 |

### 采购计划

| 函数 | 说明 |
|------|------|
| `PurchaseSchedule.GenerateReleaseForPushAndPullForecast(...)` | 生成推拉预测发布 |
| `PurchaseSchedule.Regenerate(...)` | 重新生成 |
| `PurchaseSchedule.StartMultiMain(...)` | 启动多主数据 |
| `PurchaseSchedule.Terminate(...)` | 终止 |

---

## 八、Pricing 定价模块

**DLL**：`tdextprcap`

| 函数 | 说明 |
|------|------|
| `Pricing.CalculateAmounts(...)` | 计算定价金额 |
| `Pricing.GetGeneralSettings(...)` | 获取通用定价设置 |
| `Pricing.GetPurchaseSettings(...)` | 获取采购定价设置 |
| `Pricing.GetSalesSettings(...)` | 获取销售定价设置 |
| `Pricing.GetServiceSettings(...)` | 获取服务定价设置 |
| `Pricing.RetrievePriceBookDataForItem(...)` | 获取物料价格本数据 |
| `Pricing.SimulatePurchasePrice(...)` | 模拟采购价格 |
| `Pricing.SimulateSalesPrice(...)` | 模拟销售价格 |
| `Pricing.SimulateServicePrice(...)` | 模拟服务价格 |
| `Pricing.SimulateTransferPrice(...)` | 模拟转移价格 |

---

## 九、Planning 计划模块

| 函数 | 说明 |
|------|------|
| `PlanItem.StartATPHandling(...)` | 启动 ATP（可承诺量）处理 |
| `ItemMasterPlan.Generate(...)` | 生成物料主计划 |
| `ItemMasterPlan.StartPlan(...)` | 启动主计划 |
| `ItemMasterPlan.Update(...)` | 更新主计划 |
| `ItemOrderPlan.Get(...)` | 获取订单计划 |
| `ItemOrderPlan.StartPlan(...)` | 启动订单计划 |
| `ItemOrderPlan.StartPlanForProject(...)` | 启动项目订单计划 |
| `ItemOrderPlan.StartPlanForProjectPeg(...)` | 启动项目挂钩计划 |
| `PlannedOrder.Replan(...)` | 重计划 |
| `PlannedOrder.StartMultiMain(...)` | 启动多主数据 |
| `PlannedOrders.StartGenerate(...)` | 启动计划订单生成 |
| `PlannedOrders.StartOverview(...)` | 启动计划订单概览 |
| `PlannedOrders.TransferOrderSet(...)` | 转移订单集 |
| `PlannedProductionOrder.Transfer(...)` | 转移计划生产订单 |
| `PlannedPurchaseOrder.Transfer(...)` | 转移计划采购订单 |
| `PlannedPeggingRelations.FindDemandForOrder(...)` | 查找订单需求 |
| `PlannedPeggingRelations.FindSupplyForOrder(...)` | 查找订单供应 |
| `ProductAvailability.GetWhenAvailableSchedule(...)` | 获取可承诺量计划 |
| `OrderPegging.StartSelect(...)` | 启动挂钩选择 |

---

## 十、Standard Costs 标准成本模块

| 函数 | 说明 |
|------|------|
| `StandardCosts.Calculate(...)` | 计算标准成本 |
| `StandardCosts.CalculateAndGetStandardCost(...)` | 计算并获取标准成本 |
| `StandardCosts.CalculateForNewItem(...)` | 为新物料计算标准成本 |
| `StandardCosts.CalculateForSimulation(...)` | 模拟计算标准成本 |
| `StandardCosts.CalculateSingleItem(...)` | 计算单个物料标准成本 |
| `StandardCosts.Actualize(...)` | 实际化标准成本 |
| `StandardCosts.PrintMultilevelCostCalculation(...)` | 打印多级成本计算 |

---

## 十一、Manufacturing 制造模块

### BOM 与工艺路线

| 函数 | 说明 |
|------|------|
| `ProductionBillOfMaterial.ApproveRevision(...)` | 审批生产 BOM 版本 |
| `ProductionBillOfMaterial.CopyToJobShop(...)` | 复制到车间 |
| `ProductionBillOfMaterial.ExpireRevision(...)` | 过期生产 BOM 版本 |
| `ProductionBillOfMaterial.GenerateProductSubcontractingModel(...)` | 生成产品外协模型 |
| `ProductionBillOfMaterial.StartMultiMain(...)` | 启动多主数据 |
| `ProductionBillOfMaterial.ValidateRevision(...)` | 验证 BOM 版本 |
| `JobShopBillOfMaterial.ApproveRevision(...)` | 审批车间 BOM 版本 |
| `JobShopBillOfMaterial.Copy(...)` | 复制 |
| `JobShopBillOfMaterial.CreateNewRevision(...)` | 创建新版本 |
| `JobShopBillOfMaterial.ExpireRevision(...)` | 过期版本 |
| `JobShopBillOfMaterial.Explode(...)` | 展开 BOM |
| `JobShopRouting.ApproveRevision(...)` | 审批工艺路线版本 |
| `JobShopRouting.Copy(...)` | 复制 |
| `JobShopRouting.CopyOperations(...)` | 复制工序 |
| `JobShopRouting.CreateNewRevision(...)` | 创建新版本 |
| `JobShopRouting.ExpireRevision(...)` | 过期版本 |
| `JobShopRouting.SetUseForCosting(...)` | 设为成本计算用 |
| `JobShopRouting.SetUseForPlanning(...)` | 设为计划用 |
| `ProductVariant.GenerateStructure(...)` | 生成产品结构 |
| `ProductVariant.StartConfigurator(...)` | 启动配置器 |

---

## 十二、Calendar 日历模块

| 函数 | 说明 |
|------|------|
| `Calendar.CalculateDaysFromHours(comp, calendar, hours, ref days, ref msg, ref id)` | 工时转天数 |
| `Calendar.GetPeriodCapacity(comp, cal.code, period, ref capacity, ref msg, ref id)` | 获取期间产能 |
| `Calendar.GetWorkingDays(comp, from.date, to.date, ref days, ref msg, ref id)` | 获取工作日数 |
| `Calendar.PlanLeadTimeBackward(comp, item, date, ref start.date, ref msg, ref id)` | 反向排程 |
| `Calendar.PlanLeadTimeForward(comp, item, date, ref end.date, ref msg, ref id)` | 正向排程 |
| `Calendar.StartUpdateWorkingHours(...)` | 启动更新工作时间 |
| `Calendar.UpdateWorkingHours(...)` | 更新工作时间 |

---

## 十三、Warehouse 仓储模块

| 函数 | 说明 |
|------|------|
| `Warehouse.StartOverview(...)` | 启动仓库概览 |
| `ProductionWarehouseOrders.StartDetail(...)` | 启动生产仓库订单明细 |

---

## 十四、完整调用示例

### 14.1 销售订单审批

```4gl
declaration:
    extern long SalesOrder.Approve(
        domain tccmp iFinancialCompany,
        domain tcorno iOrder,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

function long approve_sales_order(domain tcorno i.order)
{
    long ret
    domain tcmcs.s999m oMsg mb
    long oID

    ret = SalesOrder.Approve(575, i.order, oMsg, oID)
    if ret = 0 then
        Exception.Delete(exception.id)
        message("订单 %s 审批成功", i.order)
    else
        Exception.GetMessage(oID, 1, oMsg)
        message("审批失败: " & oMsg)
        raise error
    endif

    return(ret)
}
```

### 14.2 获取业务伙伴付款方数据

```4gl
declaration:
    extern long BusinessPartner.GetPayByData(
        domain tccmp iFinancialCompany,
        domain tccom.bpid iPayByBP,
        domain tccwoc iDepartment,
        boolean iForceRead,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

function long get_pay_by_data()
{
    long ret
    domain tcmcs.s999m oMsg mb
    long oID

    ret = BusinessPartner.GetPayByData(
        575,                       | 财务公司
        "BP000001",                | 业务伙伴
        "",                        | 部门
        true,                      | 强制读取
        oMsg, oID )

    if ret = 0 then
        Exception.Delete(exception.id)
        | 数据已加载到 tccom114 表缓冲区
        message("地址: %s", tccom114.cadr)
    else
        Exception.GetMessage(oID, 1, oMsg)
        message("获取失败: " & oMsg)
    endif

    return(ret)
}
```

### 14.3 采购订单行释放到仓储

```4gl
declaration:
    extern long PurchaseOrderLine.ReleaseToWarehousing(
        domain tccmp iFinancialCompany,
        domain tcorno iOrder,
        domain tcpono iPosition,
        domain tclot iLot,
        domain tcsern iSerial,
        ref domain tcmcs.s999m oExceptionMessage mb,
        ref long oExceptionID )

function long release_to_warehouse()
{
    long ret
    domain tcmcs.s999m oMsg mb
    long oID

    ret = PurchaseOrderLine.ReleaseToWarehousing(
        575,                       | 财务公司
        tdpor401.orno,              | 采购订单号
        tdpor401.pono,              | 订单行号
        "",                        | 批号
        "",                        | 序列号
        oMsg, oID )

    if ret = 0 then
        Exception.Delete(exception.id)
        message("已释放到仓储")
    else
        Exception.GetMessage(oID, 1, oMsg)
        message("释放失败: " & oMsg)
    endif

    return(ret)
}
```

---

*最后更新：2026-05-08*

> **参考资料**：Infor LN 10.8 Public Interfaces & Process Extensions Reference Guide (On-premises), March 25, 2026
>
> 💡 如有 PI 函数遗漏或调用示例需要补充，欢迎通过 [GitHub Issue](https://github.com/cuiwenyuan/infor-ecosystem-open-resources/issues/new) 反馈！
