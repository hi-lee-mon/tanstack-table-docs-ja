---
id: ExtractTableMeta
title: ExtractTableMeta
---

```ts
type ExtractTableMeta<TFeatures, TData> = IsAny<TFeatures> extends true ? TableMeta<TFeatures, TData> : TFeatures extends object ? TMeta : TableMeta<TFeatures, TData>;
```

定義元: [core/table/coreTablesFeature.types.ts:30](https://github.com/TanStack/table/blob/main/packages/table-core/src/core/table/coreTablesFeature.types.ts#L30)

機能の組み合わせについて、`options.meta` の型を求めます。

features オブジェクトが型専用スロット `tableMeta` を宣言している場合（`tableFeatures({ ..., tableMeta: {} as MyTableMeta })`）は、その型が使われます。
そうでなければ、グローバルに宣言のマージをした `TableMeta` インターフェースが使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
