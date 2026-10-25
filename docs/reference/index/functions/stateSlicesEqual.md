---
id: stateSlicesEqual
title: stateSlicesEqual
---

```ts
function stateSlicesEqual(a, b): boolean;
```

定義元: [utils.ts:155](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L155)

2つの状態スライスの値を構造的に比較します。比較する深さは、標準機能の状態が入れ子になりうる深さまでで、それより深くは比べません。

3段階のコンテナーまで比べれば、平坦なマップと配列、状態オブジェクトの配列、配列のフィルター値、`columnResizing.columnSizingStart` のタプルに対応できます。
それより深いコンテナーとプレーンでない値は参照で比較します。`false` を返しても常に安全で、その場合は状態の更新がそのまま進みます。

## パラメーター {#parameters}

### a {#a}

`unknown`

### b {#b}

`unknown`

## 戻り値 {#returns}

`boolean`
