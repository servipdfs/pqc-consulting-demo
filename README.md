[README.md](https://github.com/user-attachments/files/28610892/README.md)
# 🔐 Post-Quantum Cryptography Consulting Demo

**Autor:** Ramón Rodríguez Monje  
**Objetivo:** Demostrar capacidades prácticas y estratégicas en Criptografía Post-Cuántica (PQC), alineado con la oferta de SEREM.

## 📌 Contenido
- PoC: ML-KEM (Kyber-768) + AES-256-GCM y ML-DSA (Dilithium-3)
- Simulación de handshake TLS híbrido (X25519 + Kyber)
- Análisis de riesgos SNDL y hoja de ruta de migración (QSFF/FS-ISAC)
- Tests unitarios, CI/CD y Docker

## 🧪 Ejecutar PoC
```bash
python src/kem_hybrid_demo.py
python src/signature_demo.py
python src/hybrid_tls_sim.py
