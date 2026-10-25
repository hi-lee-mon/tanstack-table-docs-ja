---
id: columnFacetingFeature
title: columnFacetingFeature
---

```ts
const columnFacetingFeature: TableFeature;
```

定義元: [features/column-faceting/columnFacetingFeature.ts:21](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-faceting/columnFacetingFeature.ts#L21)

フィルター向けに、ファセット行モデル、一意な値、最小値・最大値を導き出す機能です。

これらの API は、この層ではあえてメモ化していません。標準の `createFaceted*` ファクトリーは（他の標準の行モデルと同じく）内部でメモ化しています。ここでさらにメモ化すると、ファセット行モデルとは別にデータが変わるカスタムのファクトリーの結果が固まってしまいます。
カスタムのファクトリーは、メモ化を自分で行います。
