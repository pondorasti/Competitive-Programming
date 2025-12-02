const filePath = "input.txt";

async function main() {
  try {
    const data = await Deno.readTextFile(filePath);
    console.log("File content:", data); // Process file content here
  } catch (err) {
    console.error("Error reading the file:", err);
  }
}

main();
