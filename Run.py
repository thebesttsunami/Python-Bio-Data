#!/usr/bin/python

print(Fore.CYAN + Style.BRIGHT + "Biodata Pribadi" + Style.RESET_ALL)
    print("-" * 50)
    
    # Data biodata
    biodata = [
        ["Nama", "Aldy Yoay"],
        ["Usia", "14 Tahun"],
        ["Alamat", "Mekar Asri No. 25, Bogor, Indonesia"],
        ["Nomor HP", "+62 851 9499 6351"],
        ["Email", "aldyyoaysite@gmail.com"],
        ["GitHub", "https://github.com/thebesttsunami"],
        ["Facebook", "https://facebook.com/lubangeek"],
        ["Twitter", "https://twitter.com/lubangeek"]
    ]
    
    # Mencetak biodata dalam format tabel dengan warna
    print(Fore.GREEN + tabulate(biodata, headers=["Informasi", "Detail"], tablefmt="fancy_grid") + Style.RESET_ALL)

    print("-" * 50)

Menjalankan fungsi untuk menampilkan biodata
if _name_ == "_main_":
    display_biodata()
