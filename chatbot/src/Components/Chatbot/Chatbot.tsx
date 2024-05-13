import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import { BotMessage, BoxLeft, BoxRight, Button, ButtonBox, ChatBox, ChatContainer, Input, InputBox, UserMessage } from './styles';

interface Message {
    author: 'user' | 'VTR';
    text: string;
}

const Chatbot: React.FC = () => {
    const [message, setMessage] = useState('');
    const [conversation, setConversation] = useState<Message[]>([]);

    const initialize = async () => {
        const response = await axios.get<{ answer: string }>('http://localhost:5000/initialize');

        setConversation([
            { author: 'VTR', text: response.data.answer }
        ])
    }

    const sendMessage = async () => {
        
        // Send the message to the backend API
        const response = await axios.post<{ answer: string }>('http://localhost:5000/ask', { question: message });

        // Add the user's message and the bot's response to the conversation
        setConversation([
            ...conversation,
            { author: 'user', text: message },
            { author: 'VTR', text: response.data.answer }
        ]);

        // Clear the input field
        setMessage('');
    };

    useEffect(() => {
        initialize()
    }, [])

    return (
        <ChatContainer>
            <ChatBox>
                {conversation.map((msg, index) => (
                    <div key={index}>
                        {msg.author === 'user' ? (
                            <BoxRight>
                                <UserMessage>
                                    <strong>{msg.author}: </strong>
                                    {msg.text}
                                </UserMessage>
                            </BoxRight>
                        ) : (
                            <BoxLeft>
                                <BotMessage>
                                    <strong>{msg.author}: </strong>
                                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                                </BotMessage>
                            </BoxLeft>
                        )}
                    </div>
                ))}
            </ChatBox>
            <InputBox>
                <Input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type your message..."
                />
                <ButtonBox>
                    <Button onClick={sendMessage}>Ask Data!</Button>
                    <Button onClick={initialize}>Clear</Button>
                </ButtonBox>
                
            </InputBox>
        </ChatContainer>
    );
};

export default Chatbot;
