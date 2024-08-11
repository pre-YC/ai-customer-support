//remove this as you see fit
interface placeholder {
  hello: string;
}

async function query(text: string): Promise<string> {
  const response = await fetch('http://localhost:8080/hello', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(text),
  });

  const data: placeholder = await response.json();

  return data.hello;
}

export { query };
