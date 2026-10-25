---
id: Cell_CellSelection
title: Cell_CellSelection
---

定義元: [features/cell-selection/cellSelectionFeature.types.ts:158](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L158)

## プロパティ {#properties}

### getCanSelect {#getcanselect}

```ts
getCanSelect: () => boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:162](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L162)

このセルが現在選択できるかどうかを判定します。

#### 戻り値 {#returns}

`boolean`

***

### getIsFocused {#getisfocused}

```ts
getIsFocused: () => boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:167](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L167)

このセルがアクティブなセル、つまり直近の範囲のアンカーかどうかを判定します。

#### 戻り値 {#returns-1}

`boolean`

***

### getIsSelected {#getisselected}

```ts
getIsSelected: () => boolean;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:171](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L171)

このセルが最終的な選択（除外を差し引いた結果）の中にあるかどうかを判定します。

#### 戻り値 {#returns-2}

`boolean`

***

### getSelectionEdges {#getselectionedges}

```ts
getSelectionEdges: () => CellSelectionEdges;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:179](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L179)

このセルのどの辺が選択範囲の外周に接しているかを返します。各セルが隣のセルを調べなくても、スプレッドシートのような枠線を描画できます。

セルが選択されていない場合は、どの辺も `false` です。

#### 戻り値 {#returns-3}

[`CellSelectionEdges`](CellSelectionEdges.md)

***

### getSelectionExtendHandler {#getselectionextendhandler}

```ts
getSelectionExtendHandler: () => (event) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:187](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L187)

ドラッグ中に、アクティブな範囲をこのセルまで広げるハンドラーを作成します。`mouseenter` に結び付けてください。

このハンドラーは、ドラッグ中でなければ何もしません。また、アクティブな範囲がすでにこのセルにフォーカスしている場合は、余計な書き込みを省きます。

#### 戻り値 {#returns-4}

(`event`) => `void`

***

### getSelectionStartHandler {#getselectionstarthandler}

```ts
getSelectionStartHandler: (contextDocument?) => (event) => void;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:198](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L198)

このセルから選択を始めるハンドラーを作成します。`mousedown` に結び付けてください。

修飾キーを検出できるよう、元のマウスイベントか、`nativeEvent` にそのイベントを持つフレームワークのイベントを渡してください。
ハンドラーは document レベルの `mouseup` リスナーを自分で登録するので、テーブルの外でドラッグを離しても正しく終わります。iframe やポップアウトウィンドウのように別の document にテーブルを描画する場合は、`contextDocument` を渡してください。

#### パラメーター {#parameters}

##### contextDocument? {#contextdocument}

`Document`

#### 戻り値 {#returns-5}

(`event`) => `void`

***

### getTabIndex {#gettabindex}

```ts
getTabIndex: () => number;
```

定義元: [features/cell-selection/cellSelectionFeature.types.ts:204](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/cell-selection/cellSelectionFeature.types.ts#L204)

ローヴィング tabindex のために、フォーカスされたセルでは `0`、それ以外では `-1` を返します。

#### 戻り値 {#returns-6}

`number`
