---
id: CellSelectionRange
title: CellSelectionRange
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:19](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L19)

1つの長方形のセル選択です。範囲を決める2つの角で保存されます。

Shift キーでの拡張やドラッグの間、`anchor` 側の角は動かず、`focus` 側の角が動きます。そのため、この2つの組は、正規化した最小・最大の長方形よりも多くの情報を持ちます。
角は、入れ子のオブジェクトや `rowId_columnId` のように連結したキーではなく、平坦な行 ID と列 ID で保存します。`getRowId` は利用者が指定するもので、どんな区切り文字を含む ID でも返しうるからです。

## プロパティ {#properties}

### anchorColumnId {#anchorcolumnid}

```ts
anchorColumnId: string;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:20](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L20)

***

### anchorRowId {#anchorrowid}

```ts
anchorRowId: string;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L21)

***

### focusColumnId {#focuscolumnid}

```ts
focusColumnId: string;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:22](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L22)

***

### focusRowId {#focusrowid}

```ts
focusRowId: string;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:23](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L23)

***

### operation? {#operation}

```ts
optional operation?: CellSelectionRangeOperation;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L28)

前にある範囲が作った選択を、この範囲がどう変えるかを表します。既定値は `include` です。
