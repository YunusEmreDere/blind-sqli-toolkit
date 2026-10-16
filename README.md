# blind-sqli-toolkit
Blind SQL injection zafiyetlerini, karakter karakter veri çıkararak (brute-force) exploit eden script koleksiyonu.<br>

## exploit.py
PortSwigger Web Security Academy'deki `Blind SQL injection with conditional errors` labının çözüm scripti.<br>
**Veritabanı:** Oracle <br>
**Teknik:** Error-based blind SQL injection — `TrackingId` cookie'sine enjekte edilen bir `CASE WHEN` ifadesi, koşul doğru olduğunda `TO_CHAR(1/0)` ile sıfıra bölme hatası tetikliyor (HTTP 500), yanlışsa normal cevap (200) dönüyor. Script, `administrator` kullanıcısının şifresini bu davranış farkına bakarak pozisyon pozisyon, a-z ve 0-9 karakterlerini deneyerek buluyor.
## Çalıştırma
```bash
pip install requests
python3 exploit.py
```

## Değişkenler

`url` kısmına PortSwigger lab'ının adresi girilmelidir.

**Opsiyonel:** `proxies` kısmındaki boş `""` ifadelerine Burp Suite proxy adresi (örn. `http://127.0.0.1:8080`) yazılabilir, böylece trafiği Burp üzerinden gözlemleyebilirsiniz. İstenmezse `response` satırındaki `proxies` ve `verify` parametreleri silinebilir.

## Örnek çıktı
Pozisyon: 1 : g , Şu ana kadarki şifre: g <br>
Pozisyon: 2 : 7 , Şu ana kadarki şifre: g7 <br>
Pozisyon: 3 : 3 , Şu ana kadarki şifre: g73 <br>
... <br>
Test tamamlandı!!! Şifre: g73chyfwwjcc4xnnu8y8 <br>



## Planlanan geliştirmeler

- [ ] Binary search ile istek sayısını azaltma
- [ ] Time-based blind SQLi desteği
- [ ] PostgreSQL / MySQL desteği
