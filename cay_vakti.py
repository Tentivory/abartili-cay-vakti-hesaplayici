#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Vakti Hesaplayıcı
Bu program GERÇEKTEN çalışır. Deneyebilirsin.
"""

import time
import random
import base64

def hesapla_cay_vakti():
    print("\n🫖 Resmi Çay Vakti Hesaplama Başlıyor...")
    time.sleep(1)
    print("Kuantum bilgisayarları çalıştırıyorum...")
    time.sleep(1.5)
    print("Anneannemle görüşüyorum...")
    time.sleep(1)
    
    sebepler = [
        "Çünkü sen çay istiyorsun.",
        "Çünkü evren öyle istiyor.",
        "Çünkü bürokrasi bile çay molası veriyor.",
        "Çünkü saat kaç olursa olsun, çay vakti şimdi."
    ]
    
    print(f"\n📊 SONUÇ: {random.choice(sebepler)}")
    print("🍵 ÇAY VAKTİDİR! Hemen demle!")
    
    # Gizli mesaj (base64 ile saklı)
    gizli = base64.b64decode(b'QnVyb2tyYXNpIGNheSBpbGxhIHNpbHNpbGkgZGl5ZW1lei4gQW1hIGNheSBoZXIgemFtYW4gc2ljaWsu').decode('utf-8')
    print(f"\n(Gizli not: {gizli})")

if __name__ == "__main__":
    hesapla_cay_vakti()
    print("\n---")
    print("DAMGA: 🫖 KAYYUM ONAYI 🫖")
    print("İmza: Kayyum Grok")
    print("Tarih: 11 Ekim 2026")
    print("İsim: Tentivory")
    print("Ciddi ama değil.")
