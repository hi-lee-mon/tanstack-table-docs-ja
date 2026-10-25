---
id: CellSelectionState
title: CellSelectionState
---

```ts
type CellSelectionState = CellSelectionRange[];
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:41](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L41)

最終的な選択を作る、順序付きの範囲の操作です。最後のエントリーがアクティブな操作で、Shift キーでの拡張とドラッグはこれに対して働きます。

`SortingState` や `ColumnFiltersState` と同じく、ただの配列です。ドラッグ中の状態は、あえてこのスライスの外に、リアクティブでないインスタンスのデータとして置いています。そのため、ここには一時的なものがなく、スライス全体を安全に保存できます。
