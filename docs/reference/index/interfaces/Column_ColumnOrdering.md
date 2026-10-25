---
id: Column_ColumnOrdering
title: Column_ColumnOrdering
---

定義元: [features/column-ordering/columnOrderingFeature.types.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L40)

## プロパティ {#properties}

### getIndex {#getindex}

```ts
getIndex: (position?) => number;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:47](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L47)

表示中の列の中で、この列の0始まりのインデックスを探します。

`'start'`、`'center'`、`'end'` を渡すと、表示中の末端の列全体の並びではなく、その固定領域の中で数えます。

#### パラメーター {#parameters}

##### position? {#position}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns}

`number`

***

### getIsFirstColumn {#getisfirstcolumn}

```ts
getIsFirstColumn: (position?) => boolean;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:53](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L53)

この列が表示中の最初の列かどうかを判定します。

固定領域を渡すと、その領域内で最初の列かどうかを判定します。

#### パラメーター {#parameters-1}

##### position? {#position-1}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns-1}

`boolean`

***

### getIsLastColumn {#getislastcolumn}

```ts
getIsLastColumn: (position?) => boolean;
```

定義元: [features/column-ordering/columnOrderingFeature.types.ts:59](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-ordering/columnOrderingFeature.types.ts#L59)

この列が表示中の最後の列かどうかを判定します。

固定領域を渡すと、その領域内で最後の列かどうかを判定します。

#### パラメーター {#parameters-2}

##### position? {#position-2}

  \| [`ColumnPinningPosition`](../type-aliases/ColumnPinningPosition.md)
  \| `"center"`

#### 戻り値 {#returns-2}

`boolean`
