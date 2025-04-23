# TLS 1.3 toy implementation
## 1. 🔍 Overview

A minimal, working client-side MVP of the TLS 1.3 protocol. The implementation aims to highlight the core components of a complete handshake for easy understanding and potential replication. This can serve as the skeleton on which custom TLS protocols can be built.

## 2. 🏗️ Features

- ✅ TLS 1.3 Handshake (ClientHello → Finished)

- ✅ HKDF-based Key Schedule

- ✅ AEAD encryption using AES-GCM

- ✅ Record Layer Framing

- ✅ Basic test client/server interaction  

Currently, the skeleton retrieves an HTML representing the frontpage of a website, as proof of successful handshake. This can be extended based on project needs.

## 3. 🛠️ How to Build / Run
- Using console command:  
```bash
git clone https://github.com/VuLemon/tinyTLS-implementations
/path/to/your/jupyter nbconvert --to notebook --execute tinyTLS.ipynb --inplace
```  
- Alternatively, run the .ipynb in your preferred editor

![Demo GIF](asset/demo1.gif)

## 4. 🚧 Future plans
- Develop custom test server to accompany client  
- Develop testing suite + custom error messages for easy debug
