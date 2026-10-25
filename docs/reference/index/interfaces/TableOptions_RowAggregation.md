---
id: TableOptions_RowAggregation
title: TableOptions_RowAggregation
---

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:329](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L329)

`rowAggregationFeature` が追加するテーブルのオプションです。

## プロパティ {#properties}

### manualAggregation? {#manualaggregation}

```ts
optional manualAggregation?: boolean;
```

定義元: [features/row-aggregation/rowAggregationFeature.types.ts:335](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-aggregation/rowAggregationFeature.types.ts#L335)

列の上書きが要求を処理しなかった場合に、ローカルで `column.getAggregationValue()` を計算しないようにします。手動でグループ化した行が持つグループの値は、引き続きデータの持ち主が責任を持ちます。
