---
id: TableOptions
title: TableOptions
---

```ts
type TableOptions<TFeatures, TData> = TableOptions_Core<TFeatures, TData> & ExtractFeatureMapTypes<TFeatures, TableOptions_FeatureMap<TFeatures, TData>> & DebugOptions<TFeatures>;
```

定義元: [types/TableOptions.ts:131](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableOptions.ts#L131)

特定の機能の組み合わせについての、テーブルのオプション全体です。

機能のオプションは、その機能が `TFeatures` にある場合にだけ含まれます。そのうえで、カスタム機能やプラグインのオプションと、デバッグ用のオプションが加わります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](RowData.md)
