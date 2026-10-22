---
id: getCoreRowModel
title: getCoreRowModel
---

```ts
function getCoreRowModel<TData>(): RowModelFactory<TData>;
```

定義元: [src/useLegacyTable.ts:151](https://github.com/TanStack/table/blob/main/packages/react-table/src/useLegacyTable.ts#L151)

## 型パラメーター {#type-parameters}

### TData {#tdata}

`TData` *extends* `RowData`

## 戻り値 {#returns}

[`RowModelFactory`](../type-aliases/RowModelFactory.md)\<`TData`\>

## 非推奨 {#deprecated}

v9 では、コア行モデルは常に自動で作成されます。

これは `useLegacyTable` で v8 の API との互換性を保つためのスタブ関数です。
何も行いません。コア行モデルは常に利用できます。
