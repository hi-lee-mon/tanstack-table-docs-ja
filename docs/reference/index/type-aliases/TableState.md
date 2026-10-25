---
id: TableState
title: TableState
---

```ts
type TableState<TFeatures> = ExtractFeatureMapTypes<TFeatures, TableState_FeatureMap>;
```

定義元: [types/TableState.ts:40](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableState.ts#L40)

特定の機能の組み合わせについての、テーブルの状態全体です。

状態スライスは、その機能が `TFeatures` にある場合にだけ含まれます。そのうえで、カスタム機能やプラグインの状態が加わります。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
