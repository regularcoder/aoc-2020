defmodule AOC do
  def fileToNumericList(fileInput) do
    numberLines = String.split(String.trim(fileInput), "\n")

    Enum.map(numberLines, fn n_str ->
      {n, _} = Integer.parse(n_str)
      n
    end)
  end

  def readNumericFile(fileName) do
    case File.read(fileName) do
      {:ok, body}       -> fileToNumericList(body)
      {:error, _reason} -> IO.puts "could not open file due"
    end
  end

  def findPairForSum(numbers, sum) do
    numberMap = Map.new(Enum.map(numbers, & {&1, true}))
    
    matchingPair = Enum.map(numbers, fn n ->
      if Map.get(numberMap, sum - n) do n end
    end) 
      |> Enum.filter(& !is_nil(&1))
      |> Enum.map_reduce(1, fn x, acc -> {x, x * acc} end)
  end

  def day_1 do
    findPairForSum(readNumericFile("input.txt"), 2020)
  end

  def day_2 do
    numbers = readNumericFile("input.txt")

    Enum.map(numbers, fn n ->
      {pair, multiplied} = findPairForSum(numbers, 2020 - n)

      if Enum.count(pair) > 0 do
        multiplied * n
      end
    end) |> Enum.filter(& !is_nil(&1))
  end
end
