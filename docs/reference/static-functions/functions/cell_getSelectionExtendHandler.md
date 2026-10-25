---
id: cell_getSelectionExtendHandler
title: cell_getSelectionExtendHandler
---

```ts
function cell_getSelectionExtendHandler<TFeatures, TData, TValue>(cell): (_e) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1458](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1458)

ドラッグ中に、アクティブな範囲をこのセルまで広げるハンドラーを作成します。

リサイズのハンドラーと違い、ここでは rAF でまとめる必要はありません。`mouseenter` は連続して発生するのではなくセルの境界をまたぐたびに1回だけ発生するので、1フレーム遅らせても強調表示が遅れるだけです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### cell {#cell}

[`Cell`](../../index/type-aliases/Cell.md)\<`TFeatures`, `TData`, `TValue`\>

## 戻り値 {#returns}

(`_e`) => `void`

## 例 {#example}

```tsx
<td onMouseEnter={cell.getSelectionExtendHandler()} />
```
