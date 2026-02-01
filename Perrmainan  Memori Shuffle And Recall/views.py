import os
import time

class GameView:
                                       
    COLORS = {                       # Warna untuk terminal
        'HEADER': '\033[95m',
        'BLUE': '\033[94m',
        'GREEN': '\033[92m',
        'YELLOW': '\033[93m',
        'RED': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }
    
    @staticmethod
    def clear():                                            # Clear screen terminal
        os.system('cls' if os.name == 'nt' else 'clear')    
        
    def print_color(self, text, color):                     # Print dengan warna
        color_code = self.COLORS.get(color.upper(), '')
        print(f"{color_code}{text}{self.COLORS['ENDC']}")
        
    def show_title(self, title):                            # Tampilkan judul
        print("=" * 60)
        print(f"{' ' * 20}{self.COLORS['BOLD']}{title}{self.COLORS['ENDC']}")
        print("=" * 60)
        
    def welcome_screen(self):                               # Layar selamat datang
        self.clear()
        self.show_title("PERMAINAN MEMORI ANGKA")
        
        self.print_color("\n🎮 GAME MENGINGAT URUTAN ANGKA", 'yellow')
        print("\nCARA BERMAIN:")
        print("1. Anda akan melihat urutan angka")
        print("2. Ingat urutan tersebut")
        print("3. Masukkan kembali urutan yang sama")
        print("4. Dapatkan skor berdasarkan ketepatan")
        
        input("\nTekan ENTER untuk melanjutkan...")
        
    def get_player_settings(self):                          # Pengaturan pemain
        self.clear()
        self.show_title("PENGATURAN PEMAIN")
        
        print("\nMasukkan nama pemain:")                    # Nama pemain
        name = input("> ").strip() or "Player"
        
        print("\nPilih tingkat kesulitan:")                 # Tingkat kesulitan
        print("1. Mudah (3-4 angka)")
        print("2. Sedang (4-6 angka)")
        print("3. Sulit (6-8 angka)")
        
        while True:
            choice = input("\nPilihan (1-3): ").strip()
            if choice == '1':
                difficulty = 'easy'
                break
            elif choice == '2':
                difficulty = 'medium'
                break
            elif choice == '3':
                difficulty = 'hard'
                break
            else:
                self.print_color("Pilihan tidak valid!", 'red')
                
        return name, difficulty
        
    def show_sequence(self, sequence, seconds=5):               # urutan angka
        self.clear()
        self.show_title("HAFAL URUTAN INI")
        
        print("\n" + "-" * 40)
        print("URUTAN ANGKA:")
        print("-" * 40)
        
        for i, num in enumerate(sequence):                      # Warna bergantian
            if i % 2 == 0:
                self.print_color(f"  [{num}]", 'blue')
            else:
                self.print_color(f"  [{num}]", 'green')
        print("-" * 40)
        
        print(f"\nWaktu: {seconds} detik")                      # countdown
        for i in range(seconds, 0, -1):
            print(f"\r{i}... ", end="", flush=True)
            time.sleep(1)
        print("\rWAKTU HABIS! " + " " * 10)
        time.sleep(1)
        
    def get_answers(self, length):                               # input jawaban
        self.clear()
        self.show_title("MASUKKAN JAWABAN")
        
        print(f"\nMasukkan {length} angka (pisahkan dengan spasi):")
        print("Contoh: 1 2 3 4")
        print("-" * 40)
        
        while True:
            try:
                answer_str = input("\nJawaban Anda: ").strip()
                
                if not answer_str:
                    self.print_color("Masukkan jawaban!", 'red')
                    continue
                    
                answers = [int(x) for x in answer_str.split()]                      # Konversi ke int
                
                if len(answers) != length:
                    self.print_color(f"Masukkan tepat {length} angka!", 'red')
                    continue
                    
                if any(x < 0 or x > 9 for x in answers):                            # Validasi angka 0-9
                    self.print_color("Angka harus antara 0-9!", 'red')
                    continue
                    
                return answers
                
            except ValueError:
                self.print_color("Masukkan angka yang valid!", 'red')
            except KeyboardInterrupt:
                raise
                
    def show_results(self, game_data, results):                                     # Tampilkan hasil
        self.clear()
        self.show_title("HASIL PERMAINAN")
        
        print(f"\nPemain: {game_data.player_name}")                                  # Info pemain
        print(f"Tingkat: {game_data.difficulty}")
        print("-" * 40)
        
        print("\nPERBANDINGAN JAWABAN:")                                             # Perbandingan jawaban
        print("No. | Anda | Benar | Status")
        print("-" * 30)
        
        for result in results:
            idx = result['index'] + 1
            user = result['user_answer']
            correct = result['correct_answer']
            status = "✓" if result['is_correct'] else "✗"
            color = 'green' if result['is_correct'] else 'red'
            
            self.print_color(f"{idx:2d}. |  {user}  |  {correct}  | {status}", color)
            
        print("\n" + "-" * 40)                                                            # Statistik
        print("STATISTIK:")
        summary = game_data.get_summary()
        
        print(f"Jumlah Soal   : {summary['total']}")
        print(f"Jawaban Benar : {summary['correct']}")
        print(f"Jawaban Salah : {summary['total'] - summary['correct']}")
        print(f"Akurasi       : {summary['accuracy']:.1f}%")
        print(f"Skor          : {summary['score']}")
        
        print("\n" + "-" * 40)                                                          # Feedback                              
        print("FEEDBACK:")
        
        accuracy = summary['accuracy']
        if accuracy == 100:
            self.print_color("🎉 LUAR BIASA! Ingatan sempurna!", 'green')
        elif accuracy >= 80:
            self.print_color("👍 Sangat baik! Hampir sempurna.", 'green')
        elif accuracy >= 60:
            self.print_color("👌 Cukup baik. Terus berlatih!", 'yellow')
        else:
            self.print_color("💪 Jangan menyerah! Ayo coba lagi!", 'red')
            
    def ask_replay(self):                                                            # Tanyakan main lagi
        print("\n" + "=" * 40)
        
        while True:
            choice = input("\nMain lagi? (y/n): ").strip().lower()
            if choice in ['y', 'ya', 'yes']:
                return True
            elif choice in ['n', 'tidak', 'no']:
                return False
            else:
                self.print_color("Pilihan tidak valid!", 'red')
                
    def goodbye_screen(self):                                                         # Layar keluar
        self.clear()
        self.show_title("TERIMA KASIH")
        self.print_color("\nTerima kasih telah bermain!", 'yellow')

        self.print_color("Sampai jumpa lagi! 👋\n", 'blue')
