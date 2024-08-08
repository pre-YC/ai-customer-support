'use client'

import { Box, Button, Stack, TextField } from '@mui/material'
import { useState } from 'react'

export default function Home() {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: `Hi I'm the Headstarter Support Agent, how can I help?`,
    },
  ])

  const [message, setMessage] = useState('')

  const sendMessage = async () => {
    setMessages((messages) => [
      {role: 'user', content: message},
      {role: 'assistant', content: ''},
    ])
    const response = fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify([...messages, {role: 'user', content: message}]),
    }).then( async (res) => {
      const reader = res.body.getReader()
      const decoder = new TextDecoder()

      let result = ''
      return reader.read().then(function processText({done, value}){
        if (done){
          return result
        }
        const text = decoder.decode(vaue || new Int8Array(), {stream:true})
        setMessages((messages) => {
          let lastMessage = messages[message.length - 1]
          let otherMessages = message.slice(0, messages.length - 1)
          return [
            ...otherMessages,
            {
              ...lastMessage,
              content: lastMessage.content + text,
            },
          ]
        })
        return reader.read().then(processText)
      })
    })
    }
  

  // const handleKeyPress = (event) => {
  //   if (event.key === 'Enter' && !event.shiftKey) {
  //     event.preventDefault()
  //     sendMessage()
  //   }
  // }
  // const messagesEndRef = useRef(null)

  // const scrollToBottom = () => {
  //   messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  // }

  // useEffect(() => {
  //   scrollToBottom()
  // }, [messages])
  return (
    <Box
    // ... (rest of the Box props)
    >
      <Stack
      // ... (rest of the Stack props)
      >
        <Stack
        // ... (rest of the messages Stack props)
        >
          {messages.map((message, index) => (
            // ... (message rendering code)
          ))}
          <div ref={messagesEndRef} />
        </Stack>
        <Stack direction={'row'} spacing={2}>
          <TextField
            label="Message"
            fullWidth
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            disabled={isLoading}
          />
          <Button
            variant="contained"
            onClick={sendMessage}
            disabled={isLoading}
          >
            {isLoading ? 'Sending...' : 'Send'}
          </Button>
        </Stack>
      </Stack>
    </Box>
  )
}