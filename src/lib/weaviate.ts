import weaviate, { WeaviateClient, ObjectsBatcher, ApiKey } from "weaviate-ts-client";

const client: WeaviateClient = weaviate.client({
  scheme: "https",
  host: "some-endpoint.weaviate.network", // Replace with your endpoint
  apiKey: new ApiKey(process.env.WEAVIATE_KEY as string), // Replace w/ your Weaviate instance API key
  headers: { "X-OpenAI-Api-Key": process.env.OPENAI_API_KEY }, // Replace w/ your OpenAI API key },
});

const response = await client.schema.getter().do();
console.log(JSON.stringify(response, null, 2));
