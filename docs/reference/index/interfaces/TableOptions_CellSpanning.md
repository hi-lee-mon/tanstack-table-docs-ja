---
id: TableOptions_CellSpanning
title: TableOptions_CellSpanning
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L131)

## プロパティ {#properties}

### enableCellSpanning? {#enablecellspanning}

```ts
optional enableCellSpanning?: boolean;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:136](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L136)

セルが行や列をまたいで結合できるようにします。`false` の場合、どのセルも結合数 `1` を返し、結合インデックスは作られません。既定値は `true` です。
