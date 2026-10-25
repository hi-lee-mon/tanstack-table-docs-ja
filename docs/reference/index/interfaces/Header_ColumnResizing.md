---
id: Header_ColumnResizing
title: Header_ColumnResizing
---

定義元: [features/column-resizing/columnResizingFeature.types.ts:79](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L79)

## プロパティ {#properties}

### getResizeHandler {#getresizehandler}

```ts
getResizeHandler: (context?) => (event) => void;
```

定義元: [features/column-resizing/columnResizingFeature.types.ts:85](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.types.ts#L85)

リサイズ用のつまみに付ける `onMouseDown` / `onTouchStart` のハンドラーを作成します。

ドラッグ中と離したときのリスナーは、自動で登録・解除されます。

#### パラメーター {#parameters}

##### context? {#context}

`Document`

#### 戻り値 {#returns}

(`event`) => `void`
