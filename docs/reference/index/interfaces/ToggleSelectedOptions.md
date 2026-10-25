---
id: ToggleSelectedOptions
title: ToggleSelectedOptions
---

定義元: [features/row-selection/rowSelectionFeature.types.ts:11](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L11)

行を切り替えたときに、その子孫と祖先にどう影響させるかを制御します。

## プロパティ {#properties}

### deselectParents? {#deselectparents}

```ts
optional deselectParents?: boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:27](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L27)

この行を選択解除したときに、祖先の行 ID を選択から取り除くかどうかです。親からの連鎖で親の ID が状態に書き込まれたあと、子を選択解除する場合に便利です。既定値は `false` です。

祖先自身が選択できない行でも、祖先の ID は取り除かれます。
他の対象を絞った選択解除と同じく、この取り除きは `enableRowSelection` に左右されません。選択できない行を残すのは、一括の全選択の処理だけです。

***

### selectChildren? {#selectchildren}

```ts
optional selectChildren?: boolean;
```

定義元: [features/row-selection/rowSelectionFeature.types.ts:16](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/row-selection/rowSelectionFeature.types.ts#L16)

選択可能な子の行を再帰的に切り替えるかどうかです。既定値は `true` です。
