'use client';

import { useEffect } from 'react';
import { GreeterClient } from '../proto/ExampleServiceClientPb'; // ✅ grpc/grpc-web
import { HelloRequest } from '../proto/example_pb'; // your generated request class

export default function Home() {
  useEffect(() => {
    const client = new GreeterClient('http://localhost:8080', null, null);

    const request = new HelloRequest();
    request.setName('Simon from gRPC-Web');

    client.sayHello(request, {}, (err, response) => {
      if (err) {
        console.error('gRPC Error:', err.message);
      } else {
        console.log('gRPC Response:', response.getMessage());
      }
    });
  }, []);

  return (
    <main>
      <h1>gRPC-Web Test</h1>
      <p>Check the browser console for the response.</p>
    </main>
  );
}
