---
category: note
date: 2022-04-24 15:00:33-07:00
draft: false
tags:
- config
- nushell
title: Config Tweaks for Nushell
updated_at: 1650838225
---

[nushell-config]: {{< ref "/config/shell/nushell/_index.md" >}}

Added my [Nushell config][nushell-config] stuff to the site. It's not that
interesting yet.

What is?

Here's a tmux binding to readily launch a `nu` session, while leaving `$SHELL` alone.

```
bind C new-window -- nu
```

And [`nvim-nu.nvim`][nvim-nu] for Nushell support in Neovim through Treesitter.

```lua
use {
  "LhKipp/nvim-nu",
  run = ":TSInstall nu",
  config = function()
    require("nu").setup{}
  end
}
```

[nvim-nu]: https://github.com/LhKipp/nvim-nu
