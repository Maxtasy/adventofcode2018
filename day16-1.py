# https://adventofcode.com/2018/day/16


OPCODES = [
  "addr", 
  "addi", 
  "mulr", 
  "muli", 
  "banr", 
  "bani", 
  "borr", 
  "bori", 
  "setr", 
  "seti", 
  "gtir", 
  "gtri", 
  "gtrr", 
  "eqir", 
  "eqri", 
  "eqrr"
  ]


def apply_instruction(opcode, instr, registers):
  if opcode == "addr":
    registers[instr[3]] = registers[instr[1]] + registers[instr[2]]
  elif opcode == "addi":
    registers[instr[3]] = registers[instr[1]] + instr[2]
  elif opcode == "mulr":
    registers[instr[3]] = registers[instr[1]] * registers[instr[2]]
  elif opcode == "muli":
    registers[instr[3]] = registers[instr[1]] * instr[2]
  elif opcode == "banr":
    registers[instr[3]] = registers[instr[1]] & registers[instr[2]]
  elif opcode == "bani":
    registers[instr[3]] = registers[instr[1]] & instr[2]
  elif opcode == "borr":
    registers[instr[3]] = registers[instr[1]] | registers[instr[2]]
  elif opcode == "bori":
    registers[instr[3]] = registers[instr[1]] | instr[2]
  elif opcode == "setr":
    registers[instr[3]] = registers[instr[1]]
  elif opcode == "seti":
    registers[instr[3]] = instr[1]
  elif opcode == "gtir":
    if instr[1] > registers[instr[2]]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0
  elif opcode == "gtri":
    if registers[instr[1]] > instr[2]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0
  elif opcode == "gtrr":
    if registers[instr[1]] > registers[instr[2]]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0
  elif opcode == "eqir":
    if instr[1] == registers[instr[2]]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0
  elif opcode == "eqri":
    if registers[instr[1]] == instr[2]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0
  elif opcode == "eqrr":
    if registers[instr[1]] == registers[instr[2]]:
      registers[instr[3]] = 1
    else:
      registers[instr[3]] = 0

  return registers


def part1(input_file):
  with open(input_file, "r") as f:
    input_parts = f.read().strip().split("\n\n\n\n")
    
    samples_arr = input_parts[0].split("\n\n")

    answer = 0

    for i in range(len(samples_arr)):
      sample_parts = samples_arr[i].split("\n")
      before = list(map(int, sample_parts[0].split(":")[1].replace("[", "").replace("]", "").replace(" ", "").split(",")))
      instr = list(map(int, sample_parts[1].split(" ")))
      after = list(map(int, sample_parts[2].split(":")[1].replace("[", "").replace("]", "").replace(" ", "").split(",")))

      possible_opcodes = []

      for opcode in OPCODES:
        if apply_instruction(opcode, instr, before[:]) == after:
          possible_opcodes.append(opcode)
          
      if len(possible_opcodes) >= 3:
        answer += 1
    
    return answer


def main():
  input_file = "day16-input.txt"
  print(part1(input_file))


if __name__ == "__main__":
  main()