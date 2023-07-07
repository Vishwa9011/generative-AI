import React, { useState, ChangeEvent, FormEvent } from 'react';
import { Box, Input, Button, VStack } from '@chakra-ui/react';
import axios from 'axios';

interface Message {
     role: string;
     content: string;
}

const ChatAssistance: React.FC = () => {
     const [userInput, setUserInput] = useState<string>('');
     const [conversation, setConversation] = useState<Message[]>([]);

     const handleUserInput = (e: ChangeEvent<HTMLInputElement>) => {
          setUserInput(e.target.value);
     };

     const handleUserMessageSubmit = async (e: FormEvent<HTMLFormElement>) => {
          e.preventDefault();
          if (userInput.trim() === '') {
               return;
          }
          const userMessage: Message = {
               role: 'user',
               content: userInput.trim()
          };
          setConversation((prevConversation) => [...prevConversation, userMessage]);
          setUserInput('');

          try {
               const response = await axios.post('/query', { query: userMessage.content });
               const aiMessage: Message = {
                    role: 'assistant',
                    content: response.data.answer
               };
               setConversation((prevConversation) => [...prevConversation, aiMessage]);
          } catch (error) {
               console.error('Error:', error);
          }
     };

     return (
          <Box width="500px" mx="auto" my={8} p={4} borderWidth="1px" borderRadius="md">
               <VStack spacing={4} alignItems="stretch">
                    <Box>
                         {conversation.map((message, index) => (
                              <Box
                                   key={index}
                                   p={2}
                                   borderRadius="md"
                                   bg={message.role === 'user' ? 'gray.100' : 'blue.100'}
                              >
                                   {message.content}
                              </Box>
                         ))}
                    </Box>
                    <form onSubmit={handleUserMessageSubmit}>
                         <Input
                              type="text"
                              value={userInput}
                              onChange={handleUserInput}
                              placeholder="Type your message..."
                         />
                         <Button type="submit" colorScheme="blue">
                              Send
                         </Button>
                    </form>
               </VStack>
          </Box>
     );
};

export default ChatAssistance;
