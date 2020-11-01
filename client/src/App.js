import { useState } from "react";
import { Launcher } from "react-chat-window";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";

const initialValues = [
  {
    author: "Them",
    type: "text",
    data: {
      text:
        "Welcome! Here you can ask whatever questions you want about finance",
    },
  },
  {
    author: "Them",
    type: "text",
    data: {
      text: "Ask any question you want.",
    },
  },
];

const loadingValue = {
  author: "Them",
  type: "text",
  data: {
    text: "Thinking...",
  },
};

const popper = (array = []) => {
  array.pop();
  return array;
};

function App() {
  const [isOpen, setOpen] = useState(true);
  const [messageList, setMessageList] = useState(initialValues);

  const handleOpen = () => {
    setOpen(!isOpen);
  };
  const handleMessageSent = async (message) => {
    setMessageList((currentList) => [...currentList, message, loadingValue]);
    const { data } = await axios.post("/chatbot/response", {
      data: { text: message.data.text },
      headers: {
        "content-type": "application/json",
      },
    });

    setMessageList((currentList) => [
      ...popper(currentList),
      {
        author: "Them",
        type: "text",
        data: {
          text: data,
        },
      },
    ]);
  };
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <div>
        <div className="launcher">
          <Launcher
            agentProfile={{
              teamName: "CS4395 Chatbot",
              imageUrl:
                "https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png",
            }}
            onMessageWasSent={handleMessageSent}
            messageList={messageList}
            showEmoji={false}
            isOpen={isOpen}
            handleClick={handleOpen}
            className="launcher"
          />
        </div>
      </div>
    </div>
  );
}

export default App;
