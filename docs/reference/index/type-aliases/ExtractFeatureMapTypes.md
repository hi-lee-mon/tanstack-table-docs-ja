---
id: ExtractFeatureMapTypes
title: ExtractFeatureMapTypes
---

```ts
type ExtractFeatureMapTypes<TFeatures, TFeatureMap> = IsAny<TFeatures> extends true ? UnionToIntersection<TFeatureMap[keyof TFeatureMap]> : UnionToIntersectionOrEmpty<TFeatureMap[Extract<keyof TFeatures, keyof TFeatureMap>]>;
```

定義元: [types/TableFeatures.ts:43](https://github.com/TanStack/table/blob/main/packages/table-core/src/types/TableFeatures.ts#L43)

`TFeatures` に含まれる機能が提供する API や型を取り出します。

`TFeatureMap` は、機能のキーを、その機能が提供する型に対応付けます。
`TFeatures` が `any` の場合は、広いテーブルの型で期待される制限の緩い動作を保つため、機能マップのエントリーをすべて含めます。そうでなければ、`TFeatures` にキーがあるエントリーだけを交差型で組み合わせます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TFeatureMap {#tfeaturemap}

`TFeatureMap` *extends* `object`
