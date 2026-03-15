## 🏗️ Architecture

```text
camouchat/ 
├── src/
│   ├── BrowserManager/     # Anti-detect Camoufox, ProfileManager, Sandboxing
│   ├── WhatsApp/           # Platform-specific implementation
│   │   ├── login.py                  # QR + Phone authentication
│   │   ├── chat_processor.py         # Handles chat fetching and navigation
│   │   ├── message_processor.py      # Extracts and processes messages
│   │   ├── humanized_operations.py   # Human-like typing and scrolling
│   │   ├── media_capable.py          # Media processing and downloading
│   │   ├── reply_capable.py          # Handling replies in chats
│   │   ├── web_ui_config.py          # Selector definitions
│   │   └── DerivedTypes/             # Chat, Message dataclasses
│   ├── Interfaces/         # Abstract contracts (for future platform extensions)
│   ├── StorageDB/          # Async SQLite/PostgreSQL, SQLAlchemy Integrations
│   ├── Encryption/         # Out-of-the-box AES-256 encrypted storage
│   ├── Filter/             # Message and chat filtering module
│   ├── Decorators/         # Common utility decorators
│   ├── Exceptions/         # Custom customized Error hierarchies 
│   └── directory.py        # Centralized OS-independent directory resolver
└── tests/                  # Playwright Async Tests, Security suites, CI pipelines.
```
---

### Key Design Decisions

- **Interface-Driven**: Every platform implements abstract contracts like `ChatProcessorInterface`, `MessageProcessorInterface`.
- **Dependency Injection**: Classes cleanly accept highly flexible parameters (e.g. `log`) for rigorous testability.
- **Sandboxed Profiles**: End-to-end multithreaded Profile & Session isolation to aggressively circumvent anti-bots.
- **Encrypted Storage**: Secure AES-256 automated pipeline connecting flawlessly to SQLAlchemy queues out-of-the box.
- **Async-First**: Completely asynchronous non-blocking DB writes, Background task flushing, and Playwright interactions.
- **Anti-Detection**: Built natively on Camoufox, dynamically spoofed rendering dimensions by BrowserForge, augmented by realistically human cursor trajectories and typing algorithms.
