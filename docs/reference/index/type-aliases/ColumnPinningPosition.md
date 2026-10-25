---
id: ColumnPinningPosition
title: ColumnPinningPosition
---

```ts
type ColumnPinningPosition = false | "start" | "end";
```

定義元: [features/column-pinning/columnPinningFeature.types.ts:15](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-pinning/columnPinningFeature.types.ts#L15)

論理的な列の固定領域です。

LTR の言語やレイアウトでは、ふつう `start` は左、`end` は右にあたります。RTL の言語やレイアウトでは、ふつう `start` は右、`end` は左にあたります。
