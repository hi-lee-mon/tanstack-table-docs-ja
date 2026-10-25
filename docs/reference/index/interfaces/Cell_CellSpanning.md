---
id: Cell_CellSpanning
title: Cell_CellSpanning
---

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:139](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L139)

## プロパティ {#properties}

### getColSpan {#getcolspan}

```ts
getColSpan: () => number;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:147](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L147)

描画時にこのセルが結合する列の数です。結合しない場合は `1`、他のセルの列の結合に覆われている場合は `0` です。

`0` を `colSpan` 属性として描画しないでください。代わりにそのセルを描画しないでください。`getIsCovered` を参照してください。

#### 戻り値 {#returns}

`number`

***

### getIsCovered {#getiscovered}

```ts
getIsCovered: () => boolean;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:153](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L153)

他のセルの結合がこのセルを覆っているかどうかです。覆われたセルは描画しないでください。内容と結合の属性は、覆っている側のセルが持ちます。

#### 戻り値 {#returns-1}

`boolean`

***

### getRowSpan {#getrowspan}

```ts
getRowSpan: () => number;
```

定義元: [features/cell-spanning/cellSpanningFeature.types.ts:163](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.types.ts#L163)

描画時にこのセルが結合する行の数です。結合しない場合は `1`、上にある結合セルに覆われている場合は `0` です。`header.rowSpan` と同じ決まりです。

`0` を `rowSpan` 属性として描画しないでください。HTML では `rowspan="0"` は「行グループの最後まで結合する」という意味になり、テーブルのセクション全体にわたってセルが下へ結合されてしまいます。代わりにそのセルを描画しないでください。`getIsCovered` を参照してください。

#### 戻り値 {#returns-2}

`number`
