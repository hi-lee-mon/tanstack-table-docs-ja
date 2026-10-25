---
id: row_getToggleSelectedHandler
title: row_getToggleSelectedHandler
---

```ts
function row_getToggleSelectedHandler<TFeatures, TData>(row, opts?): (e) => void;
```

定義元: [features/row-selection/rowSelectionFeature.utils.ts:697](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.utils.ts#L697)

この行を選択または選択解除する、チェックボックス用のハンドラーを作成します。

行が選択できない場合、ハンドラーは何もしません。ハンドラーは `event.target.checked` を読みます。
Shift キーを押したイベントでは、このテーブルで直近に処理された選択可能な行から数えた両端を含む範囲を、選択または選択解除します。
変更を表示順の範囲に明示的に含まれる行だけに絞るには `selectChildren: false` を、行を選択解除したときに祖先の行 ID も選択から取り除くには `deselectParents: true` を渡してください。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### row {#row}

[`Row`](../../index/type-aliases/Row.md)\<`TFeatures`, `TData`\>

### opts? {#opts}

[`ToggleSelectedOptions`](../../index/interfaces/ToggleSelectedOptions.md)

## 戻り値 {#returns}

(`e`) => `void`

## 例 {#example}

```ts
const onChange = row_getToggleSelectedHandler(row)
```
