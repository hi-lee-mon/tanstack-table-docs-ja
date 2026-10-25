---
id: IdIdentifier
title: IdIdentifier
---

定義元: [types/ColumnDef.ts:84](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L84)

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TValue {#tvalue}

`TValue` *extends* [`CellData`](../type-aliases/CellData.md) = [`CellData`](../type-aliases/CellData.md)

## プロパティ {#properties}

### header? {#header}

```ts
optional header?: ColumnDefTemplate<HeaderContext<TFeatures, TData, TValue>>;
```

定義元: [types/ColumnDef.ts:96](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L96)

この列のヘッダーを描画するためのヘッダーのテキストまたはテンプレートです。

***

### id {#id}

```ts
id: string;
```

定義元: [types/ColumnDef.ts:92](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/ColumnDef.ts#L92)

明示的に指定する、変わらない列 ID です。
