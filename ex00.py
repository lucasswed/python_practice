def rpsls(pl1, pl2):
	d = {
		"rock": ["lizard", "scissors"],
		"paper": ["rock", "spock"],
		"scissors": ["paper", "lizard"],
		"spock": ["scissors", "rock"],
		"lizard": ["spock", "paper"],
	}

	if pl1 == pl2:
		return "Draw!"
	elif pl2 in d[pl1]:
		return "Player 1 Won!"
	else:
		return "Player 2 Won!"


def main():
	pl1 = input("Qual a tua jogada? ").lower()
	while pl1 not in ["rock", "paper", "scissors", "lizard", "spock"]:
		pl1 = input("Escolhe uma jogada válida: ").lower()

	pl2 = input("Qual a tua jogada? ").lower()

	while pl2 not in ["rock", "paper", "scissors", "lizard", "spock"]:
		pl2 = input("Escolhe uma jogada válida: ").lower()
	
	print(rpsls(pl1, pl2))

if __name__ == "__main__":
	while True:
		i = input("Deseja jogar? ").lower()
		if i in ["nao", "n", "nope", "no"]:
			break
		elif i in ["sim", "s", "yap", "yes"]:
			main()