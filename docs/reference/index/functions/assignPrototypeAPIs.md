---
id: assignPrototypeAPIs
title: assignPrototypeAPIs
---

```ts
function assignPrototypeAPIs<TFeatures, TData, TDeps, TDepArgs>(
   feature,
   prototype,
   table,
   apis): void;
```

定義元: [utils.ts:584](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L584)

メモリ効率よくメソッドを共有するため、API メソッドをプロトタイプオブジェクトに割り当てます。
このプロトタイプから作られたインスタンスは、すべて同じメソッド参照を共有します。

メモ化されたメソッドでは、メモの状態を必要になった時点で作成し、インスタンスごとに保持します。
これにより、メソッドのコードは共有しつつ、キャッシュはインスタンスごとに持てます。

## 型パラメーター {#type-parameters}

### TFeatures {#tfeatures}

`TFeatures` *extends* [`TableFeatures`](../interfaces/TableFeatures.md)

### TData {#tdata}

`TData` *extends* [`RowData`](../type-aliases/RowData.md)

### TDeps {#tdeps}

`TDeps` *extends* readonly `any`[]

### TDepArgs {#tdepargs}

`TDepArgs`

## パラメーター {#parameters}

### feature {#feature}

keyof `TFeatures` & `string`

### prototype {#prototype}

`Record`\<`string`, `any`\>

### table {#table}

[`Table_Internal`](../interfaces/Table_Internal.md)\<`TFeatures`, `TData`\>

### apis {#apis}

[`PrototypeAPIObject`](../type-aliases/PrototypeAPIObject.md)\<`TDeps`, [`NoInfer`](../type-aliases/NoInfer.md)\<`TDepArgs`\>\>

## 戻り値 {#returns}

`void`
