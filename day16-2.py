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


def part2(input_file):
  with open(input_file, "r") as f:
    input_parts = f.read().strip().split("\n\n\n\n")
    
    samples_arr = input_parts[0].split("\n\n")
    sequence_arr = input_parts[1].split("\n")

    opcodes = [OPCODES[:] for i in range(16)]

    for i in range(len(samples_arr)):
      sample_parts = samples_arr[i].split("\n")
      before = list(map(int, sample_parts[0].split(":")[1].replace("[", "").replace("]", "").replace(" ", "").split(",")))
      instr = list(map(int, sample_parts[1].split(" ")))
      after = list(map(int, sample_parts[2].split(":")[1].replace("[", "").replace("]", "").replace(" ", "").split(",")))

      impossible_opcodes = []

      for opcode in opcodes[instr[0]]:
        if apply_instruction(opcode, instr, before[:]) != after:
          impossible_opcodes.append(opcode)
      
      updated_opcodes = []
      for code in opcodes[instr[0]]:
        if code not in impossible_opcodes:
          updated_opcodes.append(code)
      opcodes[instr[0]] = updated_opcodes[:]

    # logically remove the known codes from the list of possible codes of others
    known_codes = []
    while True:
      finished = True

      for i in range(len(opcodes)):
        if len(opcodes[i]) == 1:
          known_codes.append(opcodes[i][0])
        else:
          still_possible = []

          for code in opcodes[i]:
            if code not in known_codes:
              still_possible.append(code)
          
          opcodes[i] = still_possible[:]
        
        if len(opcodes[i]) > 1:
          finished = False
      
      if finished:
        break
    
    registers = [0, 0, 0, 0]

    for instr in sequence_arr:
      instr = list(map(int, instr.split(" ")))
      registers = apply_instruction(opcodes[instr[0]][0], instr, registers[:])
    
    return registers[0]
      

def main():
  input_file = "day16-input.txt"
  print(part2(input_file))


if __name__ == "__main__":
  main()