---
id: table_mergeOptions
title: table_mergeOptions
---

```ts
function table_mergeOptions<TFeatures, TData>(table, newOptions): TableOptions<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.utils.ts:134](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.utils.ts#L134)

新しいテーブルのオプションを、現在の解決済みのオプションとマージします。

`options.mergeOptions` を渡した場合は、マージの動作をそれに任せます。そうでなければ、オプションは浅くマージされます。
初期化後に変わってはいけない静的なオプションは、新しいオブジェクトに戻されます。そのため、フレームワークのマージ用ヘルパーが読み取り専用の getter やプロキシのオブジェクトを返しても問題ありません。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### newOptions {#newoptions}

[`TableOptions`](../../index/type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

## 戻り値 {#returns}

[`TableOptions`](../../index/type-aliases/TableOptions.md)\<`TFeatures`, `TData`\>

## 例 {#example}

```ts
const options = table_mergeOptions(table, nextOptions)
```
