---
id: table_setOptions
title: table_setOptions
---

```ts
function table_setOptions<TFeatures, TData>(
   table,
   updater,
   options?): void;
```

定義元: [core/table/coreTablesFeature.utils.ts:201](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.utils.ts#L201)

テーブルのオプションのオブジェクトを更新します。

アップデーターは現在の解決済みのオプションを受け取り、マージした結果はすぐにテーブルインスタンスに割り当てられます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### updater {#updater}

[`Updater`](../../index/type-aliases/Updater.md)\<[`TableOptions`](../../index/type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>\>

### options? {#options}

#### syncExternalState? {#syncexternalstate}

`boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_setOptions(table, (old) => old)
table_setOptions(table, (old) => old, { syncExternalState: false })
```
