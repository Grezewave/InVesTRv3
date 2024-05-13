import styled from 'styled-components';

export const ChatContainer = styled.div`
    background-color: lightblue;
    height: 100%; /* Adjust height as needed */
    padding: 10px;
    display: flex;
    flex-direction: column;
    font-size: 14px;
`;

export const ChatBox = styled.div`
    height: 80%;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    border: solid gray 1px;
    border-radius: 10px;
    padding: 3px;
`;

export const InputBox = styled.div`
    height: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
`;

export const Input = styled.input`
    width: 30%;
    border-radius: 10px;
    margin: 10px 10px;
    padding: 10px;
`;

export const Button = styled.button`
    width: 100%;
    background-color: lightgreen;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
    margin: 2px 15px;
`;

export const ChatMessage = styled.div`
    margin-bottom: 10px;
    margin: 5px 5px 10px 5px;
    padding: 8px;
    border-radius: 10px;
`;

export const BoxRight = styled.div`
    display: flex;
    justify-content: flex-end;
    width: 100%;
`

export const BoxLeft = styled.div`
    display: flex;
    justify-content: flex-start;
    align-items: left;
    width: 100%;
`

export const ButtonBox = styled.div`
    display: flex;
    justify-content: space-between;
    width: 30%;
`

export const UserMessage = styled(ChatMessage)`
    background-color: #fff;
    text-align: left;
    width: fit-content;
`;

export const BotMessage = styled(ChatMessage)`
    background-color: #BFB;
    text-align: left;
    width: fit-content;
    max-width: 80%;
`;