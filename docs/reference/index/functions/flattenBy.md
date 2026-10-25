---
id: flattenBy
title: flattenBy
---

```ts
function flattenBy<TNode>(arr, getChildren): TNode[];
```

定義元: [utils.ts:264](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L264)

子ノードを再帰的に読み取り、ノードのツリーを平坦化します。

元のノードは深さ優先の順で保持されます。

## 型パラメーター {#type-parameters}

### TNode {#tnode}

`TNode`

## パラメーター {#parameters}

### arr {#arr}

`TNode`[]

### getChildren {#getchildren}

(`item`) => `TNode`[]

## 戻り値 {#returns}

`TNode`[]
