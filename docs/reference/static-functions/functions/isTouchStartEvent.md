---
id: isTouchStartEvent
title: isTouchStartEvent
---

```ts
function isTouchStartEvent(e): e is TouchEvent;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:431](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L431)

型のわからないイベントを、`touchstart` イベントに絞り込みます。

列幅の変更では、タッチの座標を読み、タッチ用のリスナーを登録する前にこれを使います。

## パラメーター {#parameters}

### e {#e}

`unknown`

## 戻り値 {#returns}

`e is TouchEvent`

## 例 {#example}

```ts
const isTouch = isTouchStartEvent(event)
```
