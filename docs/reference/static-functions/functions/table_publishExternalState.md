---
id: table_publishExternalState
title: table_publishExternalState
---

```ts
function table_publishExternalState<TFeatures, TData>(
   table,
   state,
   compare?): void;
```

定義元: [core/table/coreTablesFeature.utils.ts:73](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.utils.ts#L73)

ホストのフレームワークがコミットしたあとに、記録しておいた制御された状態を公開します。

描画フェーズのアダプターは、基底アトムを同期せずにオプションを準備し、コミットされた描画で記録した状態をここに渡します。基底アトムに何も書き込まれなかった場合も、コミットの合図によって持ち主の変更が無効になります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### state {#state}

  \| `Partial`\<[`TableState`](../../index/type-aliases/TableState.md)\<`TFeatures`\>\>
  \| `null`

### compare? {#compare}

(`currentState`, `externalState`) => `boolean`

## 戻り値 {#returns}

`void`
