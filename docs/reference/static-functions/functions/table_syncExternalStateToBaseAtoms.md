---
id: table_syncExternalStateToBaseAtoms
title: table_syncExternalStateToBaseAtoms
---

```ts
function table_syncExternalStateToBaseAtoms<TFeatures, TData>(
   table,
   capturedState?,
   compare?): void;
```

定義元: [core/table/coreTablesFeature.utils.ts:28](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.utils.ts#L28)

外部で制御された状態スライスを、テーブルの基底アトムに同期します。

`options.state` の値をアトムのグラフに写しておくことで、派生アトム、ストア、テーブルの API が一貫したスナップショットを読めるようにします。

ホストの描画フェーズでオプションを更新するアダプターは、コミットされた描画で記録した状態のスナップショットを `capturedState` として渡します。共有のオプションのオブジェクトには、コミットされずに終わる新しい描画の値がすでに入っている可能性があるためです。
`null` を渡すと何も公開しません（「制御された状態がない」ことを記録したものとして扱います）。引数を省略すると、代わりに現在の `table.options.state` を読みます。
省略可能な `compare` を渡すと、意味の上で変わっていないスライスの書き込みを抑えられます。既定は参照の等価性のままです。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../../index/interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../../index/type-aliases/RowData.md)

## パラメーター {#parameters}

### table {#table}

[`Table_Internal`](../../index/interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### capturedState? {#capturedstate}

  \| `Partial`\<[`TableState`](../../index/type-aliases/TableState.md)\<`TFeatures`\>\>
  \| `null`

### compare? {#compare}

(`currentState`, `externalState`) => `boolean`

## 戻り値 {#returns}

`void`

## 例 {#example}

```ts
table_syncExternalStateToBaseAtoms(table)
table_syncExternalStateToBaseAtoms(table, capturedState ?? null, shallow)
```
