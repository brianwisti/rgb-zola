+++
title = "Stupid VS Code Vim Tricks"
date = "2023-03-20"
draft = false

[taxonomies]
category = ["note",]
tags = ["vs-code", "config",]
+++

Still trying my [experiment][pkm] with using [Dendron][dendron] in [Visual
Studio Code][vs-code] as part of some sort of public second brain. Honestly I
don't know how long that'll last, so I figure better share the fun stuff I
learn here too.

[pkm]: https://randomgeekery.online
[dendron]: https://dendron.so
[vs-code]: https://code.visualstudio.com

Anyways this afternoon I installed the [Vim][vscode-vim] extension and learned just enough about custom keybindings to add a few.

[vscode-vim]: https://marketplace.visualstudio.com/items?itemName=vscodevim.vim


```json{title="settings.json"}
{
  "vim.leader": "<space>",
  "vim.normalModeKeyBindings": [
    {
      "before": ["<leader>", "t", "l"],
      "commands": ["workbench.action.toggleSidebarVisibility"]
    },
    {
      "before": ["<leader>", "t", "r"],
      "commands": ["workbench.action.toggleAuxiliaryBar"]
    },
    {
      "before": ["<leader>", "t", "t"],
      "commands": ["workbench.action.toggleLightDarkThemes"]
    }
  ]
}
```

- `vim.leader` is handy as a prefix for extended custom bindings in Vim; I prefer the spacebar as my leader 
- `<leader> t l` toggles my left sidebar
- `<leader> t r` toggles my right sidebar
- `<leader> t t` toggles between light and dark theme

These bindings look and work very similar to some of [Logseq][logseq]'s default bindings.
That's no accident.
I like those bindings.

[logseq]: https://logseq.com
