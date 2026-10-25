---
id: Row_ColumnPinning
title: Row_ColumnPinning
---

定義元: [features/column-pinning/columnPinningFeature.types.ts:80](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L80)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## プロパティ {#properties}

### getCenterVisibleCells {#getcentervisiblecells}

```ts
getCenterVisibleCells: () => Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:87](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L87)

列が先頭にも末尾にも固定されていない、表示中の行のセルを取得します。

#### 戻り値 {#returns}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getEndVisibleCells {#getendvisiblecells}

```ts
getEndVisibleCells: () => Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:95](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L95)

列が論理的な末尾に固定されている、表示中の行のセルを取得します。

#### 戻り値 {#returns-1}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]

***

### getStartVisibleCells {#getstartvisiblecells}

```ts
getStartVisibleCells: () => Cell<TFeatures, TData, unknown>[];
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L91)

列が論理的な先頭に固定されている、表示中の行のセルを取得します。

#### 戻り値 {#returns-2}

[`Cell`](../type-aliases/Cell.md)\<`TFeatures`, `TData`, `unknown`\>[]
