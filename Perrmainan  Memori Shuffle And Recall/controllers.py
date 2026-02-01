import random
from models import GameData
from views import GameView

class GameController:
    def __init__(self):
        self.model = GameData()
        self.view = GameView()
        
    def setup_game(self):
        """Setup awal permainan"""
        # Tampilkan welcome screen
        self.view.welcome_screen()
        
        # Dapatkan pengaturan pemain
        name, difficulty = self.view.get_player_settings()
        self.model.player_name = name
        self.model.difficulty = difficulty
        
    def determine_sequence_length(self):
        """Tentukan panjang sequence berdasarkan difficulty"""
        if self.model.difficulty == 'easy':
            return random.randint(3, 4)
        elif self.model.difficulty == 'medium':
            return random.randint(4, 6)
        else:  # hard
            return random.randint(6, 8)
            
    def run_round(self):
        """Jalankan satu ronde permainan"""
        # Reset untuk ronde baru
        self.model.reset()
        
        # Generate sequence
        length = self.determine_sequence_length()
        sequence = self.model.generate_sequence(length)
        
        # Tampilkan sequence
        self.view.show_sequence(sequence)
        
        # Dapatkan jawaban
        user_answers = self.view.get_answers(length)
        
        # Periksa jawaban
        success, results = self.model.check_answers(user_answers)
        
        if success:
            # Tampilkan hasil
            self.view.show_results(self.model, results)
        else:
            self.view.print_color(f"Error: {results}", 'red')
            
    def main_game_loop(self):
        """Loop utama permainan"""
        self.setup_game()
        
        play_again = True
        while play_again:
            self.run_round()
            play_again = self.view.ask_replay()
            
        self.view.goodbye_screen()