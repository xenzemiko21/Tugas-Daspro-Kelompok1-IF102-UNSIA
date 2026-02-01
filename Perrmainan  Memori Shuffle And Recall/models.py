import random

class GameData:
    """Model untuk menyimpan semua data permainan"""
    
    def __init__(self):                    
        self.sequence = []              # Urutan angka yang harus diingat
        self.user_answers = []          # input dari user                   
        self.score = 0                  # Skor permainan
        self.correct_count = 0          # skor jawaban benar
        self.total_questions = 0        # Total pertanyaan dalam ronde
        self.game_state = "ready"       # Status permainan
        self.difficulty = "medium"      # Tingkat kesulitan
        self.player_name = "Player"     # Nama pemain
        self.start_time = None          # Waktu mulai permainan
        self.end_time = None            # Waktu selesai permainan
        
    def reset(self):
        """Reset semua data untuk permainan baru"""
        self.sequence = []              # angka yang harus diingat
        self.user_answers = []          # input dari user
        self.score = 0                  # skor permainan
        self.correct_count = 0          # skor jawaban benar    
        self.game_state = "ready"       # status permainan
        self.start_time = None          # waktu mulai permainan
        self.end_time = None            # waktu selesai permainan
        
    def generate_sequence(self, length):
        """Generate urutan angka acak"""
        self.sequence = [random.randint(0, 9) for _ in range(length)]
        self.total_questions = length
        return self.sequence
        
    def check_answers(self, user_answers):
        """Periksa jawaban user terhadap sequence"""
        if len(user_answers) != len(self.sequence):
            return False, "Jumlah jawaban tidak sesuai"
            
        self.user_answers = user_answers
        results = []
        correct_count = 0
        
        for i in range(len(self.sequence)):
            is_correct = (user_answers[i] == self.sequence[i])
            if is_correct:
                correct_count += 1
                
            results.append({
                'index': i,
                'user_answer': user_answers[i],
                'correct_answer': self.sequence[i],
                'is_correct': is_correct
            })
            
        self.correct_count = correct_count
        self.calculate_score()
        return True, results
        
    def calculate_score(self):
        """Hitung skor akhir"""
        base_score = self.correct_count * 25
        
        # Bonus akurasi
        accuracy = self.get_accuracy()
        if accuracy == 100:
            bonus = 50
        elif accuracy >= 80:
            bonus = 30
        elif accuracy >= 60:
            bonus = 10
        else:
            bonus = 0
            
        self.score = base_score + bonus
        return self.score
        
    def get_accuracy(self):
        """Hitung persentase akurasi"""
        if self.total_questions == 0:
            return 0
        return (self.correct_count / self.total_questions) * 100
        
    def get_summary(self):
        """Dapatkan ringkasan hasil permainan"""
        return {
            'player': self.player_name,
            'difficulty': self.difficulty,
            'total': self.total_questions,
            'correct': self.correct_count,
            'score': self.score,
            'accuracy': self.get_accuracy()
        }