import json

def save_data(electricity_data: dict) -> None:
	json.dump(
		electricity_data,
		open("./data.json", "w")
	)

def main():
	try:
		past_electricity_data: dict = json.load(open("./data.json", "r"))
	except:
		past_electricity_data: dict = {}
	if past_electricity_data.get("current_month") == None:
		past_electricity_data["current_month"] = int(input("Enter your current units: "))
		save_data(past_electricity_data)
		current_used: int = int(input("Enter your units used: "))
		print(f"Your current bill is: {(current_used - past_electricity_data.get("current_month")) * 0.387} MYR")

	else:
		print(f"Saved Data: {past_electricity_data.get("current_month")}\n")
		option: str = input("Modify data [y/n]: ")
		if option.lower() == "y":
			past_electricity_data["current_month"] = int(input("Enter your current units: "))
			save_data(past_electricity_data)
		elif option.lower() == "n":
			_ = None
		else:
			print("Invalid Option. Abort.")
			exit(1)
		current_used: int = int(input("Enter your units used: "))
		print(f"Your current bill is: {(current_used - past_electricity_data.get("current_month")) * 0.387} MYR")

main()