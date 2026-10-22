---
id: AppColumnDefTemplate
title: AppColumnDefTemplate
---

```ts
type AppColumnDefTemplate<TProps> = string | ((props) => any);
```

定義元: [src/createTableHook.tsx:86](https://github.com/TanStack/table/blob/main/packages/react-table/src/createTableHook.tsx#L86)

列定義で使うテンプレートの型です。文字列か関数を指定できます。

## 型パラメーター {#type-parameters}

### TProps {#tprops}

`TProps` *extends* `object`
