---
id: cellSpanningFeature
title: cellSpanningFeature
---

```ts
const cellSpanningFeature: TableFeature;
```

定義元: [features/cell-spanning/cellSpanningFeature.ts:18](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-spanning/cellSpanningFeature.ts#L18)

同じ値を持つ隣り合うセルを、行をまたいで結合したセルにまとめる機能です。列定義で、行ごとに列をまたいで結合するセルを宣言することもできます。

状態を持ちません。結合は常に現在描画されている行から導き出されるので、保存するものはなく、列定義以外に設定するものもありません。
