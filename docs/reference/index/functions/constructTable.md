---
id: constructTable
title: constructTable
---

```ts
function constructTable<TFeatures, TData>(tableOptions): Table<TFeatures, TData>;
```

定義元: [core/table/constructTable.ts:33](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/constructTable.ts#L33)

正規化されたテーブルの内部データからテーブルのインスタンスを作成します。

コアのプロパティ、機能のプロトタイプ API、インスタンスデータを結び付けます。これらはテーブルの描画と行モデルの処理で使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

## パラメーター {#parameters}

### tableOptions {#tableoptions}

[`TableOptions`](../type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`Table`](../type-aliases/Table.md)\<`TFeatures`, `TData`\>
