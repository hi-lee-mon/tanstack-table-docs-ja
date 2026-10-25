---
id: ExtractFilterMeta
title: ExtractFilterMeta
---

```ts
type ExtractFilterMeta<TFeatures> = IsAny<TFeatures> extends true ? FilterMeta : TFeatures extends object ? TFilterMeta : FilterMeta;
```

定義元: [features/column-filtering/columnFilteringFeature.types.ts:24](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-filtering/columnFilteringFeature.types.ts#L24)

機能の組み合わせについて、行に付けるフィルターのメタデータの型を求めます。

features オブジェクトが型専用スロット `filterMeta` を宣言している場合（`tableFeatures({ ..., filterMeta: {} as MyFilterMeta })`）は、その型が使われます。
そうでなければ、グローバルに宣言のマージをした `FilterMeta` インターフェースが使われます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)
