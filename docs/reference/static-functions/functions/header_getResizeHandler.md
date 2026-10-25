---
id: header_getResizeHandler
title: header_getResizeHandler
---

```ts
function header_getResizeHandler<TFeatures, TData, TValue>(header, _contextDocument?): (event) => void;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:91](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L91)

ヘッダーのリサイズのための、ポインターやタッチの開始時のハンドラーを作成します。

このハンドラーは、すべての末端のヘッダーの開始時の幅を記録し、ドラッグの移動量を追い、一時的なリサイズの情報を書き込みます。そして `columnResizeMode` に応じて、変更のたびか、ドラッグの終わりに列幅を確定します。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* `unknown` = `unknown`

## パラメーター {#parameters}

### header {#header}

[`Header`](../../index/type-aliases/Header.md)\<`TFeatures`, `TData`, `TValue`\>

### \_contextDocument? {#_contextdocument}

`Document`

## 戻り値 {#returns}

(`event`) => `void`

## 例 {#example}

```ts
const onMouseDown = header_getResizeHandler(header)
```
