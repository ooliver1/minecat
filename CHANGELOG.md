# Changelog

## [0.4.0](https://github.com/ooliver1/minecat/compare/v0.3.0...v0.4.0) (2022-08-15)


### Features

* add link server cog ([f8743c1](https://github.com/ooliver1/minecat/commit/f8743c1564db9863bcc3f273c63242a729047924))
* **mineager:** add custom server protocol ([c6fa507](https://github.com/ooliver1/minecat/commit/c6fa50796024726dd12d00bd62c017f6a459d119))
* **ws:** add controller and storage to manage clients ([ce107bb](https://github.com/ooliver1/minecat/commit/ce107bb9b5b62caa9abc96ded0e44ca4010cbde6))


### Bug Fixes

* add -py.typed files ([61ab7b8](https://github.com/ooliver1/minecat/commit/61ab7b8b5a4e95fc510410e0ac9f1629bd79c1ee))
* eliminate pyright errors ([aa9e635](https://github.com/ooliver1/minecat/commit/aa9e635232509e619a8f7f7ed8800b2a576cbee8))
* import from correct module ([d20e7b8](https://github.com/ooliver1/minecat/commit/d20e7b808cf7c8fe559cc14c29a67cc8bb25681e))
* **main:** remove more pyright issues ([e30acdf](https://github.com/ooliver1/minecat/commit/e30acdf2c3baa85b5de20799df072c728b28a543))
* pyright thinks we are in 3.11 ([5bba00e](https://github.com/ooliver1/minecat/commit/5bba00e545bdc0dfed36360c2b74fa1c0ffe1b4b))
* **ws:** import logger properly ([23fdb40](https://github.com/ooliver1/minecat/commit/23fdb40bfe118e60273e7189315595c3a9d2d9d0))

## [0.3.0](https://github.com/ooliver1/minecat/compare/v0.2.0...v0.3.0) (2022-07-21)


### Features

* add a served websocket server ([4b71d6d](https://github.com/ooliver1/minecat/commit/4b71d6d78d05366ed2bc10b0818c2ca4cf5c1c09))
* add bot process manager ([828a955](https://github.com/ooliver1/minecat/commit/828a95531a46553095503278ff67d23f0faf3ec4))
* **manager:** add opcode for process management ([8829eb0](https://github.com/ooliver1/minecat/commit/8829eb0440954a217a93b9635cc5bc16caf6afc0))
* **manager:** restart other processes+always use json ([b66dbff](https://github.com/ooliver1/minecat/commit/b66dbff50100c722db40bd024be831f42f75adc7))
* **server:** annotate uuid attribute ([07c2f6e](https://github.com/ooliver1/minecat/commit/07c2f6eb484b9d709cce9506f3352b2dafa97b0e))


### Bug Fixes

* add manager dockerfile ([6d4c1a3](https://github.com/ooliver1/minecat/commit/6d4c1a3b84c1dedfe90080ff5c08f348a023456e))
* include gcc in manager as im lazy, cchardet 3.10 moment ([725d923](https://github.com/ooliver1/minecat/commit/725d923d3129ae36a7c1220ee1769e9c94d06e30))
* **manager:** reload properly ([b6455dd](https://github.com/ooliver1/minecat/commit/b6455dd2560e3fab0e486e16728567f8a393ef4e))
* **manager:** return on error and define callbacks ([fe8c17b](https://github.com/ooliver1/minecat/commit/fe8c17b12f52e03c2fe62802596c84a95b3c972c))
* **server:** add a setup function ([b09ae4e](https://github.com/ooliver1/minecat/commit/b09ae4ed160a83ca955cae82f5269a026454769c))
* **server:** use the proper logger name ([1c08316](https://github.com/ooliver1/minecat/commit/1c08316f6a3f54afd3da4c5e89dcb509d2f29528))
* **server:** use the websocket logger ([d0c071f](https://github.com/ooliver1/minecat/commit/d0c071fd40f1ece458a04f01be9dd3ac2feef359))

## [0.2.0](https://github.com/ooliver1/minecat/compare/v0.1.0...v0.2.0) (2022-07-17)


### Features

* actually add the ability to add callbacks ([731c1f4](https://github.com/ooliver1/minecat/commit/731c1f452c450108990ae1a1b51c5b6a28b9e6b2))
* add a manager class for callback sorting ([7d4986d](https://github.com/ooliver1/minecat/commit/7d4986d29fb83b8b047e4ef382af92b17ad2c94e))
* use a graceful shutdown on the manager ([99f4426](https://github.com/ooliver1/minecat/commit/99f44260a3ad32d5927bac788e5472e416e672ed))


### Bug Fixes

* actually rename bot ([c7575df](https://github.com/ooliver1/minecat/commit/c7575df06da18fd7e0dc253478c82a68664484e1))
* use an __init__ file for version to update ([7a4753a](https://github.com/ooliver1/minecat/commit/7a4753ad5e320679802b9546b8128be508739c58))

## 0.1.0 (2022-07-09)


### Features

* add basic starting manager ([d09386e](https://github.com/ooliver1/minecat/commit/d09386e80b11fe8bc7f182215650eea888f590a7))
* add postgres to docker ([e88c90f](https://github.com/ooliver1/minecat/commit/e88c90f6876f6eb5e827e5c94793a9a5d246261d))
* add relevant intents ([5288508](https://github.com/ooliver1/minecat/commit/5288508da8a994c4b3019f0dd6b7e8fda9a7b9f9))
* add template ([c11a666](https://github.com/ooliver1/minecat/commit/c11a6661ff7a8c803be74063bc17ed555271e1c6))
* move manager separate for multi process lol ([a95ffff](https://github.com/ooliver1/minecat/commit/a95ffff0832fd1c262ce12958012db855f551aad))
* setup config ([7ca8356](https://github.com/ooliver1/minecat/commit/7ca8356ce551014873518fa5e55d84001e4d7810))


### Bug Fixes

* use member cache flags ([4035ac3](https://github.com/ooliver1/minecat/commit/4035ac391205dbf9c37e40a00a52c81b8539fa5c))
* use multiple compose entries again ([3efcead](https://github.com/ooliver1/minecat/commit/3efcead1fa8b202449a06a17450cafc8a408fce0))
