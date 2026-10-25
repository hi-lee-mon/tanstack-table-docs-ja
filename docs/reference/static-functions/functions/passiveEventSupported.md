---
id: passiveEventSupported
title: passiveEventSupported
---

```ts
function passiveEventSupported(): boolean;
```

定義元: [features/column-resizing/columnResizingFeature.utils.ts:397](https://github.com/TanStack/table/blob/main/packages/table-core/src/features/column-resizing/columnResizingFeature.utils.ts#L397)

現在の環境がパッシブなイベントリスナーに対応しているかどうかを判定します。

列幅の変更ではこれを使い、環境がパッシブのオプションを理解する場合にだけ、`passive: false` を付けてポインターやタッチのリスナーを登録します。

## 戻り値 {#returns}

`boolean`

## 例 {#example}

```ts
const canUsePassiveListeners = passiveEventSupported()
```
