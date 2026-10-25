---
id: cell_getSelectionStartHandler
title: cell_getSelectionStartHandler
---

```ts
function cell_getSelectionStartHandler<TFeatures, TData, TValue>(cell, _contextDocument?): (e) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.utils.ts:1379](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.utils.ts#L1379)

このセルから選択を始めるハンドラーを作成します。

`header_getResizeHandler` と同じ作りです。有効かどうかの判定は返すクロージャーの外で1回だけ行い、クロージャーの中でもう一度確かめます。SSR や別の document への描画のために document を差し替えられます。
また、テーブルの外でドラッグを離しても終わるよう、document レベルの `mouseup` リスナーはここで登録します。

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

### \_contextDocument? {#_contextdocument}

`Document`

## 戻り値 {#returns}

(`e`) => `void`

## 例 {#example}

```tsx
<td onMouseDown={cell.getSelectionStartHandler()} />
```
