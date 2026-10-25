---
id: setStateSlice
title: setStateSlice
---

```ts
function setStateSlice<K>(
   instance,
   key,
   updater,
   isEqual?): void;
```

定義元: [utils.ts:223](https://github.com/TanStack/table/blob/main/packages/table-core/src/utils.ts#L223)

状態スライスの更新を、そのスライスの `on<State>Change` ハンドラーに通します。構造上は何も変わらない更新では、状態の持ち主が持つ現在の参照をそのまま保ちます。

等価判定は、状態の持ち主が受け取るアップデーターの中で行います。テーブルが持つ、古くなっているかもしれない制御された状態のスナップショットとは比べません。
これにより、React の state のような更新をキューに積むコンテナーでも同じティック内の更新を組み合わせられます。また、元のアップデーターは持ち主が適用したときにだけ評価され、アトムの持ち主は既存の参照を返すことで通知を抑えられます。

何も変わらない更新でも、利用者が渡した変更ハンドラーは呼び出されます。キューに積まれた最新の値を知っているのは、そのハンドラーの状態コンテナーだけだからです。
保護されたアップデーターはそのコンテナーの前の参照を返すので、同一性で処理を打ち切る状態コンテナーでは、状態の書き込みや描画が起きません。

保護を完全に省くホットパスのスライス（行数に比例して大きくなる選択のマップや、ポインター操作のたびに更新されるリサイズの状態）は、このユーティリティを通さず変更ハンドラーを直接呼び出します。
より軽い比較や意味を考慮した比較を持つカスタム機能のスライスは、`isEqual` を渡して構造比較の既定を上書きできます。

## 型パラメーター {#type-parameters}

### K {#k}

`K` *extends* keyof TableState\_All \| `string` & `object`

## パラメーター {#parameters}

### instance {#instance}

#### options {#options}

`object`

### key {#key}

`K`

### updater {#updater}

[`Updater`](../type-aliases/Updater.md)\<`StateSliceForKey`\<`K`\>\>

### isEqual? {#isequal}

[`StateSliceEqualityFn`](../type-aliases/StateSliceEqualityFn.md)\<`StateSliceForKey`\<`K`\>\> = `stateSlicesEqual`

## 戻り値 {#returns}

`void`
