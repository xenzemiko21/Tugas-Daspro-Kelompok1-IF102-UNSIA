from controllers import GameController

def main():
    print("=" * 60)
    print("PERMAINAN MEMORI ANGKA")
    print("=" * 60)
    
    try:
        game = GameController()
        game.main_game_loop()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")
        print("Silakan jalankan program kembali.")
    finally:
        print("\n" + "=" * 60)

if __name__ == "__main__":
    main()